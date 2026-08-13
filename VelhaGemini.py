from random import randrange

def display_board(board):
    # Imprime o tabuleiro no console formatado com as linhas e colunas
    print("+-------" * 3 + "+")
    for row in range(3):
        print("|       " * 3 + "|")
        for col in range(3):
            print(f"|   {board[row][col]}   ", end="")
        print("|")
        print("|       " * 3 + "|")
        print("+-------" * 3 + "+")


def enter_move(board):
    # Pergunta ao usuário sobre sua jogada, valida e atualiza o tabuleiro
    while True:
        move = input("Digite seu movimento (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Entrada inválida! Digite um número de 1 a 9.")
            continue
        
        move = int(move) - 1 # Converte para índice 0-8
        row = move // 3
        col = move % 3
        
        if (row, col) not in make_list_of_free_fields(board):
            print("Essa casa já está ocupada! Escolha outra.")
            continue
            
        board[row][col] = 'O'
        break


def make_list_of_free_fields(board):
    # Navega pelo tabuleiro e retorna uma lista de tuplas (linha, coluna) das casas livres
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields


def victory_for(board, sign):
    # Verifica linhas, colunas e diagonais para ver se o jogador (sign) ganhou
    # Linhas e Colunas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
            
    # Diagonais
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
        
    return False


def draw_move(board):
    # Sorteia uma jogada válida para o computador ('X')
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        index = randrange(len(free_fields))
        row, col = free_fields[index]
        board[row][col] = 'X'


# --- FLUXO PRINCIPAL DO JOGO ---
if __name__ == "__main__":
    # Inicializa o tabuleiro com os números de 1 a 9
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    
    # O computador faz a primeira jogada no centro (regra do exercício)
    board[1][1] = 'X'
    
    while True:
        display_board(board)
        
        # Turno do Jogador
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("Parabéns! Você ganhou!")
            break
            
        if not make_list_of_free_fields(board):
            display_board(board)
            print("Empate!")
            break
            
        # Turno do Computador
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("O computador venceu!")
            break
            
        if not make_list_of_free_fields(board):
            display_board(board)
            print("Empate!")
            break