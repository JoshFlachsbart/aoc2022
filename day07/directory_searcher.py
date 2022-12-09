""" Module to size up a filesystem """

# Simple File System Functions
def do_all_commands_simple(all_commands):
    """ Streamlined version of this problem. """
    path = ['/']
    path_sizes = {'/': 0}

    for command in all_commands:
        if command == '$ cd /':
            path = ['/']
        elif command.startswith('$ cd ..'):
            path.pop()
        elif command.startswith('$ cd'):
            new_path = path[-1] + command[5:] + '/'
            path.append(new_path)
            if (new_path not in path_sizes):
                path_sizes[new_path] = 0
        elif not command.startswith('$'):
            (val, name) = command.split()
            if not val == 'dir':
                for path_str in path:
                    path_sizes[path_str] += int(val)
        elif command == '$ ls':
            continue
        else:
            print("Error, unknown command: " + command)
    return path_sizes

# File System Functions
# Building a class because we might need it for part 2.  And I just found out they exist.
class Directory:
    path: str
    size: int
    files: list

    def __init__(self, path):
        self.path = path
        self.size = 0
        self.files = []

    def add_file(self, file_size, file_name):
        """ Premature optimization """
        self.files.append(file_name)
        # need to update the size of all the directories in this branch of the search tree.
        for dir in path_d:
            dir.size += file_size

root = Directory('/')
path_d = [root]
all_paths = {'/': root}

def do_all_commands(all_commands):
    """ Do the minimum amount of work to build up the file structure. """
    for command in all_commands:
        if command == '$ cd /':
            path_d = [root]
        elif command.startswith('$ cd ..'):
            path_d.pop()
        elif command.startswith('$ cd'):
            new_path = path_d[-1].path + command[5:] + '/'
            if (new_path not in all_paths):
                all_paths[new_path] = Directory(new_path)
            path_d.append(all_paths[new_path])
        elif not command.startswith('$'):
            (val, name) = command.split()
            if not val == 'dir':
                path_d[-1].add_file(int(val), name)
        elif command == '$ ls':
            continue
        else:
            print("Error, unknown command: " + command)

# Calculations
def cal_pt_1():
    total = 0
    for dir in all_paths.values():
        if dir.size <= 100000:
            total += dir.size
    return total

def cal_pt_1_simple(path_sizes):
    total = 0
    for size in path_sizes.values():
        if size <= 100000:
            total += size
    return total

def cal_pt_2():
    """ Find the file that gets you closest to the amount of needed space while providing that amount """
    disk_size = 70000000
    required_space = 30000000
    print('Total size:', disk_size)
    available_space = disk_size - root.size
    print('Available space', available_space)
    space_needed = required_space - available_space
    print('Free up:', space_needed)
    smallest_delete = root.size
    for dir in all_paths.values():
        if dir.size < smallest_delete and dir.size >= space_needed:
            smallest_delete = dir.size
    return smallest_delete

def cal_pt_2_simple(path_sizes):
    """ Find the file that gets you closest to the amount of needed space while providing that amount """
    disk_size = 70000000
    required_space = 30000000
    print('Total size:', disk_size)
    available_space = disk_size - path_sizes['/']
    print('Available space', available_space)
    space_needed = required_space - available_space
    print('Free up:', space_needed)
    smallest_delete = path_sizes['/']
    for size in path_sizes.values():
        if size < smallest_delete and size >= space_needed:
            smallest_delete = size
    return smallest_delete

# Loader

def read_file(file_name):
    """ Read a full pair listing from a file """
    all_command_lines = []
    with open(file_name, encoding='utf-8') as data_file:
        all_command_lines = [line.strip() for line in data_file]
    return all_command_lines

def run():
    """ Search for a collection of files depending on part specific rules """
    all_command_lines = read_file('data.txt')
    do_all_commands(all_command_lines)

    print('Part 1 1454188:', cal_pt_1())
    print('Part 2 4183246:',cal_pt_2())

# Redoing it without the class, but a simple hash map string -> int
    path_sizes = do_all_commands_simple(all_command_lines)
    print('Part 1 simple 1454188:', cal_pt_1_simple(path_sizes))
    print('Part 2 simple 4183246:',cal_pt_2_simple(path_sizes))

run()
