board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

cpu_win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

player_positions = set()

cpu_positions = set()

import player_selection
import cpu_selection
import winner

def execution():
    play()
    while result == False:



        print('''
                                            THE BOARD
                                             0, 1, 2,
                                             3, 4, 5,
                                             6, 7, 8''')
        print("")
        
        
       #             Step1: player selection 

        
        print('''                                        PLACEMENT OPTIONS
                                  ''' ,board)
        player_selection()
        play()
        
        player_positions.add(player_ch)
        print("YOUR POSITIONS:", player_positions)
        print("")
        board.remove(player_ch)
    
    
        #             Step2: CPU  
        for combination in cpu_win_combinations:
            for num in combination:
                if player_ch == num:
                    cpu_win_combinations.remove(combination)
            
        cpu_selection()
        play()
        print("                                                                                   ",cpu_choice,"CPU CHOICE")
        cpu_positions.add(cpu_choice)
        print("                                                                                   ",cpu_positions,"CPU POSITIONS")
        print("")
        board.remove(cpu_choice)
    
        for ele in cpu_win_combinations:
            if cpu_choice in ele:
                ele.remove(cpu_choice)
        cpu_positions.add(cpu_choice)

    

    else:
        print("                            GAME IS OVER")
        if result == 1:
            print ("---------------------------WINNER------------------------")
        if result == 2:
            print ("---------------------------LOSER-------------------------")
        if result == 3:
            print ("----------------------------TIE--------------------------")

        
 execution()

