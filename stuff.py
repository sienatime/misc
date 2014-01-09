def print_unique(l):
    for number in l:
        if is_unique(number):
            print number

def is_unique(number):
    s = set()
    for dig in str(number):
        if dig in s:
            return False
        else:
            s.add(dig)
    return True