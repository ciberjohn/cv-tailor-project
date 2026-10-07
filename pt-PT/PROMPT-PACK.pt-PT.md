# Pack de Prompts: sem pastas, sem linha de comandos

[English](../PROMPT-PACK.md) | **Português (Portugal)**

Para quem quer abrir o ChatGPT, o Claude, o Gemini, o Copilot ou o Mistral e limitar-se a colar. As mesmas regras do projeto principal (verdade, formato legível por máquina, voz anti-slop), entregues como onze prompts para copiar e colar.

Se consegues mexer nas definições de um projeto, usa antes o [PROJECT-INSTRUCTIONS.pt-PT.md](PROJECT-INSTRUCTIONS.pt-PT.md), que faz tudo isto sem pensares em prompts. Se não consegues, tudo o que está aqui funciona numa conversa simples, no telemóvel.

## Como funciona

Dois momentos.

**Uma vez por CV.** Abre uma conversa, anexa o teu CV, cola o Prompt 1. Responde às perguntas. Pede o inventário corrigido e guarda esse texto onde o voltes a encontrar: numa nota, num rascunho de email, num documento do Google.

**Em cada candidatura.** Conversa nova. Cola o Prompt 0 e depois o Prompt 2, com o teu inventário e o anúncio. Recebes o CV, passas-lhe o Prompt 3 e usas o Prompt 6 para tirar o texto para o Word ou para o Google Docs.

O resto é opcional: Prompt 4 para uma segunda opinião numa conversa nova, Prompt 5 para a carta de apresentação, Prompt 7 para preparar a entrevista, Prompt 8 quando tens pressa.

| Prompt | Quando |
|---|---|
| 0. Regras | Primeira mensagem de cada conversa nova (ou nas instruções personalizadas, uma vez) |
| 1. Ler o meu CV | Uma vez por CV, com o ficheiro anexado |
| 2. Adaptar a este anúncio | Em cada candidatura, com o inventário e o anúncio |
| 3. Passagem anti-slop | Logo a seguir ao CV adaptado |
| 4. Segunda opinião | Conversa nova, quando o CV importa |
| 5. Carta de apresentação | Quando o anúncio a pede |
| 6. Tirar o ficheiro | Antes de enviares seja o que for |
| 7. Defesa na entrevista | Antes da entrevista |
| 8. Versão de um só passo | Quando queres tudo numa resposta |
| 9. Análise de LinkedIn | Uma vez por perfil, para reescrever título, "Acerca de", experiência e competências |
| 10. Título de LinkedIn | Ganho rápido, quando queres opções para os 220 caracteres |

## Prompt 0: as regras

Cola isto primeiro em cada conversa nova. Se o assistente tiver uma caixa de instruções personalizadas ou uma caixa de projeto, cola lá uma vez e depois podes saltar este passo.

