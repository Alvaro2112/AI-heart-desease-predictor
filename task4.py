from task12.noeud_de_decision import NoeudDeDecision
import copy


def cure(health_attr, sick_attr) :

    new_sick_attr= copy.deepcopy(sick_attr)

    new_sick_attr.pop("age") ### dont care about this attributes
    new_sick_attr.pop("sex")
    delta_min = len(sick_attr)  ####length of the treatment
    delta_curr = delta_min

    min_change = dict()

    for i in health_attr :
        changes = dict()
        for j in list(i.keys()):
            value_sain = i.get(j)
            value_malade = health_attr.get(j)
            if value_sain != value_malade:
                    changes[j] = value_sain
                    delta_curr = len(changes)
        if delta_curr < delta_min:
            delta_min = delta_curr
            min_change = copy.deepcopy(changes)
                        
        
    return min_change,delta_min
