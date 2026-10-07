# Regras anti-slop (português de Portugal)

Cola este ficheiro em qualquer projeto de IA como conhecimento, ou guarda-o na pasta do projeto. É o conjunto de regras que o trabalho no CV tem de cumprir, reduzido ao que um CV, uma carta de apresentação ou um resumo de perfil precisa.

Se o assistente executa código, corre o `no_slop_check.py --lang pt` sobre o rascunho antes de exportar. Se não executa, percorre a lista de verificação no fim deste ficheiro à mão e diz o que corrigiu.

---

## 1. O ponto

Os modelos de linguagem escolhem sempre a formulação mais provável, e é por isso que o texto de IA soa todo igual. A solução não é juntar calão. É cortar as marcas estatísticas e depois escrever com concretos: números reais, ferramentas reais, nomes reais, resultados reais.

## 2. Vocabulário a cortar

Substitui, nunca mantém.

| Proibido | Em vez disso |
|---|---|
| alavancar | usar, com |
| otimizar | cortar, reduzir, simplificar, com o número |
| potencializar, potenciar | aumentar, duplicar, com o número |
| mergulhar em, desvendar | analisar, ler, percorrer, resolver |
| impulsionar, catalisar | lançar, arrancar, conduzir |
| fomentar, capacitar, empoderar | formar, ensinar, criar |
| desbloquear o potencial | nomeia o obstáculo e o resultado |
| destacando-se, realçando, salientando | mostrou, entregou, resultou em |
| sublinhar, evidenciar (como muleta) | diz a coisa e para |
| robusto | fiável, testado |
| abrangente | completo, ou nomeia as partes |
| holístico, multifacetado | nomeia as funções concretas |
| intrincado, minucioso, meticuloso | exato, rigoroso, ou um resultado que o mostre |
| crucial, imprescindível | diz por que razão importou, com um número |
| paradigmático, disruptivo, revolucionário | nomeia a versão, a data, o resultado |
| transformador, exponencial | nomeia o antes e o depois |
| emblemático, icónico, vibrante | apaga |
| sinergia, sinérgico | apaga, ou nomeia as duas partes |
| testemunho de | provou, mostrou |
| sem precedentes, notável | diz o que aconteceu de facto |
| tapeçaria (como imagem) | apaga |

Ferramentas, frameworks e relatórios têm nome próprio e ficam como estão: Django REST Framework, Kubernetes, "Global Risks Report" do Fórum Económico Mundial. Usa o nome, mantém as maiúsculas.

## 3. Frases a cortar

Todas estas são enchimento. Substitui por nada, ou pelo facto que estavam a esconder.

| Frase proibida | O que fazer |
|---|---|
| No mundo de hoje / nos dias de hoje | apaga, começa pelo facto |
| No panorama atual / no cenário atual | apaga |
| É importante notar / é importante salientar | apaga, diz a coisa |
| Importa referir / convém lembrar / vale a pena notar | apaga |
| Vamos mergulhar / vamos explorar | apaga |
| Em suma / em conclusão / para concluir / resumindo | apaga, para quando o ponto estiver feito |
| Em primeiro lugar / em segundo lugar / por último | ordena os pontos, ou usa uma frase |
| No âmbito de / no contexto de | em, para |
| Com o objetivo de / de forma a | para |
| Ao nível de / no que diz respeito a / no que toca a | em, sobre |
| Não só X mas também Y | diz os dois de forma simples |
| Espero que esteja tudo bem / espero que este email o encontre bem | apaga |
| Não hesite em contactar / fico ao seu dispor | diz o que queres que aconteça |
| Terei todo o gosto em | apaga, faz a coisa |
| Pensamento fora da caixa | nomeia a decisão |
| Pontos de dor / valor acrescentado | diz o problema e o resultado |
| Líder de pensamento | apaga |
| Mover a agulha | nomeia o número |
| Ponto de viragem | apaga |
| Um dos mais [adjetivo] | a coisa específica |

## 4. Aberturas a cortar

| Abertura proibida | Em vez disso |
|---|---|
| Claro, / Com certeza, / Certamente, | a resposta em si |
| Excelente pergunta / Boa pergunta | apaga |
| Terei todo o gosto em ajudar | apaga, faz a coisa |
| Enquanto IA / enquanto modelo de linguagem | apaga |
| Aqui está | o conteúdo |
| Além disso, / Por outro lado, / Ademais, | começa pelo sujeito |
| Desta forma, / Importa notar, | apaga |
| Com mais de N anos de experiência | o resultado que torna o número irrelevante |
| Um dos mais [adjetivo] | a coisa específica |
| Responsável por [frase] no início da linha | o verbo no passado: assumi, liderei, reconstruí |

As duas últimas pesam mais num CV. "Com mais de quinze anos de experiência em..." é a abertura mais comum em CVs escritos por IA. Não diz nada ao leitor.

## 5. Estrutura e ritmo

