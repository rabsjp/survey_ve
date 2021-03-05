from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'instructions_link': self.session.config['instructions_link'],
        }


class Question(Page):
    form_model = 'player'
    form_fields = ['submitted_answer_1','submitted_answer_2','submitted_answer_3','submitted_answer_4',
                   'submitted_answer_5','submitted_answer_6','submitted_answer_pais_1','submitted_answer_pais_2',
                   'submitted_answer_macho_1','submitted_answer_macho_2','submitted_answer_macho_3',
                   'submitted_answer_macho_4','submitted_answer_macho_5'
                   ]


page_sequence = [
    #Introduction,
    Question,
    #Results
]
