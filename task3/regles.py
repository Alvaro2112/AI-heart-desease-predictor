import copy

  

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


    # r = Regle({'a': 0, 'b': 0}, 0)
    # set = [[0, {'a': 0, 'b': 0}], [0, {'a': 0, 'b': 1}]]
    # print(r)
    # ->{'a': 0, 'b': 0} => 0
    # print(self.simplifie_regle(r, set))
    # ->{'a': 0} => 0
