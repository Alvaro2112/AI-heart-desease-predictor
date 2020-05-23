from task12.noeud_de_decision import NoeudDeDecision
from task12.id3 import ID3
from regles import rules_generator, explain
from csvtool import csv_to_array
from reglesansvariables import RegleSansVariables
from task4 import cure

def test( train,test):
    train = csv_to_array(train)
    test = csv_to_array(test)

    id3 = ID3()
    arbre = id3.construit_arbre(train)
    
    reg = (rules_generator(arbre, [RegleSansVariables("", set())]))

    healthy_rules = []
    for r in reg:
        if r.conclusion == '0':
            healthy_rules.append(r.path)





if __name__ == "__main__":
    test("train_bin.csv", "test_public_bin.csv")
            











    