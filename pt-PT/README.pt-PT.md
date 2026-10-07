# CV Tailor (pt-PT)

Instruções de projeto que entram em qualquer assistente capaz: Claude, ChatGPT, Mistral Vibe, Gemini, Copilot ou um agente local. Carregas um CV, colas um anúncio de emprego, recebes um CV adaptado em `.docx` e PDF que não parece escrito por uma máquina.

Versão inglesa: [README.md](../README.md)

## O problema que isto resolve

Pede a um chatbot para melhorar o teu CV e recebes três coisas por defeito: feitos inventados, uma parede de adjetivos e um PDF que um sistema de triagem não consegue ler. A pessoa chega à entrevista com afirmações que não consegue defender.

Este projeto fixa as regras primeiro. Cada ponto tem de vir de evidência que já deste, cada ficheiro tem de sair como ficheiro verdadeiro, e cada frase tem de passar uma verificação escrita contra texto de máquina.

## Como funciona

1. Carrega o teu CV atual uma vez. O assistente constrói um **Inventário de Carreira**: funções, datas, alcance, resultados, ferramentas, qualificações, línguas, mais os pontos fracos do CV e as perguntas que precisa de ver respondidas.
2. Cola um anúncio completo. O assistente cruza a tua evidência com os requisitos, diz o que corresponde, o que corresponde em parte e o que falta, e reescreve o CV contra esse anúncio.
3. Corre a passagem anti-slop e exporta dois ficheiros: um `.docx` que podes editar e um PDF que podes enviar.

Nada é inventado. A reescrita muda ênfase, ordem, redação e extensão. Se a evidência não existe, recebes uma pergunta em vez de um palpite.

## Comandos

| Comando | Resultado |
|---|---|
| `/setup` | Inventário de Carreira, problemas do CV atual, até oito perguntas |
| `/cv` + anúncio | CV adaptado, relatório de correspondência, lista de lacunas, `.docx` e PDF |
| `/cover` + anúncio | Carta de apresentação com as mesmas regras |
| `/check` | Verificação anti-slop e ATS em qualquer texto colado de volta |

## Começar

**Projeto do Claude ou do ChatGPT**: `PROJECT-INSTRUCTIONS.pt-PT.md` nas instruções do projeto, tudo o que está em `attachments/` mais o teu CV como ficheiros do projeto. Depois corre `/setup`.

**GPT personalizado**: `PROJECT-INSTRUCTIONS.pt-PT.md` na caixa de instruções, `attachments/` como ficheiros de conhecimento.

**Mistral Vibe**: o Vibe Chat e o Vibe Work aceitam documentos e correm um interpretador de código, por isso os ficheiros servem tal como estão. O Vibe Code lê `AGENTS.md`, por isso as instruções vão para lá e os anexos para `.vibe/skills/`.

**CLI de agentes** (Claude Code, Codex, Cursor, Vibe Code): `PROJECT-INSTRUCTIONS.pt-PT.md` copiado para `AGENTS.md` ou `CLAUDE.md` na pasta de trabalho, anexos ao lado.

**Caixa de instruções pequena** (campos de instruções personalizadas do ChatGPT, Gems do Gemini, Copilot): cola o Apêndice C do `PROJECT-INSTRUCTIONS.pt-PT.md`. Fica dentro dos 1 500 caracteres, que é a caixa mais pequena do mercado.

Depois envia:

> `/setup` Aqui está o meu CV atual. Constrói o Inventário de Carreira, diz-me o que está fraco e pergunta-me o que precisas.

## O que está nesta pasta

| Ficheiro | Para que serve |
|---|---|
| `PROJECT-INSTRUCTIONS.pt-PT.md` | As instruções. Também em `PROJECT-INSTRUCTIONS.pt-PT.pdf` e `.docx` |
| `PROMPT-PACK.pt-PT.md` | Nove prompts para copiar e colar, sem projeto, sem ficheiros e sem comandos |
| `attachments/anti-slop-rules.pt-PT.md` | As regras de escrita em português, autónomas, para qualquer plataforma |
| `attachments/cv-print-template.pt-PT.html` | Modelo de CV A4, pronto para impressão, uma coluna |
| `attachments/cover-letter-print-template.pt-PT.html` | Modelo de carta de apresentação A4 |

