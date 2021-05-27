class Contestant:
    def __init__(self):
        self.f_name = ""
        self.l_name = ""
        self.email = ""
        self.reg_number = int

    def notification(self, message):
        name = self.f_name + " " + self.l_name
        print(message)