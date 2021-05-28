from sweepstake_stack_manager import SweepstakesStackManager
from sweepstake_queue_manager import SweepstakesQueueManager


def manager_type():
    print("Which type of sweepstakes manager do you want to use?\n"
          "1: Queue\n2: Stack")
    try:
        choice = int(input(" "))
        assert choice == 1 or choice == 2
        if choice == 1:
            return SweepstakesQueueManager()
        else:
            return SweepstakesStackManager()
    except:
        print("Not a valid option")
        choice = manager_type()
        return choice
