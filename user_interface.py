import random


def new_contestant(contestant):
    contestant.first_name = input("First Name:\n: ")
    contestant.last_name = input("Last Name:\n: ")
    contestant.email_address = input("Email Address:\n: ")
    contestant.registration_number = get_random_number()
    return contestant


def get_random_number():
    return random.randrange(0, 100)


def sweepstakes_name():
    name = input("What is the name of the sweepstakes?\n: ")
    if name != "":
        return name
    else:
        sweepstakes_name()


def prompt():
    print("What would you like to do?\n"
          "1: Create new sweepstake\n"
          "2. Add contestant to existing sweepstake\n"
          "3. Generate a winner for a sweepstake\n"
          "4. Quit\n")