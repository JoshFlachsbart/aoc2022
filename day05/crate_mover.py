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
def load_crate_row(crate_stacks, crate_row_string, num_cols):
    """ Pull the crates from a row """
    crate_row =  [crate_row_string[(4*i)+1] for i in range(num_cols)]
    for i in range(num_cols):
        if crate_row[i] != ' ':
            crate_stacks[i].append(crate_row[i])

def read_file(file_name):
    """ Read a full pair listing from a file """
    crate_row_strings = []
    with open(file_name, encoding='utf-8') as data_file:
        done = False
        while not done:
            crate_row_string = data_file.readline().rstrip('\n')
            if crate_row_string:
                crate_row_strings.append(crate_row_string)
            else:
                done = True

        num_cols = (len(crate_row_strings[0]) - 3) // 4 + 1
        crate_stacks = [[] for i in range(num_cols)]
        print(crate_stacks)
        crate_row_strings.pop()
        crate_row_strings.reverse()
        for crate_row_string in crate_row_strings:
            load_crate_row(crate_stacks, crate_row_string, num_cols)
        print ('Start ', crate_stacks)

        while data_file:
            command_row_string = data_file.readline().rstrip('\n')
            commands = command_row_string.split()
            cmd_count = int(commands[1])
            from_col = int(commands[3])
            to_col = int(commands[5])
            print(f'{cmd_count}, {from_col}, {to_col}')
            for i in range(cmd_count):
                crate_stacks[to_col-1].append(crate_stacks[from_col-1].pop())
            print ('Count ', crate_stacks)

def run():
    """ Count all pairs with fully contained or overlapping sections """
    all_pair_sections = read_file('data.txt')
    print('Total Pairs', len(all_pair_sections))
    print('Containing Pairs: ', count_containing_pairs(all_pair_sections))
    print('Overlapping Pairs: ', count_overlapping_pairs(all_pair_sections))

# run()
