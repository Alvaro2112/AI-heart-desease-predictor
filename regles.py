import copy


def rules_generator(node, rules):
    if node.terminal():
        for rule in rules:
            rule.conclusion = node.classe()
        new_rules = rules
    else:
        new_rules = []
        for i in node.enfants.items():
            new_rule = copy.deepcopy(rules)
            for rule in new_rule:
                rule.conditions.add("%s = %s " % (node.attribut, i[0]))
                rule.path[node.attribut] = i[0]
            new_rules = new_rules + rules_generator(i[1], new_rule)
    return new_rules
