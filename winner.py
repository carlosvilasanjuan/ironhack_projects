from execution import win_combinations
from execution import player_positions
from execution import cpu_positions

print(cpu_win_combinations) 
def play():
    global result 
    result = 0
    for combination in win_combinations:
        if len (set(combination) - player_positions) == 0:
            result = 1
            return result
        elif len (set(combination) - cpu_positions) == 0:
            result = 2
            return result
        elif len (player_positions) == 5: 
            result = 3
            return result
        else:
            pass