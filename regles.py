import copy
from task4 import cure
from reglesansvariables import RegleSansVariables

  

def genere_regles_rec(node, rules):
    if node.terminal():
        for rule in rules:
            rule.conclusion = node.classe()
        new_rules= rules
    else:
        new_rules = []
        for i in node.enfants.items():
            new_rule = copy.deepcopy(rules)
            for rule in new_rule:
                rule.conditions.add("%s = %s " % (node.attribut, i[0]))
            new_rules = new_rules + genere_regles_rec(i[1], new_rule)
    return new_rules


def explain(example, arbre,healthy_rules):
    path = arbre.find_path(example)
    cond =set()
    conc =""
    for i in path.items():
        if(i[0] != 'target'):
            cond.add("%s = %s " % (i[0], i[1]))
        else :
            conc = i[1]

    r = RegleSansVariables(cond,conc)
    print(r)
    num_changes =0
    
    if path['target'] == '1':     ### if sick then show the treatment
        treat,num_changes = cure(healthy_rules, path.pop['target'])
        print(treat)

    return  num_changes
    # r = Regle({'a': 0, 'b': 0}, 0)
    # set = [[0, {'a': 0, 'b': 0}], [0, {'a': 0, 'b': 1}]]
    # print(r)
    # ->{'a': 0, 'b': 0} => 0
    # print(self.simplifie_regle(r, set))
    # ->{'a': 0} => 0
