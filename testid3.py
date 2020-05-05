from noeud_de_decision import NoeudDeDecision
from id3 import ID3
from csvtool import csv_to_array

def test( train,test):
    train = csv_to_array(train)
    test = csv_to_array(test)

    id3 = ID3()
    arbre = id3.construit_arbre(train)

    num_test = len(test)

    for row in test :
        





    