import turtle
import pandas
from subtitles import Subtitles

"""
Módulo principal: Gerencia o loop do jogo, validação de dados e interface.
"""

TOTAL_STATES = 50 # Define a constante de total de estados

# Configuração da interface gráfica
screen = turtle.Screen() # Inicializa a tela do turtle
screen.title("U.S. States Game") # Define o título da janela
screen.setup(width=725, height=491) # Configura o tamanho da janela para o tamanho do GIF

# Inicialização da classe de escrita e carregamento do mapa
subtitles = Subtitles() # Cria a instância da classe de legendas
image = "blank_states_img.gif" # Define o caminho da imagem do mapa
screen.addshape(image) # Adiciona o formato da imagem ao turtle
turtle.shape(image) # Altera o cursor para o formato da imagem do mapa

# Configurações de sistema para a janela
canvas = screen.getcanvas() # Obtém o canvas do tkinter
root = canvas.winfo_toplevel() # Acessa a janela raiz do sistema
game_is_on = True # Define a variável de controle do loop do jogo

# Processamento de dados com Pandas
data = pandas.read_csv("50_states.csv") # Carrega o arquivo CSV com os dados dos estados
all_states = data.state.to_list() # Converte a coluna 'state' em uma lista Python
guessed_states = [] # Inicializa a lista vazia para armazenar os acertos

while game_is_on: # Inicia o loop principal do jogo
    # Solicita a resposta do usuário e padroniza para título
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()

    # Condição de saída manual
    if answer_state == "Exit": # Se o usuário digitar 'Exit'
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False # Altera a variável para encerrar o loop
        print("Você encerrou o jogo") # Imprime mensagem de encerramento no console

    # Validação da resposta e lógica de escrita
    if answer_state in all_states and answer_state not in guessed_states: # Se a resposta existir na lista de estados e ela não for repetida
        guessed_states.append(answer_state) # Adiciona o estado à lista de acertos
        state_data = data[data.state == answer_state] # Filtra os dados daquele estado específico
        
        # Chama o método de escrita passando o nome e as coordenadas convertidas
        subtitles.write_state(answer_state, int(state_data.x.item()), int(state_data.y.item()))

        print(f"Total de estados descobertos: {len(guessed_states)} de 50 estados") # Exibe contagem parcial
        print(guessed_states) # Imprime a lista de estados já encontrados
    
    # Verificação de vitória
    if len(guessed_states) == TOTAL_STATES: # Se a lista de acertos chegar a 50
        print(f"Fim de jogo! Você descobriu todos os {TOTAL_STATES} estados") # Mensagem de vitória
        game_is_on = False # Encerra o jogo

turtle.mainloop() # Mantém a janela aberta após o fim do loop