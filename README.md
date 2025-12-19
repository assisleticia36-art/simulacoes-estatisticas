# Simulações Estatísticas e Método de Monte Carlo

Este repositório apresenta a implementação de simulações computacionais
relacionadas a variáveis aleatórias discretas e contínuas, além da aplicação
do método de Monte Carlo, conforme proposto no trabalho.

As simulações foram implementadas em Python, utilizando bibliotecas padrão
para computação científica.

## Requisitos

- Python 3.8+
- numpy
- matplotlib
- scipy

Para instalar as dependências:

pip install -r requirements.txt


## Questão 1. Simulação de Variáveis Aleatórias Discretas

Foi implementado um simulador do lançamento de um dado honesto de seis faces,
executado com 10^6 lançamentos. A distribuição empírica foi comparada com a
distribuição teórica uniforme, discutindo-se a convergência conforme a Lei dos
Grandes Números.

Arquivo: questao1_dado_justo.py

## Questão 2. Dado Não Uniforme e Probabilidade Condicional

Propôs-se uma distribuição não uniforme válida para um dado de seis faces.
Um simulador gerou amostras segundo essa distribuição, e as probabilidades
empíricas foram comparadas com os valores teóricos.

Arquivo: questao2_dado_viciado.py

## Questão 3. Simulação de Distribuição Contínua

Simulação de uma variável aleatória contínua baseada em uma distribuição normal
truncada, representando valores monetários. Foram geradas 10.000 amostras e
calculadas estatísticas descritivas, além da construção de um histograma.

Arquivo: questao3_normal_truncada.py


## Questão 4. Método de Monte Carlo Aplicado

Modelou-se um fundo com capital inicial finito que concede empréstimos sucessivos
de valores aleatórios até o esgotamento do capital. Utilizou-se simulação de Monte
Carlo para estimar o número esperado de clientes atendidos.

Arquivo: questao4_monte_carlo_fundo.py


## Questão 5. Análise Estatística e Interpretação

Os resultados das simulações foram analisados comparando teoria e prática,
discutindo fontes de erro estatístico e computacional, bem como o impacto do
número de simulações na precisão dos resultados.


## Autor Letícia Assis
