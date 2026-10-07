#!/usr/bin/env python3
"""md2docx.py - convert a plain Markdown CV to .docx using only the Python standard library.

No pip install. No internet. Works in any sandbox that has Python 3 (ChatGPT, Claude analysis,
Mistral, local shell). Word, LibreOffice, Google Docs and Pages all open the result.

Supported Markdown subset (deliberately small, because a CV needs nothing more):
  # H1              -> name (large, bold)
  ## H2             -> section heading (bold, rule under it)
  ### H3            -> role line (bold, colour)
  - item / * item   -> bullet
  1. item           -> numbered bullet
  plain paragraph   -> body paragraph
  **bold** inline   -> bold run
Design flags:
  --accent RRGGBB   heading colour (default 1F3864, a dark navy)
  --font NAME       body font (default Calibri)
  --size PT         body size in points (default 10.5)
Usage:
  python3 md2docx.py cv.md cv.docx [--accent 1F3864] [--font Calibri] [--size 10.5]
"""
import sys
import html as H
import re
import zipfile

CT = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
    '<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
    '</Types>'
)

RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
    '</Relationships>'
)

DOC_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>'
    '</Relationships>'
)

NUMBERING = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    '<w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="hybridMultilevel"/>'
    '<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="\u2022"/>'
    '<w:lvlJc w:val="left"/><w:pPr><w:ind w:left="360" w:hanging="180"/></w:pPr>'
    '<w:rPr><w:rFonts w:ascii="Symbol" w:hAnsi="Symbol" w:hint="default"/></w:rPr></w:lvl>'
    '</w:abstractNum>'
    '<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>'
    '<w:abstractNum w:abstractNumId="1"><w:multiLevelType w:val="hybridMultilevel"/>'
    '<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/><w:lvlText w:val="%1."/>'
    '<w:lvlJc w:val="left"/><w:pPr><w:ind w:left="360" w:hanging="180"/></w:pPr></w:lvl>'
    '</w:abstractNum>'
    '<w:num w:numId="2"><w:abstractNumId w:val="1"/></w:num>'
    '</w:numbering>'
)