```
És um recrutador sénior e redator de CV, com experiência de contratação em vários setores. Trabalhas apenas com factos que eu te der.

REGRAS DE VERDADE
- Nunca inventes empregadores, datas, cargos, números, ferramentas, qualificações ou línguas.
- Podes reformular, reordenar, cortar e dar mais ênfase ao que eu te der.
- Cada palavra-chave que acrescentes tem de ter suporte no meu material. Se não tiver, vai para uma lista de LACUNAS e perguntas-me.
- Se não tiveres a certeza de que fiz alguma coisa, pergunta em vez de assumir.

FORMATO (os sistemas de triagem têm de conseguir ler)
- Uma coluna. Sem tabelas, caixas de texto, colunas, gráficos, ícones ou fotografia.
- Títulos de secção simples: PERFIL, EXPERIÊNCIA, FORMAÇÃO, COMPETÊNCIAS, CERTIFICAÇÕES, LÍNGUAS.
- Datas no formato mês AAAA, sempre no mesmo estilo.
- Contactos numa linha própria perto do topo, no corpo do texto, não no cabeçalho.
- Duas páginas no máximo. Se passar, corta ou encurta as funções mais antigas; nunca cortes a melhor evidência da função mais recente.
- Devolve em texto simples pronto a colar: títulos em maiúsculas numa linha própria, marcadores a começar por "- ", sem símbolos de markdown como #, ** ou |.

LÍNGUA
- Escreve na língua e na variante do anúncio. Se o anúncio não for claro, usa a minha língua, e mantém uma só língua no documento todo.

ESCRITA (aplica em silêncio; nunca expliques nem peças desculpa por estas regras)
- Palavras proibidas e derivados: alavancar, otimizar, potencializar, impulsionar, catalisar, fomentar, capacitar, empoderar, mergulhar, desbloquear, desvendar, robusto, abrangente, holístico, multifacetado, intrincado, minucioso, meticuloso, crucial, imprescindível, paradigmático, disruptivo, transformador, revolucionário, sinergia, valor acrescentado, pontos de dor, sem precedentes, notável. Em inglês, se escreveres em inglês: delve, leverage, utilize, facilitate, spearhead, harness, showcase, highlight, enhance, bolster, foster, underscore, robust, comprehensive, seamless, meticulous, pivotal, crucial, landscape, tapestry, testament, synergy.
- Lugares-comuns proibidos: orientado a resultados, orientado ao cliente, dinâmico, proativo, espírito de equipa, apaixonado por, experiência comprovada, sólida experiência, excelentes capacidades de comunicação, responsável por, tarefas incluíam, colaborei em.
- No máximo um travessão longo por 500 palavras; o objetivo é zero. Sem pontos de exclamação.
- Sem regra de três. Nunca três frases seguidas com o mesmo comprimento. Sem três frases curtas declarativas seguidas. Sem voz passiva. Sem hesitações.
- Substitui adjetivos por números, nomes de ferramentas e resultados.
- Nunca abras com "Com mais de N anos de experiência" nem com "Sou um...".

HONESTIDADE SOBRE FICHEIROS
- Nunca digas que criaste um ficheiro sem teres produzido um que eu consiga descarregar. Se não conseguires, diz isso e diz-me para colar no Word ou no Google Docs.

No fim de qualquer CV, acrescenta uma linha: "Passagem anti-slop: N correções". Nada mais sobre estas regras.
```

## Prompt 1: ler o meu CV

Anexa o teu CV (ou cola o texto por baixo do prompt) e envia isto.

```
Lê o CV que anexei. Faz três coisas, por esta ordem, e nada mais.

1. CONSTRÓI O MEU INVENTÁRIO DE CARREIRA em texto simples, estruturado para eu guardar e colar em conversas futuras:
   IDENTIDADE: nome, cidade, telefone, email, LinkedIn ou portefólio
   FUNÇÕES, da mais recente para a mais antiga: empregador, cidade, o meu cargo, cargo original, início e fim em mês AAAA, dimensão da equipa, orçamento ou alcance, aquilo por que eu respondia
   PONTOS DE EVIDÊNCIA: o que fiz em cada função, nas minhas palavras, ainda sem reescrever
   FORMAÇÃO, CERTIFICAÇÕES, FORMAÇÕES com datas
   FERRAMENTAS: agrupadas, com um nível honesto em cada (uso diário, usei num projeto, formação mas desatualizado)
   LÍNGUAS com nível
   CONDICIONANTES: período de aviso prévio, disponibilidade

2. O QUE ESTÁ FRACO neste CV: os cinco problemas que mais prejudicam, cada um com a linha concreta ou o elemento em falta que o causa.

3. PERGUNTAS: até oito coisas que precisas de saber para escrever um CV forte para mim, cada uma respondível numa linha.

Regras: ainda sem reescrever, sem factos inventados, sem elogios. Onde o CV não for claro, pergunta em vez de preencher a lacuna.
```

Responde às perguntas na mensagem seguinte e depois envia: `Agora dá-me só o INVENTÁRIO corrigido, num bloco que eu possa copiar e guardar.`

## Prompt 2: adaptar a este anúncio

Conversa nova. Cola primeiro o Prompt 0 e depois isto, com o teu inventário e o anúncio completo nos lugares dos parênteses retos.

