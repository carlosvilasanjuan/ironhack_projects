{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Globals\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "True\n",
      "[(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "the board is defined as a list of the available cells\n",
    " each represented by a tuple (x,y), with x representing the line \n",
    " number and y the columns number\n",
    "'''\n",
    "board = [0, 1, 2, 3, 4, 5, 6, 7, 8]\n",
    "print (type(board[1]))\n",
    "print(1 in board)\n",
    "'''\n",
    "win combinations are defined as sets ==> so that the order \n",
    "in witch positions are occupied \n",
    "by each player does'ent determines who wins\n",
    "'''\n",
    "win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]\n",
    "print(win_combinations)\n",
    "\n",
    "cpu_win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]\n",
    "global player_selection\n",
    "\n",
    "\n",
    "# set player selection \n",
    "player_positions = set()\n",
    "cpu_positions = set()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Def_Player_Selection"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_selection():\n",
    "\n",
    "#set player choice, and player selection as global as the accumulator of player choice\n",
    "    global player_ch\n",
    "    global player_positions\n",
    "\n",
    "#input player choice\n",
    "    player_ch = int(input())\n",
    "\n",
    "#check if selection is valid and append position in player choice and remove it from \n",
    "    if player_ch in board:\n",
    "        \n",
    "        #player wins\n",
    "        return player_positions, player_ch, board\n",
    "    \n",
    "    else:\n",
    "        print(\"Your position is not on board\")\n",
    "        player_selection()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Def_CPU_Selection\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "def cpu_selection():\n",
    "    global cpu_choice\n",
    "    \n",
    "    # if if combinations [0] and [1] have the same number if tuples, cpu choice = most repited tupple in win combinations between [0],[1] and [1][1]  \n",
    "    \n",
    "    cpu_choice = cpu_win_combinations[0][0]\n",
    "                \n",
    "            \n",
    "    return cpu_choice\n",
    "                  \n",
    "            \n",
    "cpu_selection()           \n",
    "            "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Def Winner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]\n"
     ]
    }
   ],
   "source": [
    "print(cpu_win_combinations) \n",
    "def play():\n",
    "    global result \n",
    "    result = 0\n",
    "    for combination in win_combinations:\n",
    "        if len (set(combination) - player_positions) == 0:\n",
    "            result = 1\n",
    "            return result\n",
    "        elif len (set(combination) - cpu_positions) == 0:\n",
    "            result = 2\n",
    "            return result\n",
    "        elif len (player_positions) == 5: \n",
    "            result = 3\n",
    "            return result\n",
    "        else:\n",
    "            pass\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Execution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "                                            THE BOARD\n",
      "                                             0, 1, 2,\n",
      "                                             3, 4, 5,\n",
      "                                             6, 7, 8\n",
      "\n",
      "                                        PLACEMENT OPTIONS\n",
      "                                   [0, 1, 2, 3, 4, 5, 6, 7, 8]\n",
      "1\n",
      "YOUR POSITIONS: {1}\n",
      "\n",
      "                                                                                    3 CPU CHOICE\n",
      "                                                                                    {3} CPU POSITIONS\n",
      "\n",
      "\n",
      "                                            THE BOARD\n",
      "                                             0, 1, 2,\n",
      "                                             3, 4, 5,\n",
      "                                             6, 7, 8\n",
      "\n",
      "                                        PLACEMENT OPTIONS\n",
      "                                   [0, 2, 4, 5, 6, 7, 8]\n",
      "2\n",
      "YOUR POSITIONS: {1, 2}\n",
      "\n",
      "                                                                                    4 CPU CHOICE\n",
      "                                                                                    {3, 4} CPU POSITIONS\n",
      "\n",
      "\n",
      "                                            THE BOARD\n",
      "                                             0, 1, 2,\n",
      "                                             3, 4, 5,\n",
      "                                             6, 7, 8\n",
      "\n",
      "                                        PLACEMENT OPTIONS\n",
      "                                   [0, 5, 6, 7, 8]\n",
      "3\n",
      "Your position is not on board\n",
      "4\n",
      "Your position is not on board\n",
      "5\n",
      "YOUR POSITIONS: {1, 2, 5}\n",
      "\n",
      "                                                                                    6 CPU CHOICE\n",
      "                                                                                    {3, 4, 6} CPU POSITIONS\n",
      "\n",
      "\n",
      "                                            THE BOARD\n",
      "                                             0, 1, 2,\n",
      "                                             3, 4, 5,\n",
      "                                             6, 7, 8\n",
      "\n",
      "                                        PLACEMENT OPTIONS\n",
      "                                   [0, 7, 8]\n",
      "5\n",
      "Your position is not on board\n",
      "6\n",
      "Your position is not on board\n",
      "0\n",
      "YOUR POSITIONS: {0, 1, 2, 5}\n",
      "\n",
      "                                                                                    7 CPU CHOICE\n",
      "                                                                                    {3, 4, 6, 7} CPU POSITIONS\n",
      "\n",
      "                            GAME IS OVER\n",
      "---------------------------WINNER------------------------\n"
     ]
    }
   ],
   "source": [
    "board = [0, 1, 2,\n",
    "         3, 4, 5,\n",
    "         6, 7, 8]\n",
    "\n",
    "win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]\n",
    "\n",
    "cpu_win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]\n",
    "\n",
    "player_positions = set()\n",
    "\n",
    "cpu_positions = set()\n",
    "\n",
    "\n",
    "\n",
    "def execution():\n",
    "    play()\n",
    "    while result == False:\n",
    "\n",
    "\n",
    "\n",
    "        print('''\n",
    "                                            THE BOARD\n",
    "                                             0, 1, 2,\n",
    "                                             3, 4, 5,\n",
    "                                             6, 7, 8''')\n",
    "        print(\"\")\n",
    "        \n",
    "        \n",
    "       #             Step1: player selection \n",
    "\n",
    "        \n",
    "        print('''                                        PLACEMENT OPTIONS\n",
    "                                  ''' ,board)\n",
    "        player_selection()\n",
    "        play()\n",
    "        \n",
    "        player_positions.add(player_ch)\n",
    "        print(\"YOUR POSITIONS:\", player_positions)\n",
    "        print(\"\")\n",
    "        board.remove(player_ch)\n",
    "    \n",
    "    \n",
    "        #             Step2: CPU  \n",
    "        for combination in cpu_win_combinations:\n",
    "            for num in combination:\n",
    "                if player_ch == num:\n",
    "                    cpu_win_combinations.remove(combination)\n",
    "            \n",
    "        cpu_selection()\n",
    "        play()\n",
    "        print(\"                                                                                   \",cpu_choice,\"CPU CHOICE\")\n",
    "        cpu_positions.add(cpu_choice)\n",
    "        print(\"                                                                                   \",cpu_positions,\"CPU POSITIONS\")\n",
    "        print(\"\")\n",
    "        board.remove(cpu_choice)\n",
    "    \n",
    "        for ele in cpu_win_combinations:\n",
    "            if cpu_choice in ele:\n",
    "                ele.remove(cpu_choice)\n",
    "        cpu_positions.add(cpu_choice)\n",
    "\n",
    "    \n",
    "\n",
    "    else:\n",
    "        print(\"                            GAME IS OVER\")\n",
    "        if result == 1:\n",
    "            print (\"---------------------------WINNER------------------------\")\n",
    "        if result == 2:\n",
    "            print (\"---------------------------LOSER-------------------------\")\n",
    "        if result == 3:\n",
    "            print (\"----------------------------TIE--------------------------\")\n",
    "\n",
    "        \n",
    "execution()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-6-aa67d8ecd150>, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-6-aa67d8ecd150>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    for combination in cpu_win_combinations:\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "# Step2 sorting CPU options \n",
    "    for combination in cpu_win_combinations:\n",
    "        cpu_win_combinations.sort(key = len(combination))    \n",
    "    for combination in cpu_win_combinations:        \n",
    "            for num in combination:\n",
    "                combination= sorted(combination, key = cpu_win_combinations.count(num)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " if len(cpu_win_combinations[0]) == len(cpu_win_combinations[1]):\n",
    "        cpu_choice = max(cpu_win_combinations[0][1],cpu_win_combinations[1][1],key=cpu_win_combinations.count(num))\n",
    "                            \n",
    "    else:\n",
    "        cpu_choice = cpu_win_combinations[0][1]\n",
    "        cpu_choice = max(cpu_win_combinations[0][1],cpu_win_combinations[1][1],key=cpu_win_combinations.count(num))\n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " # if if combinations [0] and [1] have the same number if tuples, cpu choice = most repited tupple in win combinations between [0],[1] and [1][1]  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for combination in cpu_win_combinations:        \n",
    "        cpu_win_combinations.sort(key = len(list(combination))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import defaultdict\n",
    "\n",
    "cpu_win_combinations = [[0, 1, 2], [3, 4], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]\n",
    "\n",
    "cpu_win_len = len(cpu_win_combinations)\n",
    "\n",
    "d = defaultdict(*cpu_win_combinations)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
