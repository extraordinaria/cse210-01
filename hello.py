#tic-tac-toe: Veronica Bardales Velasquez
from ast import Break
from tracemalloc import stop


def main():
    print ("Welcome to TIC-TAC-TOE")
    print ("You are the first player (x) and your partner is the second player (o)")
    list_tic = [1,2,3,4,5,6,7,8,9]
    show_michi(list_tic)

    for i in range(0,4):
        ask_x_player(list_tic)
        x_win = find_winner(list_tic)
        if x_win == "The X Player won":
            print (x_win)
            break
        
        show_michi(list_tic)

        ask_o_player(list_tic)
        o_win = find_winner(list_tic)
        if o_win == "The O Player won":
            print (o_win)
            break

        show_michi(list_tic)
        i=i+1
    
    ask_x_player(list_tic)
    x_win = find_winner(list_tic)
    if x_win == "The X Player won":
        print (x_win)
    print("The play is over.")

def show_michi(list_tic):
    print(f'{list_tic[0]}|{list_tic[1]}|{list_tic[2]}\n-|-|-\n{list_tic[3]}|{list_tic[4]}|{list_tic[5]}\n-|-|-\n{list_tic[6]}|{list_tic[7]}|{list_tic[8]}')

def ask_x_player(list_tic):
    player_x = 10
    
    while player_x < 1 or player_x > 9:
        try:
            player_x = int(input("x: Please, enter one number from 1 to 9 that is available: "))
            if player_x == 1 and list_tic[0] != "x" and list_tic[0] != "o":
                list_tic[0] = "x"
            elif player_x == 2 and list_tic[1] != "x" and list_tic[1] != "o":
                list_tic[1] = "x"
            elif player_x == 3 and list_tic[2] != "x" and list_tic[2] != "o":
                list_tic[2] = "x"
            elif player_x == 4 and list_tic[3] != "x" and list_tic[3] != "o":
                list_tic[3] = "x"
            elif player_x == 5 and list_tic[4] != "x" and list_tic[4] != "o":
                list_tic[4] = "x"
            elif player_x == 6 and list_tic[5] != "x" and list_tic[5] != "o":
                list_tic[5] = "x"
            elif player_x == 7 and list_tic[6] != "x" and list_tic[6] != "o":
                list_tic[6] = "x"
            elif player_x == 8 and list_tic[7] != "x" and list_tic[7] != "o":
                list_tic[7] = "x"
            elif player_x == 9 and list_tic[8] != "x" and list_tic[8] != "o":
                list_tic[8] = "x"
            else:
                player_x = 10
        except ValueError:
            print("Enter a correct integer")
            continue
        
        
        

def ask_o_player(list_tic):
    player_o = 10
    
    while player_o < 1 or player_o > 9:
        try:
            player_o = int(input("o: Please, enter one number from 1 to 9 that is available: "))
            if player_o == 1 and list_tic[0] != "x" and list_tic[0] != "o":
                list_tic[0] = "o"
            elif player_o == 2 and list_tic[1] != "x" and list_tic[1] != "o":
                list_tic[1] = "o"
            elif player_o == 3 and list_tic[2] != "x" and list_tic[2] != "o":
                list_tic[2] = "o"
            elif player_o == 4 and list_tic[3] != "x" and list_tic[3] != "o":
                list_tic[3] = "o"
            elif player_o == 5 and list_tic[4] != "x" and list_tic[4] != "o":
                list_tic[4] = "o"
            elif player_o == 6 and list_tic[5] != "x" and list_tic[5] != "o":
                list_tic[5] = "o"
            elif player_o == 7 and list_tic[6] != "x" and list_tic[6] != "o":
                list_tic[6] = "o"
            elif player_o == 8 and list_tic[7] != "x" and list_tic[7] != "o":
                list_tic[7] = "o"
            elif player_o == 9 and list_tic[8] != "x" and list_tic[8] != "o":
                list_tic[8] = "o"
            else:
                player_o = 10
        except ValueError:
            print("Enter a correct integer")
            continue
        
        
        

def find_winner(list_tic):
    if (list_tic[0]=="x" and list_tic[1]=="x" and list_tic[2]=="x") or (list_tic[3]=="x" and list_tic[6]=="x" and list_tic[0]=="x") or (list_tic[0]=="x" and list_tic[4]=="x" and list_tic[8]=="x") or (list_tic[1]=="x" and list_tic[4]=="x" and list_tic[7]=="x") or (list_tic[2]=="x" and list_tic[5]=="x" and list_tic[8]=="x") or (list_tic[3]=="x" and list_tic[4]=="x" and list_tic[5]=="x") or (list_tic[2]=="x" and list_tic[4]=="x" and list_tic[6]=="x")or (list_tic[6]=="x" and list_tic[7]=="x" and list_tic[8]=="x"):
        text = "The X Player won"
        
    elif (list_tic[0]=="o" and list_tic[1]=="o" and list_tic[2]=="o") or (list_tic[3]=="o" and list_tic[6]=="o" and list_tic[0]=="o") or (list_tic[0]=="o" and list_tic[4]=="o" and list_tic[8]=="o") or (list_tic[1]=="o" and list_tic[4]=="o" and list_tic[7]=="o") or (list_tic[2]=="o" and list_tic[5]=="o" and list_tic[8]=="o") or (list_tic[3]=="o" and list_tic[4]=="o" and list_tic[5]=="o") or (list_tic[2]=="o" and list_tic[4]=="o" and list_tic[6]=="o")or (list_tic[6]=="o" and list_tic[7]=="o" and list_tic[8]=="o"):
        text = "The O Player won"
        
    else:
        text = "The play is still on."
    return text

if __name__ == "__main__":
    main()

