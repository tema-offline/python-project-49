import random
import prompt
from operator import add, sub, mul
from brain_games.cli import welcome_user

RULES = 'What is the result of the expression?'
symbols = [("+", add), ("-", sub), ("*", mul)]


def calc_game():
    player_name = welcome_user()
    quanity = 0
    print(RULES)
    while quanity < 3:
        randint_1 = random.randint(1, 100)
        randint_2 = random.randint(1, 100)
        operator, func = random.choice(symbols)
        question = f"{randint_1} {operator} {randint_2}"
        answer = func(randint_1, randint_2)
        print(f'Question: {question}')
        player_answer = prompt.string("Your answer: ")
        if player_answer != str(answer):
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {player_name}!")
            break
        else:
            print('Correct!')
        quanity += 1
    if quanity == 3:
        print(f'Congratulations, {player_name}!')


def main():
    calc_game()


if __name__ == "__main__":
    main()