styles_doc = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>
<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>
</w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="100" w:line="252" w:lineRule="auto"/></w:pPr></w:pPrDefault>
</w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/></w:style>
<w:style w:type="paragraph" w:styleId="ListParagraph"><w:name w:val="List Paragraph"/>
<w:pPr><w:spacing w:after="40"/></w:pPr></w:style>
</w:styles>"""

NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'


def esc(text):
    return H.escape(text, quote=False)


def runs(text, size, bold, color=None, font=None):
    """Split **bold** and `code` spans into separate runs."""
    out = []
    for chunk in re.split(r'(\*\*.+?\*\*|`[^`]+`)', text):
        if not chunk:
            continue
        mono = chunk.startswith('`') and chunk.endswith('`') and len(chunk) > 2
        is_bold = (not mono) and chunk.startswith('**') and chunk.endswith('**') and len(chunk) > 4
        body = chunk[1:-1] if mono else (chunk[2:-2] if is_bold else chunk)
        use_font = 'Consolas' if mono else font
        rpr = ''
        if use_font:
            rpr += f'<w:rFonts w:ascii="{use_font}" w:hAnsi="{use_font}"/>'
        if is_bold or bold:
            rpr += '<w:b/>'
        if size:
            rpr += f'<w:sz w:val="{size - 2 if mono else size}"/>'
        if mono:
            rpr += '<w:color w:val="1F2328"/>'
        elif color:
            rpr += f'<w:color w:val="{color}"/>'
        rpr = f'<w:rPr>{rpr}</w:rPr>' if rpr else ''
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(body)}</w:t></w:r>')
    return ''.join(out)


def para(inner, after=100, before=0, numid=None, border=False, indent=None, justify=False, shade=None):
    ppr = '<w:pPr>'
    if numid:
        ppr += f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{numid}"/></w:numPr>'
    if border:
        ppr += ('<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="AAAAAA"/></w:pBdr>')
    if shade:
        ppr += f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>'
    if indent:
        ppr += f'<w:ind w:left="{indent}"/>'
    if justify:
        ppr += '<w:jc w:val="both"/>'
    ppr += f'<w:spacing w:before="{before}" w:after="{after}"/>'
    ppr += '<w:keepNext/>' if border else ''
    ppr += '</w:pPr>'
    return f'<w:p>{ppr}{inner}</w:p>'


def table_xml(rows, font, half, accent):
    """Render markdown pipe rows as a real Word table."""
    cols = max(len(r) for r in rows)
    rows = [r + [''] * (cols - len(r)) for r in rows]
    width = 9866 // cols
    borders = ('<w:tblBorders>' + ''.join(
        f'<w:{e} w:val="single" w:sz="4" w:space="0" w:color="C9CFD8"/>'
        for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV')) + '</w:tblBorders>')
    parts = ['<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/>' + borders +
             '<w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:left w:w="90" w:type="dxa"/>'
             '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="90" w:type="dxa"/></w:tblCellMar></w:tblPr>'
             '<w:tblGrid>' + ''.join(f'<w:gridCol w:w="{width}"/>' for _ in range(cols)) + '</w:tblGrid>']
    for r_i, row in enumerate(rows):
        head = r_i == 0
        cells = []
        for cell in row:
            shade = '<w:shd w:val="clear" w:color="auto" w:fill="F2F4F7"/>' if head else ''
            cells.append(f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shade}</w:tcPr>'
                         + para(runs(cell, half, head, accent if head else None, font), after=20)
                         + '</w:tc>')
        trpr = '<w:trPr><w:tblHeader/></w:trPr>' if head else ''
        parts.append(f'<w:tr>{trpr}{"".join(cells)}</w:tr>')
    parts.append('</w:tbl>' + para('', after=80))
    return ''.join(parts)


def split_row(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def convert(md, accent='1F3864', font='Calibri', size_pt=10.5):
    half = int(round(size_pt * 2))
    body = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.lstrip().startswith('```'):
            i += 1
            code = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                code.append(lines[i])
                i += 1
            i += 1
            for cl in code:
                body.append(para(runs(cl or ' ', half, False, '1F2328', 'Consolas'),
                                 after=0, indent=170, shade='F5F6F8'))
            body.append(para('', after=80))
            continue
        if line.lstrip().startswith('|'):
            block = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                block.append(lines[i])
                i += 1
            rows = [split_row(b) for b in block
                    if not re.match(r'^\|[\s:\-|]+\|?$', b.strip())]
            if rows:
                body.append(table_xml(rows, font, half, accent))
            continue
        i += 1
        if line.startswith('#### '):
            body.append(para(runs(line[5:], half, True, accent, font), after=40, before=140))
        elif line.startswith('### '):
            body.append(para(runs(line[4:], half, True, accent, font), after=20, before=120))
        elif line.startswith('## '):
            body.append(para(runs(line[3:].upper(), half + 2, True, accent, font),
                             after=50, before=220, border=True))
        elif line.startswith('# '):
            for part in line[2:].split('|'):
                first = part is line[2:].split('|')[0]
                if first:
                    body.append(para(runs(part.strip(), half + 22, True, accent, font), after=20))
                else:
                    body.append(para(runs(part.strip(), half + 2, False, '555555', font), after=20))
        elif re.match(r'^\s*[-*+]\s+', line):
            body.append(para(runs(re.sub(r'^\s*[-*+]\s+', '', line), half, False, None, font),
                             after=40, numid=1))
        elif re.match(r'^\s*\d+[.)]\s+', line):
            body.append(para(runs(re.sub(r'^\s*\d+[.)]\s+', '', line), half, False, None, font),
                             after=40, numid=2))
        elif line.strip() in ('---', '***'):
            body.append(para('', after=60))
        else:
            body.append(para(runs(line.strip(), half, False, None, font)))

    doc = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           f'<w:document {NS}><w:body>{"".join(body)}'
           '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
           '<w:pgMar w:top="850" w:right="1020" w:bottom="850" w:left="1020" w:header="0" w:footer="0" w:gutter="0"/>'
           '</w:sectPr></w:body></w:document>')
    return doc, styles_doc.format(font=font, sz=half)


def main(argv):
    args = [a for a in argv[1:]]
    opts = {'--accent': '1F3864', '--font': 'Calibri', '--size': '10.5'}
    pos = []
    i = 0
    while i < len(args):
        if args[i] in opts:
            opts[args[i]] = args[i + 1]
            i += 2
        else:
            pos.append(args[i])
            i += 1
    if len(pos) < 2:
        print(__doc__)
        return 2
    src, dst = pos[0], pos[1]
    with open(src, encoding='utf-8') as fh:
        md = fh.read()
    doc, styles = convert(md, opts['--accent'].lstrip('#'), opts['--font'], float(opts['--size']))
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', CT)
        z.writestr('_rels/.rels', RELS)
        z.writestr('word/_rels/document.xml.rels', DOC_RELS)
        z.writestr('word/document.xml', doc)
        z.writestr('word/styles.xml', styles)
        z.writestr('word/numbering.xml', NUMBERING)
    print(f'wrote {dst} ({len(md)} chars of markdown in)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
