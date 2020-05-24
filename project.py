from regles import rules_generator
import reglesansvariables
from csvtool import csv_to_array
from id3 import ID3
from id3_cont import ID3_cont
import task3 as tk3


class ResultValues():

    def __init__(self):
        # Do computations here
        self.train_discrete = csv_to_array('train_bin.csv')
        test_discrete = csv_to_array('test_public_bin.csv')
        id3 = ID3()
        # Task 1
        self.arbre = id3.construit_arbre(self.train_discrete)
        # Task 3
        self.faits_initiaux = test_discrete[0]
        self.regles = rules_generator(self.arbre, [reglesansvariables.RegleSansVariables("", set())])
        tk3.explain_and_cure([self.faits_initiaux], self.arbre, self.healthy_rules())
        # Task 5
        train_continuous = csv_to_array('train_continuous.csv')
        id3_cont = ID3_cont()
        self.arbre_advance = id3_cont.construit_arbre(train_continuous)

    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]

    def healthy_rules(self):
        healthy_rules = []
        for r in self.regles:
            if r.conclusion == '0':
                healthy_rules.append(r.path)
        return healthy_rules

    def save_count(self, max_changes, ppl):
        return tk3.explain_and_cure(ppl, self.arbre, self.healthy_rules(), max_changes)

if _name_ == '_main_':
    ee = ResultValues()
    print(ee.save_count(2,ee.train_discrete))