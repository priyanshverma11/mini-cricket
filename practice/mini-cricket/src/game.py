import random

def configure_match():

    overs = int(input("Enter number of overs: "))

    wickets = int(input("Enter number of wickets: "))

    target = int(input("Enter target score: "))

    return overs, wickets, target

def play_ball():

    return random.choice([0, 1, 2, 3, 4, 6])