# U.S. States Game 🇺🇸

Desenvolvimento de um jogo interativo de geografia utilizando a biblioteca **Turtle** e manipulação de dados com **Pandas**. Este projeto aplica conceitos de **Data Analysis**, mapeamento de coordenadas e persistência de dados.

## 🚀 Funcionalidades

* **Interface Dinâmica**: O mapa é preenchido conforme o usuário acerta os estados.
* **Sistema de Pontuação**: Contador integrado no título da janela que rastreia o progresso (ex: 5/50).
* **Mapeamento de Coordenadas**: O nome do estado é escrito na posição exata (x, y) recuperada do arquivo CSV.
* **Persistência de Aprendizado**: Ao sair, o jogo gera um arquivo `states_to_learn.csv` com todos os estados que não foram adivinhados.
* **Normalização de Texto**: Aceita entradas de texto independentemente de letras maiúsculas ou minúsculas.

## 🛠️ Tecnologias Utilizadas

* **Python 3**: Linguagem de programação.
* **Pandas**: Biblioteca para leitura e processamento de arquivos CSV.
* **Turtle Graphics**: Renderização da interface e manipulação da imagem de fundo.

## 🏗️ Estrutura do Projeto

O projeto utiliza uma estrutura focada em processamento de dados para gerenciar o fluxo do jogo:

* `main.py`: Gerencia o loop do jogo, o processamento de inputs e a lógica de verificação.
* `50_states.csv`: Base de dados contendo nomes, coordenadas X e coordenadas Y de todos os estados.
* `blank_states_img.gif`: Recurso visual do mapa utilizado como plano de fundo.
* `states_to_learn.csv`: Arquivo de saída gerado automaticamente ao encerrar o jogo.

## 🎮 Como Jogar

1.  **Pré-requisitos**: Ter o Python e a biblioteca `pandas` instalados (`pip install pandas`).
2.  **Execução**:
    ```bash
    python main.py
    ```
3.  **Controles**:
    * Digite o nome de um estado no prompt de texto.
    * Digite **"Exit"** para fechar o jogo e salvar a lista de estados restantes.

## 🧠 Conceitos Aplicados

* **Data Filtering**: Uso de filtros no Pandas para extrair a linha exata do estado adivinhado.
* **List Comprehension**: Utilizada para comparar os estados acertados com a lista completa e gerar o arquivo de revisão.
* **Screen State Management**: Uso do `screen.addshape()` para integrar arquivos de imagem customizados à biblioteca Turtle.
* **Data Persistence**: Conversão de DataFrames do Pandas para arquivos CSV para salvar o progresso de estudo.

---
*Projeto desenvolvido como parte do estudo de Python e Lógica de Programação.*