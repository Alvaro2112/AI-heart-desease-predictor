import csv
from noeud_de_decision import NoeudDeDecision
from id3 import ID3


def csv_to_array(name):
    ret = list()
    with open(name) as csv_file:
        line_count =0
        att_name =[]
        csv_reader =  csv.reader(csv_file,  delimiter=',')
        for row in csv_reader:
            if line_count ==0:
                for column in row :
                    if column == '\ufeffage' :
                        column = 'age'
                    att_name.append(column)
            else :
                d = dict()
                i =0
                for col in row:
                    d.update({att_name[i] : col })
                    i +=1
                a =[d['target']]
                del d['target']
                a.append(d)
                ret.append(a) 
            line_count +=1
    return ret

d = csv_to_dict('train_bin.csv')
print(d)
id3 = ID3()
arbre = id3.construit_arbre(d)
print('Arbre de décision :')
print(arbre)
e = csv_to_dict("test_public_bin.csv")

print(arbre.classifie(e[1][1]))