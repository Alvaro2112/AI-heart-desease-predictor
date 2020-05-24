import ReglesSansVariables
from csvtool import csv_to_array
from id3 import ID3
from rules import rules_generator
from id3_cont import ID3_cont

class ResultValues():

    def __init__(self):
        # Do computations here
        train_discrete = csv_to_array('train_bin.csv')
        test_discrete = csv_to_array('test_public_bin.csv')
        id3 = ID3()
        # Task 1
        self.arbre = id3.construit_arbre(train_discrete)
        # Task 3
        self.faits_initiaux = None
        self.regles = rules_generator(self.arbre, [ReglesSansVariables.RegleSansVariables("", set())])
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
