""" Module to sort out the rucksack mess """
def get_compartments(sack_val):
    """ Returns comparments from input string """
    compartment_len = len(sack_val)//2
    return [sack_val[:compartment_len],sack_val[compartment_len:]]

def get_duplicates(compartments):
    """ Finds repeats in the two compartments.
        Currently stops at first duplicate. """
    duplicates = []
    for item in compartments[0]:
        found_idx = compartments[1].find(item)
        if found_idx >= 0:
            duplicates.append(item)
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

def run():
    """ Calculate the total priorities from a rucksack input file. """
    all_rucksack_compartments = []
    with open('data.txt', encoding='utf-8') as data_file:
        done = False
        while not done:
            line = data_file.readline().strip()
            if not line:
                done = True
                break
            all_rucksack_compartments.append(get_compartments(line))
    all_duplicates = []
    for rucksack in all_rucksack_compartments:
        all_duplicates.extend(get_duplicates(rucksack))
    total_priority = calc_priorities(all_duplicates)
    return total_priority
