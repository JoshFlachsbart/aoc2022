""" Module to compare section assignments """

from collections import namedtuple

# Operations
def pt_one(crate_stacks, commands):
    """ Moves all crates at once """
    for cmd in commands:
        for i in range(cmd.count):
            crate_stacks[cmd.to].append(crate_stacks[cmd.fro].pop())
    return crate_stacks

def pt_two(crate_stacks, commands):
    """ Moves all crates at once """
    for cmd in commands:
        movers = []
        for i in range(cmd.count):
            movers.append(crate_stacks[cmd.fro].pop())
        movers.reverse()
        for i in movers:
            crate_stacks[cmd.to].append(i)
    return crate_stacks

# Printers
def get_top_crates_string(crate_stacks):
    crates_string = ''
    for crate_stack in crate_stacks:
        crates_string += crate_stack.pop()
    return crates_string

# Data Loaders
def load_crate_row(crate_stacks, crate_row_string, num_cols):
    """ Pull the crates from a row """
    crate_row =  [crate_row_string[(4*i)+1] for i in range(num_cols)]
    for i in range(num_cols):
        if crate_row[i] != ' ':
            crate_stacks[i].append(crate_row[i])

def load_crate_rows(crate_row_strings):
    """ Convert a bunch of crate rows into an array of crate stacks as a list """
    num_cols = (len(crate_row_strings[0]) - 3) // 4 + 1
    crate_stacks = [[] for i in range(num_cols)]
    crate_row_strings.pop()
    crate_row_strings.reverse()
    for crate_row_string in crate_row_strings:
        load_crate_row(crate_stacks, crate_row_string, num_cols)
    return crate_stacks

Command = namedtuple('Command', ['count', 'fro', 'to'])

def load_command(command_string):
    """ Converts a command string to a command array """
    commands = command_string.split()
    return Command(int(commands[1]), int(commands[3])-1, int(commands[5])-1)

def read_file(file_name):
    """ Read a full pair listing from a file """
    with open(file_name, encoding='utf-8') as data_file:
        crate_row_strings = []
        while data_file:
            crate_row_string = data_file.readline().rstrip('\n')
            if crate_row_string:
                crate_row_strings.append(crate_row_string)
            else:
                break

        crate_stacks = load_crate_rows(crate_row_strings)
        
        commands = []
        while data_file:
            command_row_string = data_file.readline().rstrip('\n')
            if command_row_string:
                commands.append(load_command(command_row_string))
            else:
                break
            
        return (crate_stacks, commands)

def run():
    """ Count all pairs with fully contained or overlapping sections """
    (crate_stacks, commands) = read_file('data.txt')
    print('Part 1 JRVNHHCSJ:', get_top_crates_string(pt_one(crate_stacks, commands)))
    (crate_stacks, commands) = read_file('data.txt')
    print('Part 2 GNFBSBJLH', get_top_crates_string(pt_two(crate_stacks, commands)))


run()
