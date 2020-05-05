from  csvtool import csv_to_array
from noeud_de_decision import NoeudDeDecision
from id3 import ID3

class ResultValues():

    def __init__(self):
        
        # Do computations here
        
        # Task 1
        self.arbre = None
        # Task 3
        self.faits_initiaux = None
        self.regles = None
        # Task 5
        self.arbre_advance = None

    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]


if __name__ == "__main__":
   d = csv_to_array('train_bin.csv')
   id3 = ID3()
   arbre = id3.construit_arbre(d)
