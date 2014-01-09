import pdb

def print_count(string):
    last_letter = string[0]
    final_str = ""
    counter = 1

    for i in range(1, len(string)):
        print i, last_letter
        
        if string[i] == last_letter:
            counter += 1
        else:
            final_str += last_letter + str(counter)
            counter = 1
        last_letter = string[i]

    final_str += last_letter + str(counter)

    print final_str

print_count("aabbbccca")