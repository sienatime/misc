def rotate_alpha(string, i):
    list_string = list(string)
    new_string  = []
    for c in list_string:
        # +1 because e - 5 should be a not z
        ord_val = ord(c) - i + 1
        if ord_val < 97:
            ord_val = ord_val + 26
        new_string.append(chr(ord_val))
    return "".join(new_string)