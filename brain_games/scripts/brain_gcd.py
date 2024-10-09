import random
import prompt
from brain_games.cli import welcome_user

RULES = 'Find the greatest common divisor of given numbers.'


def gcd_game():
    player_name = welcome_user()
    quanity = 0
    print(RULES)
    while quanity < 3:
        randint_1 = random.randint(1, 100)
        randint_2 = random.randint(1, 100)
        randint_3 = min(randint_1, randint_2)
        question = f"{randint_1} {randint_2}"
        answer = 0
        for i in range(1, randint_3 + 1):
            if randint_1 % i == 0 and randint_2 % i == 0:
                answer = i
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
    gcd_game()


if __name__ == "__main__":
    main()
