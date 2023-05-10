import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definir el tamaño del tablero
N = 100

# Crear el tablero
board = np.zeros((N, N))

# Inicializar algunas células vivas
board[50, 50] = 1
board[50, 51] = 1
board[50, 52] = 1
board[51, 50] = 1
board[52, 51] = 1
board[53, 54] = 1

board[50, 50] = 1
board[50, 51] = 1
board[50, 52] = 1

board[48:53, 48:53] = np.array([[0, 1, 0, 0, 0],
                                [1, 1, 0, 1, 1],
                                [0, 1, 0, 1, 0],
                                [0, 1, 0, 1, 0],
                                [0, 0, 1, 0, 0]])

board[5, 1:3] = 1
board[6, 1:3] = 1
board[5:7, 11:13] = 1
board[6, 15] = 1
board[7, 10:12] = 1
board[8, 9:11] = 1
board[9, 9] = 1
board[9, 15:17] = 1
board[10, 12] = 1
board[10, 16] = 1
board[11, 13:15] = 1
board[12, 14] = 1
board[13, 5:7] = 1
board[14, 4:6] = 1
board[14, 7:9] = 1
board[15, 3:5] = 1
board[15, 7:9] = 1
board[16, 6] = 1
board[17, 3:5] = 1
board[17, 7:9] = 1
board[18, 4:6] = 1
board[18, 7:9] = 1
board[19, 5] = 1
board[20, 5] = 1
board[21, 5:7] = 1
board[22, 4:6] = 1
board[22, 7:9] = 1
board[23, 3:5] = 1
board[23, 7:9] = 1
board[24, 6] = 1
board[25, 3:5] = 1
board[25, 7:9] = 1
board[26, 4:6] = 1
board[26, 7:9] = 1
board[27, 5] = 1
board[28, 5] = 1
board[29, 5] = 1
board[30, 6:8] = 1
board[31, 5] = 1



# Función para calcular la siguiente generación del tablero
def update_board(board):
    # Crear un nuevo tablero con las mismas dimensiones que el tablero anterior
    new_board = np.zeros(board.shape)
    # Iterar por cada célula en el tablero
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            # Calcular el número de células vivas en las celdas vecinas
            num_alive = np.sum(board[max(i-1, 0):min(i+2, board.shape[0]), max(j-1, 0):min(j+2, board.shape[1])]) - board[i, j]
            # Aplicar las reglas del juego de la vida
            if board[i, j] == 1 and (num_alive == 2 or num_alive == 3):
                new_board[i, j] = 1
            elif board[i, j] == 0 and num_alive == 3:
                new_board[i, j] = 1
    return new_board

# Función para animar el juego de la vida
def animate(frame):
    global board
    board = update_board(board)
    mat.set_data(board)
    return [mat]

# Crear la figura y el plot del tablero
fig, ax = plt.subplots()
mat = ax.matshow(board, cmap=plt.cm.binary)

# Animar el juego de la vida
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Mostrar la animación
plt.show()
