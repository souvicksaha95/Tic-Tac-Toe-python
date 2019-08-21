def display_board(board=[" "]*9):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def player_input_choice():
    player1_choice=' '
    while 1:
        player1_choice = input("You wanna choose 'x' or 'o', choose one - ")   
        if player1_choice == 'x' or player1_choice == 'o':
            print("You choose {}. Your turn first.".format(player1_choice))
            break
        else:
            print("Wrong Character!")
    return player1_choice

def place_marker(board, marker, position):
    if board[position-1]==" ":
        board[position-1]=marker
    else:
        print("Position already Taken!")
        player_select_pos(board,marker)
    return board

def check_for_win(board):
    return ((board[0]==board[1]==board[2]=='x' or board[0]==board[1]==board[2]=='o') or
            (board[0]==board[3]==board[6]=='x' or board[0]==board[3]==board[6]=='o') or
            (board[0]==board[4]==board[8]=='x' or board[0]==board[4]==board[8]=='o') or
            (board[1]==board[4]==board[7]=='x' or board[1]==board[4]==board[7]=='o') or
            (board[2]==board[5]==board[8]=='x' or board[2]==board[5]==board[8]=='o') or
            (board[2]==board[4]==board[6]=='x' or board[2]==board[4]==board[6]=='o') or
            (board[3]==board[4]==board[5]=='x' or board[3]==board[4]==board[5]=='o') or
            (board[6]==board[7]==board[8]=='x' or board[6]==board[7]==board[8]=='o'))

def player_select_pos(board,marker):
    pos = int(input("Enter desired position(in num 1 to 9) to put {} - ".format(marker)))
    return place_marker(board,marker,pos)

while 1:
    final_board=[' ']*9
    winner=0
    display_board()
    org_player1_choice=player_input_choice()
    if org_player1_choice=='x':
        org_player2_choice='o'
    elif org_player1_choice=='o':
        org_player2_choice='x'
    while 1:
        player_select_pos(final_board,org_player1_choice)
        display_board(final_board)
        if check_for_win(final_board):
            winner = 1
            break
        if ' ' not in final_board:
            break
        player_select_pos(final_board,org_player2_choice)
        if check_for_win(final_board):
            winner = 2
            break
        display_board(final_board)
    if winner!=0:
        print("It's a Win!!")
        display_board(final_board)
        print("Player {} Has Won!".format(winner))
    else:
        print("No match. It's a Draw :(")
    while 1:    
        play_again = str(input("Do you wanna play again? yes or no - "))
        if play_again not in ('yes','no'):
            print("Wrong Input. Select again.")
        else:
            break
    if play_again=='no':
        print("Exiting...")
        break
    else:
        print("\n"*100)
        print("Starting new game...")