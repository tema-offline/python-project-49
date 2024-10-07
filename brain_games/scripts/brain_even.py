from brain_games.cli import welcome_user
from random import randint
import prompt


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game():
    player_name = welcome_user()
    quanity = 0
    print(RULES)
    while quanity < 3:
        question = randint(1, 100)
        if question % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        print(f'Question: {question}')
        player_answer = prompt.string("Your answer: ")
        if player_answer != answer:
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
    even_game()


if __name__ == "__main__":
    main()
