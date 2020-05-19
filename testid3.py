from task12.noeud_de_decision import NoeudDeDecision
from task12.id3 import ID3
from task3.regles import genere_regles_rec
from csvtool import csv_to_array
from task3.reglesansvariables import RegleSansVariables

def test( train,test):

    train = csv_to_array(train)
    test = csv_to_array(test)

    id3 = ID3()
    arbre = id3.construit_arbre(train)
    reg = genere_regles_rec(arbre,[RegleSansVariables("",set())])           
    for r in reg:
        print(r)

if __name__ == "__main__":
    test("train_bin.csv", "test_public_bin.csv")
            











    