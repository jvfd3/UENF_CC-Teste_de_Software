# Lista

## 1. O que é qualidade do produto e qual a sua relação com os softwares?

1. A qualidade do produto é o processo de garantir e assegurar que seu funcionamento esteja correto e atenda os requisitos predeterminados.  
2. Qualidade de software segue os mesmos princípios, 
3. Identificar os bugs o quanto antes trará um bom custo-benefício pois o custo de consertá-los será menor.
4. [The Relationships between Software Development Processes and Software Product Quality][SoftQual]
    1.Existem diversas visões quanto à qualidade, cada uma delas válida em um determinado contexto.
    2. Segundo o padrão ISO 9000:2005 qualidade é definida como “o grau ao qual um conjunto de características inerentes cumprem os requisitos” ou “cumprem uma necessidade ou expectativa que foi definida, geralmente implícita ou obrigatória”
5. Métricas de Qualidade:
    1. Com o estudo das necessidades dos clientes, coleta de requisitos e a medição e gerenciamento de satisfação do cliente temos o Customer Focus, que é uma qualidade de produto.
    2. Reduzindo as variações de processo e atingindo melhoria da qualidade contínua, tem-se qualidade reforçada do produto (Process Improvement).
    3. Human Side of Quality: Cultura de qualidade de toda a empresa, incluindo liderança, apoio de alta gerência, inclusão de todos os colaboradores.
6. Para a [ISO 9000 e 9001][ISO9000], "qualidade significa adequação e conformidade a normas e requisitos previamente estabelecidos." Considerando os benefícios de se atender a um padrão previamente estabelecido e mundialmente reconhecido, pode-se considerar que esta conformidade tende a ser positiva também no desenvolvimento de softwares, visto que eles seguirão boas normas bem definidas segundo algum conjunto de regras.

## 2. Como testes de software podem garantir a qualidade do software?

1. Considerando “erro” como a diferença entre o que se esperava e o que foi obtido, podemos definir teste como o processo de identificar erros.
2. Permitem identificar erros. Ou seja, os testes evidenciam a diferença entre o esperado e o obtido.
3. Dessa forma, testes podem garantir a qualidade ao ressaltar defeitos e requisitos não atendidos permitindo que sejam corrigidos.
4. Em linhas gerais, quanto maior a cobertura de testes, mais confiável é o software.
5. Garantem a estabilidade do software
6. Permite refinar o software aumentando sua confiabilidade e desempenho para os usuários final
7. Verificar se os requisitos funcionais e não-funcionais foram implementados corretamente

## 3. Explique os tipos de testes funcionais e os não funcionais

1. Testes funcionais são resumidamente verificar se a aplicação está apta a realizar as funções na qual foi desenvolvida para fazer. Testes não-funcionais tem como objetivo testar aspectos do software que não são associados a funcionalidades mas sim a restrições. Tais testes visam verificar os requisitos que tendem a ser aqueles que “inspiram” a qualidade do sistema. Ex: escalabilidade, desempenho, segurança.
2. Os requisitos funcionais especificam o que um sistema deve fazer, enquanto os requisitos não funcionais descrevem como ele fará isso.
3. A principal técnica utilizada nos testes funcionais é a de particionamento de equivalência, cujo objetivo é dividir as entradas de valores em subconjuntos, de acordo com as funcionalidades do software, com o objetivo específicos(Por exemplo, inserir dados para validar a inserção dos mesmos). Visa aumentar a confiabilidade do software.
4. Outra técnica é a Análise do Valor Limite, que é uma extensão do particionamento de equivalência, usada para exercitar os limites do domínio de entrada. Visa descobrir a maior quantidade de defeitos possíveis com o menor esforço possível.
5. Exemplos de testes não funcionais são o teste de carga e estresse, que visam testar a confiabilidade e segurança do software, além de testar os limites da aplicação, submetendo-a a situações complicadas para avaliar o seu desempenho.
6. Além dos testes funcionais, existem também os [testes estruturais][TestControl] que envolvem o Teste de Fluxo de Controle que consiste em criar uma abstração do código em formato de gráfico de tal forma que todos os fluxos possíveis estejam descritos, em seguida definir testes tais que todos os nós do grafo sejam alcançados. Existem também os [testes de aceitação][TestAccept] que averiguam se o software desenvolvido está apropriado para uso dos usuários finais. Já o [teste de unidade][TestUnit] visa focar na menor unidade possível de código, testando diversos inputs e checando se os outputs desta unidade estão de acordo com o esperado.
<!-- 7. <del>Testes funcionais são conhecidos como testes de caixa preta. Ou seja, são testes que consideram o software como uma função e analisa suas entradas e saídas (domínio e [analisar se isso é verdade]</del> -->

## 4. Explique o que são os testes Caixa branca, Caixa preta e caixa cinza? Como eles se aplicam aos testes de software e quais ferramentas podem ser utilizadas para isto?

1. Teste de caixa preta são testes que não têm acesso aos mecanismos internos do que está sendo testado. Ou seja, a pessoa testadora utiliza apenas dos inputs e outputs para testar a aplicação.
   1. Dentre as ferramentas utilizadas para isso podemos citar: engenharia reversa, asserting.
2. Teste de caixa branca são o oposto, situação na qual se têm acesso a todas as informações do software tais como código fonte, diagramas, documentação, etc.
   1. Ferramentas de análise estática e dinâmica.
3. Já o teste caixa cinza é aquele que está entre a caixa preta e a caixa branca. Situação onde se tem acessso a algumas informações do software mas não acesso completo.

## 5. Em qual tipo de teste (caixa branca, caixa preta ou caixa cinza) se enquadram os testes automatizados?

[Kenzie][TestAuto] “Testes automatizados são programas que executam testes em softwares que estão em construção de uma forma padronizada, sem ser necessário a intervenção humana.” Com isso, podemos considerar que os testes automatizados podem ser aplicados para todos os três tipos de testes.

<!-- Links -->

[SoftQual]: https://www.researchgate.net/publication/300710746_The_Relationships_between_Software_Development_Processes_and_Software_Product_Quality
[ISO9000]: https://www.siteware.com.br/qualidade/iso-9000/
[TestControl]: https://www.inf.pucrs.br/~zorzo/sd/TesteFluxoDeControle.pdf
[TestAccept]: https://www.cin.ufpe.br/~gta/rup-vc/core.base_rup/guidances/concepts/acceptance_testing_12A0F152.html
[TestUnit]: https://homepages.dcc.ufmg.br/~figueiredo/disciplinas/aulas/testes-de-unidade_v01.pdf
[TestAuto]: https://kenzie.com.br/blog/testes-automatizados/
