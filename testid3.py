from task12.noeud_de_decision import NoeudDeDecision
from task12.id3 import ID3
from id3_cont import ID3_cont
from regles import rules_generator
from csvtool import csv_to_array
from reglesansvariables import RegleSansVariables
from task4 import cure

def test( train,test):
    train = csv_to_array(train)
    test = csv_to_array(test)

    id3 = ID3_cont()
    arbre = id3.construit_arbre(train)
    p =0
    t =0
    for te in test:
        if te[0]==arbre.classifie(te[1]):
            p+=1
        t+=1

    print(p/t)

if __name__ == "__main__":
    test("train_continuous.csv", "test_public_continuous.csv")
            











    