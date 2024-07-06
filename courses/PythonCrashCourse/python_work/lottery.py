from random import randint
from typing import List
from time import sleep

albpabet = "qwertyuiopasdfghjklzxcvbnm"

LUCK_CONFIG = {
    "high": {"digits": 1, "letters": 1},
    "medium": {"digits": 2, "letters": 1},
    "small": {"digits": 3, "letters": 2},
}


class LotteryLuckFactorError(Exception):
    """Wrong Luck Factor"""

    pass


class LuckFactor:
    """Used to set digits and letters count in Generator"""

    def __init__(self, level="high"):
        if level not in LUCK_CONFIG.keys():
            raise LotteryLuckFactorError(
                f"{level} is not a valid luck level. Valid options are {[x for x in LUCK_CONFIG.keys()]}"
            )
        else:
            self.level = level
            self.digits_factor = LUCK_CONFIG[level]["digits"]
            self.letters_factor = LUCK_CONFIG[level]["letters"]


class Generator:
    """Generate random list of digits and letters"""

    def __init__(self, digits, letters) -> None:
        self.digits: int = digits
        self.letters: int = letters
        self.combination: list = []

    def generate(self) -> List:
        def shaker(first_list: list, second_list: list):
            unify = first_list + second_list
            result = list()
            for i in range(len(unify)):
                rand_index = randint(0, len(unify) - 1)
                result.append(unify[rand_index])
                del unify[rand_index]
            return result

        def gen_letters(letters) -> List:
            result = list()
            for x in range(letters):
                result.append(
                    albpabet[randint(0, len(albpabet) - 1)]
                    + albpabet[randint(0, len(albpabet) - 1)]
                )
            return result

        self.combination = shaker(
            [randint(10, 99) for x in range(self.digits)], gen_letters(self.letters)
        )
        return self.combination


class Ticket:
    """Store combination from Generator"""

    def __init__(self, combination: Generator, id: int) -> None:
        self.combination = combination.generate()
        self.id = id

    def show(self) -> None:
        print(f"Your ticket is: {self.combination}")


class Lottery:
    """Main class of the Game
    On init will issue a winning ticket
    and compare those with all next issued tickets.
    If those match - game over - we have a winner.
    But if tickets count will be bigger that circulation
    before winner appears - game over - run out of tickets.
    """

    def __init__(self, luck: str) -> None:
        self.luck = LuckFactor(luck)
        self.generator = Generator(
            digits=self.luck.digits_factor, letters=self.luck.letters_factor
        )
        self.tickets_issued: int = 0
        self.circulation = 1_000_000
        self.winning_ticket = self.issue_ticket()
        self.game_over: bool = False
        self.have_a_winner: bool = False

    def start(self) -> None:
        print(f"Welcome on a game! Your luck factor is {self.luck.level}")
        print(f"and the winning combination is... {self.winning_ticket.combination}!")
        print(f"Good Luck!")

    def issue_ticket(self) -> Ticket:
        self.tickets_issued += 1
        if self.tickets_issued >= self.circulation:
            self.game_over = True
        return Ticket(self.generator, self.tickets_issued)

    def check_ticket(self, ticket: Ticket) -> bool:
        print(f"checking you ticket[{ticket.id}]: {ticket.combination}")
        if ticket.combination == self.winning_ticket.combination:
            self.have_a_winner = True
            self.check_game_over()
            return True
        else:
            self.check_game_over()
            print("Sorry, maybe next time...")
            return False

    def check_game_over(self):
        if self.game_over:
            print(f"GAME OVER! Max number of tickets has been reached")
            exit(0)
        elif self.have_a_winner:
            print(f"We have a WINNER! Congratulations")


class LottetyBruteForce:
    """Will get Lottery object
    and will generate tickets till winning
    or run out of tickets
    """

    def __init__(self, lottery: Lottery) -> None:
        self.lottery: Lottery = lottery
        print(
            f"lotery_hack: will try to hack: {self.lottery.winning_ticket.combination}"
        )
        self.hacked: bool = False

    def generate_new_ticket(self) -> Ticket:
        return self.lottery.issue_ticket()

    def start(self) -> None:
        iterations: int = 0
        while not self.hacked:
            ticket: Ticket = self.generate_new_ticket()
            if self.lottery.check_ticket(ticket):
                print("Hey, look - I win!")
                print(
                    f"ticket[{ticket.id}]:{ticket.combination} is the same as lottery[{self.lottery.winning_ticket.id}]:{self.lottery.winning_ticket.combination}"
                )
                print(f"took {iterations} iterations")
                self.hacked = True
            else:
                print(f"hack in progress {iterations}")
                iterations += 1
                # sleep(1)


lottery: Lottery = Lottery("high")
lottery.start()

ticket: Ticket = lottery.issue_ticket()
lottery.check_ticket(ticket)

hack: LottetyBruteForce = LottetyBruteForce(lottery)
sleep(3)
hack.start()
