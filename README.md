# Formacao ApacheSpark Com Python Alura

Neste repositório estão alguns notebooks dos cursos da formação de Apache Spark com Python ministrado pela Alura.
Esses notebooks foram preenchidos por mim com os códigos ao longo das aulas.

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
