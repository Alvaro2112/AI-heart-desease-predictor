import task4 as tk4


def explain_and_cure(people, tree, healthy_rules, max_changes=2):
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
            else:
                print("We can not cure someone with attributes  :", d, " by changing at most", max_changes, "attributes")
        else:
            d.pop('target')
            print("Someone with attributes :",d,"is healthy")

    return num_cure , tot_sick_ppl

def explain_and_cure_no_print(people, tree, healthy_rules, max_changes=2):
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
        else:
            d.pop('target')

    return num_cure , tot_sick_ppl