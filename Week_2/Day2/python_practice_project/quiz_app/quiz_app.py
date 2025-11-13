# Store questions and answers in a dictionary or JSON file.
# Ask user questions one by one.
# Keep score and show the result at the end.

import json

score = 0

#score
def keep_score(score):
    score += 20
    return score

# read json
with open('q_and_a.json', 'r') as f:
    data = json.load(f)

# display question
def display_question(data):
    score = 0
    for _ in data:
        print(f"Question: {_['question']}")
        for key,value in _['choices'].items():
            print(f"{key}) {value}")

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if(answer == _['correct']):
            print("Correct!")
            score = keep_score(score)
        else:
            print(f"Incorrect! The answer is {_['correct']}")

        print("")

    print(f"Final score: {score}")


display_question(data)