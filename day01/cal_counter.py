""" Module to count calories carried by an elf. """
def count():
    """ Count the number of calories for each elf """
    elf_count = [0]
    elf_num = 0
    with open('data.txt', encoding='utf-8') as data_file:
        done = False
        while not done:
            line = data_file.readline()
            if not line:
                done = True
                break
            if line.strip():
                elf_count[elf_num] += int(line)
            else:
                elf_count.append(0)
                elf_num += 1
    return elf_count

def topn(num_elves_to_count):
    """ Find the sum of the top three calories """
    cal_counts = count()
    cal_counts.sort(reverse=True)
    return sum(cal_counts[:num_elves_to_count])
