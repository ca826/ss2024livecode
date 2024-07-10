
from otree.api import *


doc = """
A Simple tullock contest
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'contest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT = 20
    COST_PER_TICKET = 1


class Subsession(BaseSubsession):
    is_paid = models.BooleanField()

    def setup(self):
        self.is_paid = (self.round_number == 1)
        for group in self.get_groups():
            group.setup()

class Group(BaseGroup):
    def setup(self):
        for player in self.get_players():
            player.setup()


class Player(BasePlayer):
    endowment = models.IntegerField()
    cost_per_ticket = models.IntegerField()
    tickets_purchased = models.IntegerField()
    is_winner = models.BooleanField()
    is_paid = models.BooleanField()
    earnings = models.IntegerField()

    def setup(self):
        self.endowment = C.ENDOWMENT
        self.cost_per_ticket = C.COST_PER_TICKET
def creating_session(subsession):
    subsession.setup()

# PAGES
class Intro(Page):
    pass


class SetupRound(WaitPage):
    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.setup()

class Decision(Page):
    form_model = "player"

    @staticmethod
    def get_form_fields(player):
    return["tickets_purchased"]


class WaitForDecisions(WaitPage):
    pass

class Results(Page):
    pass

class EndBlock(Page):
    pass

page_sequence = [Intro,
                 SetupRound,
                 Decision,
                 WaitForDecisions,
                 Results,
                 EndBlock,
]