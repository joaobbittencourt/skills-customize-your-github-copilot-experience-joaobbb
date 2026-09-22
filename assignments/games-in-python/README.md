
# 📘 Assignment: Hangman Game

## 🎯 Objetivo

Pratique manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória em Python construindo um jogo da Forca. O jogador deverá adivinhar uma palavra oculta antes de esgotar o número máximo de tentativas incorretas.

## 📝 Tarefas

### 🛠️ Implementar o estado inicial do jogo

#### Descrição

Use o arquivo `starter-code.py` para preparar os dados necessários antes do início da partida.

#### Requisitos

O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida usando o módulo `random`.
- Inicializar uma coleção para armazenar as letras já informadas.
- Definir o número máximo de tentativas incorretas e o estado inicial do jogo.

### 🛠️ Criar o loop de palpites

#### Descrição

Implemente o loop principal para que o jogador informe letras e acompanhe o progresso da palavra oculta.

#### Requisitos

O programa concluído deve:

- Solicitar ao jogador um palpite de letra.
- Exibir a palavra usando as letras corretas descobertas e um marcador como `_` para as letras restantes.
- Atualizar o progresso quando o palpite estiver na palavra.
- Reduzir o número de tentativas restantes quando o palpite estiver incorreto.
- Continuar a partida enquanto a palavra não for descoberta e ainda houver tentativas disponíveis.

### 🛠️ Exibir o resultado da partida

#### Descrição

Finalize a partida exibindo uma mensagem adequada para cada resultado possível.

#### Requisitos

O programa concluído deve:

- Exibir uma mensagem de vitória quando todas as letras da palavra forem descobertas.
- Exibir uma mensagem de derrota quando o jogador atingir o limite de tentativas incorretas.
- Revelar a palavra secreta ao final de uma partida perdida.