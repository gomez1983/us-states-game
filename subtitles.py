from turtle import Turtle

class Subtitles(Turtle):
    """
    Classe responsável pela renderização de textos no mapa dos EUA.
    Herda da classe Turtle para utilizar métodos de desenho e movimentação.
    """
    def __init__(self):
        """
        Configura as propriedades iniciais da instância para escrita.
        Define cor, levanta a caneta e oculta o cursor para uma renderização limpa.
        """
        super().__init__() # Inicializa a classe pai Turtle
        self.color("black") # Define a cor do texto para preto
        self.penup() # Levanta a caneta para evitar riscos ao se mover
        self.hideturtle() # Esconde o ícone da tartaruga
        self.speed("fastest") # Garante movimentação instantânea entre coordenadas

    def write_state(self, name: str, x: int, y: int): # Recebe nome (string) e coordenadas (inteiros)
        self.goto(x, y) # Move o cursor para a posição X e Y do estado
        self.write(name, align="center", font=("Arial", 8, "normal")) # Escreve o nome formatado na tela