from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv, json

author = 'Your name here'

doc = """
A quiz app that reads its questions from a spreadsheet
(see quiz.csv in this directory).
There is 1 question per page; the number of pages in the game
is determined by the number of questions in the CSV.
See the comment below about how to randomize the order of pages.
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None


    with open('survey_ve/countries.json') as f:
        countries = json.load(f)

    num_rounds = 1

def parse_config(config_file):
    with open('survey_ve/configs/' + config_file) as questions_file:
        questions = list(csv.DictReader(questions_file))
        return questions


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            #self.session.vars['questions'] = Constants.questions.copy()
            self.session.vars['questions'] = parse_config(self.session.config['config_file']).copy()
            self.session.vars['countries'] = Constants.countries.copy()
            for p in self.get_players():
                p.question_1 = self.session.vars['questions'][0]['question']
                p.question_2 = self.session.vars['questions'][1]['question']
                p.question_3 = self.session.vars['questions'][2]['question']
                p.question_4 = self.session.vars['questions'][3]['question']
                p.question_5 = self.session.vars['questions'][4]['question']
                p.question_6 = self.session.vars['questions'][5]['question']
                p.question_pais_1 = self.session.vars['questions'][6]['question']
                p.question_pais_2 = self.session.vars['questions'][7]['question']
                p.macho_1 = self.session.vars['questions'][8]['question']
                p.macho_2 = self.session.vars['questions'][9]['question']
                p.macho_3 = self.session.vars['questions'][10]['question']
                p.macho_4 = self.session.vars['questions'][11]['question']
                p.macho_5 = self.session.vars['questions'][12]['question']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question_1 = models.StringField()
    question_2 = models.StringField()
    question_3 = models.StringField()
    question_4 = models.StringField()
    question_5 = models.StringField()
    question_6 = models.StringField()
    question_pais_1 = models.StringField()
    question_pais_2 = models.StringField()
    macho_1 = models.StringField()
    macho_2 = models.StringField()
    macho_3 = models.StringField()
    macho_4 = models.StringField()
    macho_5 = models.StringField()

    submitted_answer_1 = models.StringField()
    submitted_answer_2 = models.StringField()
    submitted_answer_3 = models.StringField()
    submitted_answer_4 = models.StringField()
    submitted_answer_5 = models.StringField()
    submitted_answer_6 = models.StringField()
    submitted_answer_pais_1 = models.StringField()
    submitted_answer_pais_2 = models.StringField()

    submitted_answer_macho_1 = models.StringField()
    submitted_answer_macho_2 = models.StringField()
    submitted_answer_macho_3 = models.StringField()
    submitted_answer_macho_4 = models.StringField()
    submitted_answer_macho_5 = models.StringField()

    def submitted_answer_1_choices(self):
        qd = self.session.vars['questions'][0]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
        ]

    def submitted_answer_2_choices(self):
        qd = self.session.vars['questions'][1]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
        ]

    def submitted_answer_3_choices(self):
        qd = self.session.vars['questions'][2]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
        ]

    def submitted_answer_4_choices(self):
        qd = self.session.vars['questions'][3]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
        ]

    def submitted_answer_5_choices(self):
        qd = self.session.vars['questions'][4]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
        ]

    def submitted_answer_6_choices(self):
        qd = self.session.vars['questions'][5]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
            qd['choice6'],
            qd['choice7'],
            qd['choice8'],
            qd['choice9'],
        ]

    def submitted_answer_pais_1_choices(self):
        qd = self.session.vars['questions'][6]

        return self.session.vars['countries']

    def submitted_answer_pais_2_choices(self):
        qd = self.session.vars['questions'][7]

        return self.session.vars['countries']

    def submitted_answer_macho_1_choices(self):
        qd = self.session.vars['questions'][8]

        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
            qd['choice6'],
            qd['choice7'],
            qd['choice8'],
            qd['choice9'],
        ]

    def submitted_answer_macho_2_choices(self):

        qd = self.session.vars['questions'][9]

        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
            qd['choice6'],
            qd['choice7'],
            qd['choice8'],
            qd['choice9'],
        ]

    def submitted_answer_macho_3_choices(self):
        qd = self.session.vars['questions'][10]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
            qd['choice6'],
            qd['choice7'],
            qd['choice8'],
            qd['choice9'],
        ]

    def submitted_answer_macho_4_choices(self):
        qd = self.session.vars['questions'][11]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
            qd['choice6'],
            qd['choice7'],
            qd['choice8'],
            qd['choice9'],
        ]

    def submitted_answer_macho_5_choices(self):
        qd = self.session.vars['questions'][12]
        return [
            qd['choice1'],
            qd['choice2'],
            qd['choice3'],
            qd['choice4'],
            qd['choice5'],
            qd['choice6'],
            qd['choice7'],
            qd['choice8'],
            qd['choice9'],
        ]
