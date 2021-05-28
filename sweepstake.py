from contestant import Contestant
import random
import user_interface as useri





class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self):
        contestant = useri.new_contestant(Contestant())
        if contestant.registration_number in self.contestants.keys():
            self.register_contestant()
        self.contestants[contestant.registration_number] = contestant

    def pick_winner(self):
        keys = list(self.contestants)
        winner = random.randrange(0, len(keys))
        winner = keys[winner]
        return self.contestants.get(winner)

    def print_contestant_info(self, contestant):
        print(contestant.first_name)
        print(contestant.last_name)
        print(contestant.email_address)
        print(contestant.registration_number)


    def announce_winner(self, winner, contestant):
        for contestant in self.contestants:
            if self.contestants[contestant].registration_number == winner.registration_number:
                self.contestants[contestant].notification("You are the winner!", self.name)
            else:
                self.contestants[contestant].notification(f"Congrats to {winner.first_name} {winner.last_name}.")

