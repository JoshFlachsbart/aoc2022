""" Module to compare section assignments """
def section_contains(sec_a, sec_b) -> bool:
    """ Check if the first section contains the second section """
    return sec_a[0] <= sec_b[0] and sec_a[1] >= sec_b[1]

def section_not_overlaps(sec_a, sec_b) -> bool:
    """ Check if the first section contains the second section """
    return sec_a[0] > sec_b[1] or sec_a[1] < sec_b[0]

def pair_section_contains(sections_pair) -> bool:
    """ Compare one direction then the other. """
    return section_contains(sections_pair[0], sections_pair[1]) or section_contains(sections_pair[1], sections_pair[0])

def load_section(sec_input):
    """ Convert the input string to an array """
    sec_string = sec_input.split('-')
    return (int(sec_string[0]),int(sec_string[1]))

def load_pair(pair_string):
    """ Convert the input strig to a pair of arrays """
    sec_strings = pair_string.split(',')
    sections_pair = []
    for sec_string in sec_strings:
        sections_pair.append(load_section(sec_string))
    return sections_pair


def run():
    """ Count all pairs with fully contained overlap """
    all_pair_sections = []
    with open('data.txt', encoding='utf-8') as data_file:
        done = False
        while not done:
            line = data_file.readline().strip()
            if not line:
                done = True
                break
            all_pair_sections.append(load_pair(line))

    count = 0
    for sections_pair in all_pair_sections:
        if pair_section_contains(sections_pair):
            count += 1
    print('Total Pairs', len(all_pair_sections))
    print('Containing Pairs: ', count)
    count = 0
    for sections_pair in all_pair_sections:
        if not section_not_overlaps(sections_pair[0], sections_pair[1]):
            count += 1
    print('Overlapping Pairs: ', count)

run()