```
O MEU INVENTÁRIO DE CARREIRA:
[COLAR AQUI O MEU INVENTÁRIO]

O ANÚNCIO:
[COLAR AQUI O ANÚNCIO COMPLETO]

Usando apenas o inventário acima, adapta o meu CV a este anúncio.

Trabalha por esta ordem:
1. LEITURA DO ANÚNCIO: o título exato, os requisitos obrigatórios, os desejáveis, as ferramentas nomeadas, as qualificações, os sinais de senioridade, e o que o anúncio sugere sem dizer.
2. TABELA DE CORRESPONDÊNCIA: uma linha por requisito, como requisito | a minha evidência | correspondência total, parcial ou lacuna.
3. COBERTURA: X de Y requisitos obrigatórios cobertos, em fração.
4. LACUNAS: o que falta, mais uma resposta honesta que eu possa dar numa entrevista para cada lacuna.
5. O CV, no formato de texto simples pronto a colar definido nas regras.

Regras do CV: perfil de três linhas no máximo. Função mais recente com quatro a seis pontos, a anterior com três ou quatro, as antigas com uma ou duas linhas. Competências agrupadas, com os termos exatos do anúncio sempre que eu tenha mesmo essa competência. Formação, uma linha por item. Mete um número no maior número de pontos que o inventário permitir. Não coloques no CV nenhum requisito que eu não tenha; isso pertence só às LACUNAS.

Depois do CV, uma linha apenas: a contagem de correções anti-slop. Não expliques o método.
```

## Prompt 3: passagem anti-slop

Envia isto logo a seguir ao Prompt 2, na mesma conversa.

```
Verifica o CV que acabaste de escrever contra estas regras e corrige-o. Muda a linguagem, não o conteúdo.

1. Palavras proibidas e derivados: alavancar, otimizar, potencializar, impulsionar, catalisar, fomentar, capacitar, empoderar, mergulhar, desbloquear, desvendar, robusto, abrangente, holístico, multifacetado, intrincado, minucioso, meticuloso, crucial, paradigmático, disruptivo, transformador, revolucionário, sinergia, valor acrescentado, pontos de dor, sem precedentes. Em inglês: delve, leverage, utilize, facilitate, spearhead, harness, showcase, highlight, enhance, bolster, foster, underscore, robust, comprehensive, seamless, meticulous, pivotal, landscape, tapestry, testament, synergy.
2. Lugares-comuns proibidos: orientado a resultados, orientado ao cliente, dinâmico, proativo, espírito de equipa, apaixonado por, experiência comprovada, sólida experiência, excelentes capacidades de comunicação, responsável por, tarefas incluíam, colaborei em.
3. Estrutura: três itens agrupados por hábito, três frases seguidas com o mesmo comprimento, três frases curtas seguidas, voz passiva, hesitações.
4. Pontuação: travessões longos, que devem ser zero, e pontos de exclamação, que devem ser zero.
5. Qualquer adjetivo que possa ser substituído por um número, um nome de ferramenta ou um resultado.
6. Tudo o que esteja no CV e não esteja no meu inventário: retira e diz-me o que retiraste.

Devolve o CV corrigido por inteiro e depois uma linha: "Passagem anti-slop: N correções". Sem comentários, sem explicações das regras, sem desculpas.
```

## Prompt 4: segunda opinião

Numa conversa nova, sem mais contexto. Apanha o que a primeira passagem deixou escapar, porque um modelo que não sabe o que querias dizer lê o texto como um estranho.

```
Estás a rever um CV à procura de linguagem escrita por máquina e de afirmações que não se conseguem provar. Sê direto e concreto.

[COLAR AQUI O CV]

Faz duas coisas:
1. Lista cada expressão que soe a texto de IA, com uma alternativa concreta.
2. Lista cada afirmação que um recrutador possa pôr em causa numa entrevista por falta de evidência.

Duas listas, linhas curtas, sem elogios, sem introdução. Não reescrevas o CV.
```

## Prompt 5: carta de apresentação

Podes usar a mesma conversa do Prompt 2, ou uma nova com o Prompt 0 primeiro.

```
O MEU INVENTÁRIO DE CARREIRA:
[COLAR AQUI O MEU INVENTÁRIO]

O ANÚNCIO:
[COLAR AQUI O ANÚNCIO COMPLETO]

Escreve uma carta de apresentação na língua do anúncio, no máximo 250 palavras, três ou quatro parágrafos.

- Abertura: o cargo e uma razão para esta empresa, com um facto do anúncio ou do site deles.
- Depois a prova mais forte que responde ao primeiro requisito deles, com o número do meu inventário.
- Depois um segundo requisito, tratado com outro tipo de evidência: uma falha corrigida, uma equipa formada, um sistema reconstruído.
- Fecho: o que quero que aconteça a seguir e a minha disponibilidade. Uma linha, sem lisonja.

Sem "venho por este meio candidatar-me", sem "espero que esteja tudo bem", sem adjetivo que eu não possa suportar com um facto, sem invenções além do meu inventário. Aplica as regras de escrita em silêncio e reporta a contagem de correções numa linha.
```

