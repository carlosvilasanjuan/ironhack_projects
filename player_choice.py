def player_choice():

#set player choice, and player selection as global as the accumulator of player choice
    global player_choice

#input player choice
    print("Set your position as (x,y)")
    player_choice = input()

#check if selection is valid and append position in player choice and remove it from 
    if player_choice in board:
        player_positions.append(player_choice)
        board.remove(player_choice)
        for combination in cpu_win_combinations:
            if player_choice in combination:
               cpu_win_combinations.remove(player_choice)
    else:
        print("Your position is not on board")
        player_choice()

    return(player_position, player_choice, board, cpu_win_combinations)