def check_zipped(str1, str2, zipped):
    shorter = None
    other = None

    if len(str1) < len(str2):
        shorter = str1
        other = str2pyt
    else:
        shorter = str2
        other = str1

    zipped_list = list(zipped)
    end = -1

    for i in range(len(zipped_list)-1, -1, -1):
        if zipped_list[i] == shorter[end]:
            del zipped_list[i]
            end -= 1
            if end < -len(shorter):
                break  

    compare = "".join(zipped_list)

    print compare

    if compare == other:
        return True

    return False

str1 = "dry erase"
str2 = "board"
zipped = "dbroya redrase"

print check_zipped(str1, str2, zipped)