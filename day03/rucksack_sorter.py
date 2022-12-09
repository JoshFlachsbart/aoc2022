""" Module to sort out the rucksack mess """
def get_compartments(sack_val):
    """ Returns comparments from input string """
    compartment_len = len(sack_val)//2
    return [sack_val[:compartment_len],sack_val[compartment_len:]]

def get_duplicates(items_a, items_b, stop=True):
    """ Finds repeats in two lists, optioanally stopping at first found. """
    duplicates = []
    for item in items_a:
        found_idx = items_b.find(item)
        if found_idx >= 0:
            duplicates.append(item)
            if stop:
                break
    return duplicates

def calc_priority(item):
    """ Converts a single item to its numerical priority value. """
    priority = None
    raw_val = ord(item)
    if raw_val >= 97:
        priority = raw_val - 96
    else:
        priority = raw_val - 38
    return priority

def calc_priorities(items):
    """ Calculates full priority for a list of items. """
    priority = 0
    for item in items:
        priority += calc_priority(item)
    return priority

def calc_compartments(all_rucksack_contents):
    """ Calcualte the priority of duplicates across compartments """
    all_duplicates = []
    for rucksack in all_rucksack_contents:
        compartments = get_compartments(rucksack)
        all_duplicates.extend(get_duplicates(compartments[0], compartments[1]))
    return calc_priorities(all_duplicates)

def calc_groups(all_rucksack_contents):
    """ Calcualte the priority of duplicates withing groups """
    all_duplicates = []
    num_groups = len(all_rucksack_contents)//3
    for group in range(num_groups):
        idx = group * 3
        (cont_a, cont_b, cont_c) = all_rucksack_contents[idx:idx+3]
        group_dupes = get_duplicates(cont_a, cont_b, stop=False)
        all_duplicates.extend(get_duplicates(group_dupes,cont_c))
    return calc_priorities(all_duplicates)

def load_all_contents():
    """ Calculate the total priorities across compartments from a rucksack input file. """
    with open('data.txt', encoding='utf-8') as data_file:
        return [line.strip() for line in data_file]

def run ():
    all_rucksack_contents = load_all_contents()
    print('Compartments 8349:', calc_compartments(all_rucksack_contents))
    print('Groups 2681:', calc_groups(all_rucksack_contents))

run()