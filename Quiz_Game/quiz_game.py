
# Quiz Game

import random as rd
from termcolor import cprint

quiz = [
    {
        'question': "What is the capital of France?",
        "options": ["Berlin", "Madird", "Paris", "Rome"],
        "answer": {"C": "Paris"}
    },
    {
        'question': "Which planet is know as the red planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": {"B": "Mars"}
    },
    {
        'question': "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": {"D": "Pacific"}
    }
]

score = 0
letters = ['A', 'B', 'C', 'D']

# print(quiz)
rd.shuffle(quiz)
# print(quiz)

for index, item in enumerate(quiz, 1):
    print(f'Question {index}: {item['question']}')
    i = 0
    for option in item["options"]:
        print(f'  {letters[i]}) {option}')
        i += 1

    answer: str = list(item['answer'])[0].upper()
    # print(answer)

    user_answer = input("Your answer: ").upper().strip()
    if user_answer == answer:
        # print('Correct')
        cprint("Correct!", color="green")
        score += 1
    else:
        # print(f'Wrong! The correct answer is {answer.title()}')
        cprint(f'Wrong! The correct answer is {answer.title()}', color='red')

    print('')

print(f'Quiz is over! Your final score is {score} out of {len(quiz)}')
