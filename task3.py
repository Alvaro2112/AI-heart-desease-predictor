import task4 as tk4


def explain_and_cure(people, tree, healthy_rules, max_changes = 2):
    num_cure = 0
    tot_sick_ppl = 0

    for p in people:
        d = dict()
        d = tree.find_path(p[1], d)
        if d['target'] == '1':
            tot_sick_ppl += 1
            d.pop('target')
            how, n = tk4.cure(d, healthy_rules)
            if n <= max_changes:
                num_cure += 1
                print("We can cure someone with attributes  :", d, " by changing ", how)

    if tot_sick_ppl == 0:
        return None
    return num_cure / tot_sick_ppl