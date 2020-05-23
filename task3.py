import Task4 as tk4

def explain_and_cure(people,rules,tree):
    
    healthy_rules = []
    for r in rules:
        if r.conclusion == '0':
            healthy_rules.append(r.path)
    num_cure =0

    for p in people:
        d = dict()
        d = tree.find_path(p[1], d)
        if d['target'] =='1':
            d.pop('target')
            n,how =tk4.cure(d, healthy_rules)
            if n <=2:
                num_cure +=1
                print("We can cure someone with attributes  :",d, " by changing ",how)

    return num_cure

