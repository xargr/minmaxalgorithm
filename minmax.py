import math

def minmax(M, isMaxTurn):
    if M < 0:
        return 0

    if M == 0:
        if isMaxTurn:
            return math.inf
        else:
            return -math.inf

    
    if isMaxTurn:
        return max([minmax(M - 1, not isMaxTurn), minmax(M - 2, not isMaxTurn), minmax(M - K, not isMaxTurn)])
    else:
        return min([minmax(M - 1, not isMaxTurn), minmax(M - 2, not isMaxTurn), minmax(M - K, not isMaxTurn)])

    


if __name__ == '__main__':
    game_active = True
    M = 5
    K = 4
    isMaxTurn = True
    
    while game_active:
        # if not M:
        #     M = int(input("Give us the number of cubes: \n"))

        # if not K:
        #     K = int(input("Give us the number for K variable: \n"))

        # if K <= 2:
        #     print("The variable K must be greater than 2 \n\n")
        #     K = None
        #     continue

        # if K >= M:
        #     print("The variable K must be less than total cubes number \n\n")
        #     K = None
        #     continue

        print("\n\nRemaing cubes: " + str(M) + "\n\n")

        if not isMaxTurn:
            user_input = int(input("give a number of cubes you want to substract: \n\n"))
            if ((user_input != 1) and (user_input != 2) and (user_input != K)):
                print("\n\n\n\nNot a valid number try again... \n\n\n\n")
                continue
            M -= user_input

        if M < 0:
            print("\n\n\n\n you lose... \n\n\n\n")
            game_active = False

        if M == 0:
            print("\n\n\n\n you won...!!!!! \n\n\n\n")
            game_active = False

        if not isMaxTurn:
            isMaxTurn = True
            continue

        best_move = minmax(M, isMaxTurn)

        M -= best_move

        if isMaxTurn:
            print("\n\n best move for agent is: " + str(best_move) + "\n\n")
        

        if M > 0:
            isMaxTurn = False
            continue

        if M == 0:
            print("\n\n\n\n agent won... \n\n\n\n")
            game_active = False
        
        if M < 0:
            print("\n\n\n\n agent lost...!!! \n\n\n\n")
            game_active = False

    