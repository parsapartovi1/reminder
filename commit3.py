import random


players_name = ["ali", "hamid", "alireza", "nima"]

random.shuffle(players_name)

team1 = players_name[:2]
team2 = players_name[2:]

print("Team 1:", team1)
print("Team 2:", team2)




