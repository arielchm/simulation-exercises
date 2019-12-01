import random
import time
import os
from colorama import Fore, Back, init


def clear_screen():
    clearCommand = os.name
    if os.name == "postfix":
        clearCommand = "clear"
    if os.name == "nt":
        clearCommand = "cls"
    os.system(clearCommand)


def init_labyrinth(n, p):
    matrix = []
    for i in range(n):
        var = []
        for j in range(n):
            a = random.random()
            if a < p/100:
                var.append(10)
            else:
                var.append(0)
        matrix.append(var)
    return matrix


def draw_labyrinth(labyrinth):
    n = len(labyrinth)
    for i in range(n):
        row = ""
        for j in range(n):
            if(labyrinth[i][j] == 0):
                row += "   "
            elif labyrinth[i][j] == 10:
                row += " ■ "
            elif labyrinth[i][j] == 1:
                row += Back.RED+Fore.WHITE+" 1 "+Back.BLACK
            elif labyrinth[i][j] == 2:
                row += Back.GREEN+Fore.WHITE+" 2 "+Back.BLACK
            elif labyrinth[i][j] == 3:
                row += Back.MAGENTA+Fore.WHITE+" 3 "+Back.BLACK
            elif labyrinth[i][j] == 4:
                row += Back.BLUE+Fore.WHITE+" 4 "+Back.BLACK
        print(row)


def transition(labyrinth, probability_matrix):
    n = len(labyrinth)
    moves = [0, 0, 0, 0]
    for i in range(n):
        for j in range(n):
            element = labyrinth[i][j]
            if element in [1, 2, 3, 4] and moves[element-1] == 0:
                #direction = get_direction(probability_matrix[element-1])
                value = random.choices(
                    population=["left", "right", "forward"], weights=[20, 20, 50], k=1)
                direction = value[0]
                # print(direction)
                directions = ["left", "right", "forward"]
                if i == 0 or labyrinth[i-1][j] != 0:
                    directions.remove("left")
                if i == n-1 or labyrinth[i+1][j] != 0:
                    directions.remove("right")
                if j == n-1 or labyrinth[i][j+1] != 0:
                    directions.remove("forward")
                # if j == n-1:

                if direction in directions:
                    if direction == "left":
                        labyrinth[i-1][j] = labyrinth[i][j]
                    if direction == "right":
                        labyrinth[i+1][j] = labyrinth[i][j]
                    if direction == "forward":
                        labyrinth[i][j+1] = labyrinth[i][j]

                    moves[labyrinth[i][j]-1] = 1
                    labyrinth[i][j] = 0

    return labyrinth


def init_positions(labyrinth):
    vector = [i for i in range(len(labyrinth)) if labyrinth[i][0] is not 10]
    players = 4
    while len(vector) < players:
        players -= 1

    for i in range(players):
        item = random.choice(vector)
        vector.remove(item)
        labyrinth[item][0] = i + 1
    return labyrinth


def define_movement_probabilites(players):
    probability_matrix = []
    for i in range(len(players)):
        u = random.random()
        d = random.random()
        r = random.random()
        # probability_matrix.append([u,d,r])
        probability_matrix.append([20, 20, 50])
    return probability_matrix


def verify_players(labyrinth):
    players = []
    for i in range(len(labyrinth)):
        if(labyrinth[i][0] in [1, 2, 3, 4]):
            players.append(i)
    return players


def get_direction(probabilites):
    value = random.choices(
        population=["left", "right", "forward"], weights=probabilites, k=1)
    direction = value[0]
    return direction


def verify_winner(labyrinth):
    winners = []
    players = [1, 2, 3, 4]
    for i in range(len(labyrinth)):
        piece = labyrinth[i][len(labyrinth)-1]
        if piece in players:
            winners.append(piece)
    return winners


def main():
    clear_screen()
    labyrinth = init_labyrinth(15, 15)
    labyrinth = init_positions(labyrinth)
    # print(labyrinth)
    players = verify_players(labyrinth)
    draw_labyrinth(labyrinth)
    # '''
    if len(players) > 0:
        probability_matrix = define_movement_probabilites(players)
        winners = []
        while not winners:
            time.sleep(0.1)
            clear_screen()
            labyrinth = transition(labyrinth, probability_matrix)
            draw_labyrinth(labyrinth)
            winners = verify_winner(labyrinth)

        if len(winners) > 1:
            message = "Tie between players " + \
                " and ".join([str(i) for i in winners])

            print(message)
        else:
            print("Player "+str(winners[0])+" won")
    else:
        print("Not enough space for the players")
    # '''


if __name__ == "__main__":
    main()
