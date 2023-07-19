# Formacao ApacheSpark Com Python Alura

Neste repositório estão alguns notebooks que fiz ao longo dos cursos, dentro da Formação de Apache Spark com Python, ministrados pela Alura.


## 1- Regressão com Spark para preços de imóveis

Primeiro notebook feito foi o de Regressão com o Spark. Nele fizemos a análise de um arquivo com dados de diversos imóveis e o nosso objetivo era encontrar
um modelo que pudesse estimar melhor o preço de um imóvel. Seu uso seria para que, segundo as características que um cliente definisse, ele pudesse saber quanto seria
aproximadamente um imóvel com aquelas características.

Ao longo dessa análise foram ensinados:
- Instalar e iniciar uma sessão Spark;
- Abrir um arquivo json;
- Analisar o Schema dos dados;
- Converter para um mais amigável e que fosse possível fazer as análises e manipulações;
- Análise dos dados, com a alteração de tipo de dados, exclusão e adição de colunas;
- Criação de variáveis Dummy para preparar o dataset para um modelo de machine learning analisar;
- Vetorização dos dados;
- Criação de um modelo de Regressão Linear, preparação, carregamento e análise dos dados e métricas;
- Criação de um modelo de Árvore de Decisão para Regressão, preparação, carregamento e análise dos dados e métricas;
- Criação de um modelo de Random Forest, preparação, carregamento e análise dos dados e métricas;
- Aplicação de técnica de validação com Cross Validation;
- Teste do melhor modelo com dados fictícios;

## 2 - Classificação com Spark para previsão de Churn de clientes

Segundo notebook, foi focado em modelos de Classificação com o Spark. O objetivo foi analisar um conjunto de dados fictícios de clientes de uma empresa para
conseguir prever o Churn de um cliente.

Ao longo dessa análise foram ensinados:
- Instalar e iniciar uma sessão Spark;
- Abrir um arquivo csv;
- Analisar o Schema dos dados;
- Análise dos dados, com a alteração de tipo de dados, exclusão e adição de colunas;
- Criação de variáveis Dummy para preparar o dataset para um modelo de machine learning analisar;
- Vetorização dos dados;
- Criação de um modelo de Regressão Logística, preparação, carregamento e análise dos dados e métricas;
- Criação de um modelo de Árvore de Decisão para Classificação, preparação, carregamento e análise dos dados e métricas;
- Criação de um modelo de Random Forest, preparação, carregamento e análise dos dados e métricas;
- Aplicação de técnica de validação com Cross Validation;
- Extração dos hiperparâmetros que geraram o melhor modelo;
- Teste do melhor modelo com dados fictícios;

## 3 - NLP com Spark -  Análise e Classificação de Comentários de filmes

Terceiro notebook, focado no processo de NLP, com o objetivo de tratar os textos e criar um modelo de classificação dos comentários em "Positivo" ou "Negativo".

Os pontos estudados aqui foram:
- Instalar e iniciar uma sessão Spark;
- Abrir um arquivo csv;
- Analisar o Schema dos dados;
- Processo de limpeza dos textos com remoção de caracteres especiais e espaços;
- Tokenização dos comentários;
- Remoção das Stop Words, explorando duas bibliotecas de palavras, sendo uma da NLTK e outra nativa do Spark;
- Aplicação do conceito de Bag of Words: Contagem e vetorização das palavras, explorando o CountVectorizer e depois o HashinTF (para limitar o número de palavras contabilizadas);
- Utilização do TF-IDF, o qual, faz a ponderação das palavras;
- Vetorização da campo alvo (string) em valor númerico para inserção no modelo através da função StringIndexer do pyspark;
- Criação do Pipeline de transformação dos dados com a biblioteca do Pipeline do pyspark.ml;
- Criação e teste do modelo de Decision Tree Clissifier para classficar os comentários;

