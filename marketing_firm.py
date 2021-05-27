from sweepstake import Sweepstake


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self, name):
        created_sweepstakes = Sweepstake(name)
        self.manager.insert_sweepstakes(created_sweepstakes)
