
def menu():
    continuar = 1
    board = []

    while continuar:
        continuar = int(input("0. Sair\n" + "1. Jogar\n"))

        if continuar:
            num = int(input("Digite o número de linhas e colunas da matriz: "))

            if num > 0:
                # Limpar e reconstruir a matriz com o novo tamanho
                if num < 3:
                    print("tamanho de matriz invalido")
                    menu()
                board = [[0] * num for _ in range(num)]
                game(num, board)
            else:
                print("Tamanho inválido. Tente novamente.")
                menu()

        else:
            print("Saindo...")

def game(num, board):
    jogada=0

    while ganhou(num, board) == 0:
        print("\nJogador ", jogada%2 + 1)
        exibe(num, board)
        try:
            linha  = int(input("\nLinha :"))
            coluna = int(input("Coluna:"))

            
            if linha > num or coluna > num:
                 raise ValueError

            elif board[linha-1][coluna-1] == 0:
                if(jogada%2+1)==1:
                    board[linha-1][coluna-1]=1
                else:
                    board[linha-1][coluna-1]=-1
            else:
                print("Nao esta vazio")
                jogada -=1
        except ValueError:
            print("valor invalido")
            jogada -=1

        if ganhou(num, board):
            print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")
            limpar(num, board)
            break

        jogada +=1
        print("Jogadas:", jogada)
        if jogada == num*num and ganhou(num, board) == 0:
            print("Velha\n")
            limpar(num, board)
            break

    
def ganhou(num, board):
    #checando linhas
    somaLinha = 0
    somaColuna = 0
    somaDiagonal = 0
    somaDiagonal2 = 0
    for i in range(num):
        for j in range(num):
            somaLinha = somaLinha+ board[i][j]
            if somaLinha==num or somaLinha ==-num:
                i = 0
                j = 0
                return 1

     #checando colunas
    for i in range(num):
        for j in range(num):
                somaColuna = somaColuna+ board[j][i]
                if somaColuna==num or somaColuna ==-num:
                    i = 0
                    j = 0
                    return 1

    #checando diagonais
    for i in range(num):
        somaDiagonal = somaDiagonal+board[i][i]
        if somaDiagonal== num or somaDiagonal == -num:
            i = 0
            j = 0
            return 1
    for i in range(num): 
                somaDiagonal2 += board[i][num - 1 - i]
                if somaDiagonal2== num or somaDiagonal2 == -num:
                    i = 0
                    j = 0
                    return 1

    return 0

def exibe(num, board):
    for i in range(num):
        for j in range(num):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()
def limpar(num, board):
    for i in range(num):
        for j in range(num):
            board[i][j] = 0
            

menu()