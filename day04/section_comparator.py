""" Module to compare section assignments """

# Containment functions
def section_contains(sec_a, sec_b) -> bool:
    """ Check if the first section contains the second section """
    return sec_a[0] <= sec_b[0] and sec_a[1] >= sec_b[1]

def pair_section_contains(sections_pair) -> bool:
    """ Compare one direction then the other. """
    return section_contains(sections_pair[0], sections_pair[1]) or section_contains(sections_pair[1], sections_pair[0])

def count_containing_pairs(all_pair_sections):
    """ Count all the pairs with fully contained sections """
    count = 0
    for sections_pair in all_pair_sections:
        if pair_section_contains(sections_pair):
            count += 1
    return count

# Overlapment functions
def section_not_overlaps(sec_a, sec_b) -> bool:
    """ Check if the first section contains the second section """
    return sec_a[0] > sec_b[1] or sec_a[1] < sec_b[0]

def count_overlapping_pairs(all_pair_sections):
    """ Count all the pairs with overlapping sections """
    count = 0
    for sections_pair in all_pair_sections:
        if not section_not_overlaps(sections_pair[0], sections_pair[1]):
            count += 1
    return count

# Data Loaders
def load_section(sec_input):
    """ Convert the input string to an array """
    return [int(item) for item in sec_input.split('-') if item.isdigit()]

def load_pair(pair_string):
    """ Convert the input strig to a pair of arrays """
    return [load_section(sec_string) for sec_string in pair_string.split(',')]

def read_file(file_name):
    """ Read a full pair listing from a file """
    all_pair_sections = []
    with open(file_name, encoding='utf-8') as data_file:
        all_pair_sections = [load_pair(line.strip()) for line in data_file]
    return all_pair_sections

def run():
    """ Count all pairs with fully contained or overlapping sections """
    all_pair_sections = read_file('data.txt')
    print('Total Pairs', len(all_pair_sections))
    print('Containing Pairs 485: ', count_containing_pairs(all_pair_sections))
    print('Overlapping Pairs 857: ', count_overlapping_pairs(all_pair_sections))

run()
