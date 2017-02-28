def print_matrix(m):
    for row in m:
        vals = [str(val) for val in row]
        print('|{0:16s}{1:16s}{2:16s}| {3:16s}|'.format(*vals))
    print()