- Sem regra de três. Os modelos agrupam tudo em três por defeito. Usa dois, quatro, um ou cinco itens.
- Sem três frases seguidas com o mesmo comprimento. É o sinal mais mensurável de texto de máquina. Varia: uma frase curta ao lado de uma longa.
- Sem frases curtas em cadeia. Três frases declarativas seguidas soam a máquina. Liga as ideias com conjunções, ponto e vírgula ou orações subordinadas.
- Sem balanço de hesitações. Afirma; dá o contra-argumento no máximo numa frase.
- Sem voz passiva. "A migração foi concluída por mim" passa a "migrei".
- Sem parágrafo a fechar com transição. Deixa alguns parágrafos parar de repente.
- Sem parágrafos todos com a mesma forma. Frase-tópico, explicação, exemplo, transição, repetido oito vezes, é um molde.
- Marcadores desiguais, cinco a sete no máximo seguidos. Se cabe numa frase, escreve a frase.

## 6. Pontuação, língua e variante

- A língua e a variante vêm do anúncio: pt-PT, en-GB, en-US, de, fr. Ortografia, formato de data, pontuação e títulos de secção seguem esse mercado, não o padrão do assistente. Se o anúncio misturar línguas ou não for claro, usa a língua da pessoa e mantém-na no documento todo.
- Travessão longo: no máximo um por 500 palavras. Num CV, o melhor é zero. Usa vírgula, dois pontos, ponto e vírgula ou uma frase nova. Numa linha de cabeçalho, separa o cargo, a empresa e as datas com vírgulas ou uma barra.
- Ponto de exclamação: no máximo um por 1 000 palavras. Num CV, nenhum.
- Reticências: só quando algo fica mesmo em suspenso. Uma vez por documento no máximo.
- Ponto e vírgula: usa-o onde encaixa. Quem escreve bem usa-o; os modelos usam-no pouco.
- Escreve os números como o mercado espera: em Portugal, 1 500 e 34%, com o espaço fino antes do símbolo; em inglês, 1,500 e 34%.

## 7. Proibições específicas de CV

Substitui cada etiqueta pela ação e pelo resultado:

| Lugar-comum | Real |
|---|---|
| profissional orientado a resultados | o resultado que o prova, com número |
| orientado ao cliente | o cliente, o problema e o que mudou |
| dinâmico e proativo | a decisão que tomaste sem ninguém pedir |
| espírito de equipa | a equipa, o tamanho, o que entregaram juntos |
| apaixonado por [área] | o projeto que fizeste fora do horário de trabalho |
| experiência comprovada em X | os anos e a entrega, com datas |
| sólida experiência, longa experiência | o que fizeste em cada ano |
| excelentes capacidades de comunicação | quem formaste, quantos, com que resultado |
| candidato ideal, à altura do desafio | apaga |
| tarefas incluíam, funções várias | o que entregaste, com número |
| colaborei em | fiz X, que produziu Y |
| vasta gama de, trabalhador empenhado | apaga |
| Responsável pelo helpdesk | Liderei um helpdesk de 3 pessoas, 400 pedidos por mês |
| Colaborei na migração para a cloud | Movi 60 servidores para Azure em 9 meses, sem paragens não planeadas |
| Excelentes capacidades de comunicação | Formei 120 pessoas em triagem de phishing; a taxa de reporte passou de 8% para 41% |
| Apaixonado por cibersegurança | Reconstruí a via de escalonamento depois do ransomware de 2024 |
| Sólida experiência em gestão de equipas | Liderei 12 pessoas em 3 turnos, com rotação de 4 países |

## 8. Honestidade

Nunca inventes um número, uma data, um empregador, uma ferramenta ou uma qualificação. Se a evidência não está no material de origem, o resultado correto é uma lacuna, não um palpite. Diz o que falta e deixa a pessoa preencher.

## 9. Verificação antes de exportar

1. Sobrou alguma palavra ou frase proibida? Substitui.
2. Três frases seguidas com o mesmo comprimento? Quebra o ritmo.
3. Três frases curtas declarativas seguidas? Liga-as.
4. Itens agrupados em três por hábito? Muda a contagem.
5. Hesitaste em vez de afirmar? Afirma.
6. Mais de um travessão longo em 500 palavras? Corta.
7. Voz passiva? Passa a ativa.
8. Todos os parágrafos a fechar com transição? Corta alguns.
9. Algum facto inventado? Remove, ou transforma em pergunta para a pessoa.
10. Este CV podia ser de qualquer pessoa? Acrescenta algo que só esta pessoa poderia escrever.
11. Isto lê-se como texto de modelo? Reescreve até a resposta ser não.
12. O assistente falou das regras ou pediu desculpa por elas? Apaga esse texto. As regras aplicam-se em silêncio.

Reporta o resultado numa linha, por exemplo: "Passagem anti-slop: 6 correções (3 palavras proibidas, 2 travessões, 1 frase passiva)." Não devolvas a lista de regras à pessoa.

---

Adaptado da skill `ciberjohn-no-slop` de João Silva, que junta a diretiva anti-ai-slop-writing de Jalaaldeen (MIT) a uma lista de verificação própria. Fontes de deteção: Cheng et al. 2025 (Advances in Simulation); Russell, Karpinska & Iyyer 2025 (ACL); Juzek & Ward 2025; Kobak, González-Márquez, Horvát & Lause, Science Advances 11:eadt3813 (2025); "Signs of AI writing" da Wikipédia. Licença MIT.
