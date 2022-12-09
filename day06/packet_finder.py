""" Module to find start of message """

def check_packet(packet):
    for i in range(len(packet)):
        for j in range(i+1,len(packet)):
            i_val = packet[i]
            j_val = packet[j]
            if i_val == j_val:
                return False
    return True

def find_first(message_stream, packet_size):
    for i in range(len(message_stream) - packet_size + 1):
        if check_packet(message_stream[i:i+packet_size]):
            return i+packet_size

def run(file_name, packet_size=4):
    """ Calculate the total priorities across compartments from a rucksack input file. """
    all_lines = []
    with open(file_name, encoding='utf-8') as data_file:
        all_lines = [line.strip() for line in data_file]

# testing
#     for line in all_lines:
#        print(line, find_first(line, packet_size))
    return find_first(all_lines[0], packet_size)

def run_all():
    print('Part 1 1766:', run('data.txt'))
    print('Part 2 2383:', run('data.txt', 14))

run_all()

def test():
    print(check_packet('abcd'))
    print(check_packet('abca'))
    print(find_first('abcdefg', 4))
    print(find_first('aabcefg', 4))
#    find_first('test.txt')

# test()