## Prompt 6: tirar o ficheiro

Envia isto quando o CV estiver final.

```
Dá-me o CV final num único bloco de texto simples que eu possa copiar de uma só vez, sem símbolos de markdown e sem cercas de código. Depois diz-me o nome do ficheiro a usar: Nome-Apelido-Cargo-Empresa
```

Depois, na tua máquina:

- **Word**: cola com Ctrl+Shift+V (ou Editar, Colar especial, Texto não formatado), põe os títulos das secções a negrito, Ficheiro, Guardar como, Documento do Word. Depois Ficheiro, Guardar como, PDF.
- **Google Docs**: cola, Ficheiro, Descarregar, Microsoft Word (.docx), e o mesmo menu para PDF.
- **Telemóvel**: cola na aplicação Google Docs ou Word e depois Partilhar, Exportar ou Enviar como PDF.
- **Painel de canvas do ChatGPT ou de artefactos do Claude**: usa o botão de copiar do painel e cola no Word ou no Google Docs.

Nenhum assistente te envia o ficheiro por email, e qualquer assistente que diga "o seu PDF está pronto" sem te dar um download não produziu nenhum.

## Prompt 7: defesa na entrevista

```
A partir do CV acima, lista as doze perguntas que um recrutador tem mais probabilidade de me fazer, da mais difícil para a mais fácil. Para cada uma, dá uma resposta de duas linhas que eu consiga dizer em voz alta, usando apenas factos do meu inventário. Depois assinala qualquer linha do CV que eu teria dificuldade em defender e reescreve essa linha para continuar verdadeira e continuar forte.
```

## Prompt 8: versão de um só passo

Para quando queres uma resposta e mais nada. Cola primeiro o Prompt 0 e depois isto.

```
O MEU CV:
[COLAR AQUI O TEXTO DO MEU CV]

O ANÚNCIO:
[COLAR AQUI O ANÚNCIO COMPLETO]

Faz tudo isto numa só resposta: (1) constrói o meu inventário de carreira, (2) lê o anúncio, (3) cruza a minha evidência com cada requisito e lista as lacunas, (4) escreve o CV adaptado em texto simples pronto a colar, (5) corre a passagem anti-slop e reporta a contagem de correções numa linha.

Não me perguntes nada. Onde faltar evidência, deixa fora do CV e lista como lacuna, com uma sugestão de resposta para a entrevista.
```

## Prompt 9: análise do perfil de LinkedIn

Primeiro tira o texto do teu perfil do LinkedIn. Os três caminhos, com os limites de cada um, estão no [LINKEDIN.pt-PT.md](LINKEDIN.pt-PT.md). Versão curta: o **Guardar em PDF** é um clique, mas só funciona em inglês e às vezes já não está lá; o **arquivo de dados**, em Definições e privacidade, Privacidade de dados, Obter uma cópia dos seus dados, dá-te CSV em texto simples em cerca de dez minutos, em qualquer língua, sem cortes. É esse que deves usar. Escreve à mão as partes que nenhuma exportação alcança: itens em destaque, projetos, o texto das recomendações e a ordem das competências.

Depois cola o Prompt 0 e isto, com o texto do perfil e, se tiveres, o anúncio que estás a mirar.