Os scripts `md2docx.py` e `no_slop_check.py` são iguais nas duas línguas e vivem em [`../attachments/`](../attachments). O verificador tem modo português:

```bash
python3 no_slop_check.py --lang pt cv-rascunho.md
```

## As três regras que fazem o trabalho

**Verdade.** Três níveis de permissão de edição. Redação, ordem e ênfase são livres. Um título apresentado pode levar um qualificador verdadeiro. Números, datas, qualificações, ferramentas e alcance precisam da tua confirmação. Uma palavra-chave do anúncio que não consegues defender vai para a lista de lacunas, não para o CV. Truques de palavras escondidas falham de qualquer maneira: os sistemas de triagem removem-nas e os recrutadores leem-nas como fraude.

**Legibilidade para a máquina.** Uma coluna, títulos de secção padrão, contactos no corpo do texto e não no cabeçalho, datas no formato `mês AAAA`, um só tipo de letra entre 10,5 e 12pt, sem tabelas, caixas de texto, ícones, fotografias ou gráficos. Duas páginas no máximo, com ordem de corte definida quando passa. A língua e a variante espelham o anúncio, português de Portugal, inglês britânico ou americano, com a ortografia e as datas desse mercado; se o anúncio não for claro, ganha a língua da pessoa.

**Voz.** O conjunto anti-slop proíbe o vocabulário e as formas de frase que fazem um texto parecer escrito por máquina: a regra de três, três frases seguidas com o mesmo comprimento, frases curtas em cadeia, voz passiva, hesitações, e a mania dos travessões. Num CV proíbe também os lugares-comuns do género, com a lista no `attachments/anti-slop-rules.pt-PT.md`. Concretos substituem tudo isso: números, nomes de ferramentas, resultados.

## Exportação a sério

As instruções trazem três caminhos de exportação, para a resposta corresponder ao que a plataforma consegue mesmo fazer.

- **Com execução de código** (Claude com análise, ChatGPT com a ferramenta de código, Mistral Vibe, agente local): `python3 md2docx.py cv.md "Nome-Apelido-Cargo-Empresa.docx"` para Word, e `weasyprint`, Chrome headless ou LibreOffice para o PDF.
- **Com ficheiros mas sem comandos** (canvas, artefactos): preenche o `cv-print-template.pt-PT.html`, imprime para PDF no navegador, ou abre o mesmo ficheiro no Word e guarda como `.docx`.
- **Só texto**: um bloco markdown único, colado no Word ou no Google Docs e exportado à mão.

O `md2docx.py` não precisa de pacotes nem de rede, e é por isso que funciona em ambientes que bloqueiam instalações. Escreve um ficheiro Office Open XML verdadeiro: parágrafos, títulos, marcadores, tabelas e código monoespaçado, tudo a partir de markdown simples.

## Uma nota sobre honestidade na ferramenta

Um assistente que diz "criei o seu PDF" sem produzir nada desperdiçou o teu tempo. As instruções proíbem essa afirmação: se a plataforma não consegue gerar um ficheiro, diz isso e aponta o caminho de exportação que serve. Todos os ficheiros deste repositório foram produzidos e abertos pelas ferramentas que descrevem.

## Créditos

O conjunto anti-slop vem da skill `ciberjohn-no-slop`, que junta a diretiva [anti-ai-slop-writing](https://github.com/jalaalrd/anti-ai-slop-writing) de Jalaaldeen (MIT) a uma lista de verificação própria.

Investigação de deteção por trás das regras: Cheng et al. 2025 (*Advances in Simulation*), Russell, Karpinska & Iyyer 2025 (ACL), Juzek & Ward 2025, Kobak, González-Márquez, Horvát & Lause (*Science Advances* 11:eadt3813, 2025), e o guia "Signs of AI writing" da Wikipédia.

Licença MIT. Leva, muda, publica.
