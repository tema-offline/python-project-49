from brain_games.cli import welcome_user
from random import randint
import prompt
import math


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    mx = math.sqrt(num)

    i = 2
    while i <= mx:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def prime_game():
    player_name = welcome_user()
    quanity = 0
    print(RULES)
    while quanity < 3:
        question = randint(1, 100)
        answer = 'yes' if is_prime(question) else 'no'
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
    prime_game()


if __name__ == "__main__":
    main()