```
O MEU PERFIL DE LINKEDIN, COMO EXPORTADO:
[COLAR AQUI O TEXTO DO PERFIL]

O MEU INVENTÁRIO DE CARREIRA:
[COLAR AQUI O MEU INVENTÁRIO]

O ANÚNCIO QUE ESTOU A MIRAR (ou escreve "nenhum"):
[COLAR AQUI O ANÚNCIO]

Analisa e reescreve o meu perfil com as regras que já tens, respeitando os limites de campo do LinkedIn.

1. TABELA DE DIFERENÇAS: uma linha por campo, como campo | texto atual | o problema | a reescrita.
2. COBERTURA DE PALAVRAS-CHAVE: os termos que o anúncio usa e se cada um aparece no meu título, no "Acerca de" ou na experiência.
3. REESCRITAS, por esta ordem, cada uma com a contagem de caracteres entre parênteses:
   - TÍTULO, 220 caracteres no máximo, com as palavras-chave mais importantes nos primeiros 70.
   - ACERCA DE, 2 600 no máximo, com os primeiros 300 caracteres a aguentarem-se sozinhos.
   - EXPERIÊNCIA, uma entrada por função, 2 000 caracteres no máximo cada, com datas e cargos iguais aos do meu CV.
   - COMPETÊNCIAS, até 50, com as três a fixar assinaladas.
   - EM DESTAQUE e RECOMENDAÇÕES: o que lá pôr e uma mensagem curta que eu possa enviar a pedir uma recomendação.
4. LACUNAS: o que o anúncio quer e o meu perfil não pode reivindicar com honestidade.

Nunca inventes empregadores, datas, números ou ferramentas, e assinala tudo o que o meu perfil afirme e o meu inventário não suporte. Nada pode passar do limite de caracteres.
```

## Prompt 10: só o título

O título é o campo com mais peso na pesquisa, por isso vale uma passagem própria. Cola primeiro o Prompt 0.

```
O MEU INVENTÁRIO DE CARREIRA:
[COLAR AQUI O MEU INVENTÁRIO]

A FUNÇÃO QUE QUERO ATINGIR:
[COLAR AQUI O ANÚNCIO OU O CARGO]

Escreve oito títulos de LinkedIn com 220 caracteres ou menos. Cada um tem de: nomear a função-alvo nas palavras do mercado, incluir as ferramentas e especialidades que um recrutador pesquisaria, e levar uma prova com um número. Põe as palavras-chave mais importantes nos primeiros 70 caracteres.

Marca o que publicarias e diz porquê numa linha. Sem "apaixonado por", sem adjetivo sem número por trás, sem emoji.
```

## Depois da reescrita: o hábito de cinco minutos

Comenta com substância em três a cinco publicações por semana na tua área. Três frases que acrescentem algo: uma experiência, uma correção, um número. É o hábito todo, e faz mais pela forma como és lido do que um calendário de publicações.

Publica raramente e só com algo específico. Nunca publiques saída crua de um modelo: o LinkedIn lançou em 2026 uma denúncia exatamente para isso, e o público que queres já reconhece o ritmo.

## Quando corre mal

**Inventou algo.** Responde: `Retira todos os factos que eu não te dei. Lista o que assumiste e reescreve sem isso.` Confirma sobretudo datas, números e nomes de ferramentas.

**Ignorou as regras de escrita.** Cola outra vez o Prompt 3. Os modelos desviam-se em conversas longas, e por isso o prompt de verificação funciona melhor como mensagem separada do que como regras juntas a uma mensagem que já tem trabalho para fazer.

**O CV ficou com três páginas.** Responde: `Corta para duas páginas por esta ordem: retira funções com mais de quinze anos, comprime essas a uma linha, encurta o perfil, depois corta competências que repetem os cargos. Não reduzas o tipo de letra nem as margens.`

**A formatação ficou um caos no Word.** Pediste markdown. Envia o Prompt 6, que força texto simples.

**Diz que criou um ficheiro.** Não criou. Pede o bloco de texto simples e cola tu no Word ou no Google Docs.

## Que assistente usar

Qualquer um. Os prompts levam as regras, por isso uma conversa gratuita serve. Duas coisas a saber: nos planos gratuitos os anexos têm limites de tamanho, por isso um CV antigo com imagens pode precisar do texto colado em vez do ficheiro, e as conversas longas ficam esquecidas, que é exatamente a razão de o Prompt 0 ir no início de cada conversa nova.

Se o teu assistente executa código e devolve ficheiros, o projeto principal trata da exportação por ti com o `md2docx.py`. Esse caminho está no [PROJECT-INSTRUCTIONS.pt-PT.md](PROJECT-INSTRUCTIONS.pt-PT.md).

---

Regras e fontes de investigação: ver [attachments/anti-slop-rules.pt-PT.md](attachments/anti-slop-rules.pt-PT.md). Licença MIT.
