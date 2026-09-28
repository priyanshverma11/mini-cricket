import random
 
def configure_match():

    overs = int(input("Enter number of overs: "))

    wickets = int(input("Enter number of wickets: "))

    target = int(input("Enter target score: "))

    return overs, wickets, target

def play_ball():

    return random.choice([0, 1, 2, 3, 4, 6])

def update_score(current_score, runs):

    return current_score + runs

def increment_ball(ball_number):

    return ball_number + 1
