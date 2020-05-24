import copy


def cure(sick_attr, health_attr):
    min_changes = dict()
    delta_curr = len(sick_attr)
    delta_min = len(sick_attr)

    # Loop through list attributes that lead to a healthy outcome
    for i in health_attr:
        changes = dict()

        # Loops through attributes in chosen list
        for j in list(i.keys()):
            if j == 'age' or j == 'sex':
                continue
            value_sain = i.get(j)
            value_malade = sick_attr.get(j)

            # Checks if current argument is different from target rules
            if (value_sain != value_malade):
                changes[j] = value_sain
                delta_curr = len(changes)

        # Check if found new smallest change
        if delta_curr < delta_min:
            delta_min = delta_curr
            min_changes = copy.deepcopy(changes)

    # Return smallest rule change that leads to healthy outcome
    return min_changes, delta_min
