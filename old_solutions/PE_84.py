from utils import timer
from PE_84_Monopoly import Monopoly


@timer
def simulate(n):
    game = Monopoly(4)
    game.simulate(n)
    game.print_state()

    game.print_most_visited()

simulate(5 * 10**6)