def pali_ana(string):
    d = {}
    for c in string:
        count = d.get(c, 0)
        count += 1
        d[c] = count
    return is_pa(d)

def is_pa(d):
    found_odd = False
    for num in d.values():
        if num % 2 != 0:
            if found_odd:
                return False
            else:
                found_odd = True

    return True