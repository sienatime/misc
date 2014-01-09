from math import sqrt

def reverselist(l):
    tokens = l.split()
    for i in range(1, len(tokens)+1):
        print tokens[-i],

def count_words(l):
    d = {}
    for word in l:
        val = d.get(word, 0)
        d[word] = val + 1
    final_list = []
    for key,value in d.iteritems():
        final_list.append([key, value])
    return final_list

def html_table(l):
    html = "<table><tbody>"

    for row in l:
        html += "<tr>"
        for cell in row:
            html = html + "<td>" + cell + "</td>"
        html += "</tr>"

    html += "</table></tbody>"

    return html

def sort_list(l):
    temp_list = []
    last_char = ""
    for i in range(len(l)):
        last_char = l[i][-1]
        val = l[i].strip("KMG")
        temp_list.append( int(val) )

    if last_char in "0123456789":
        last_char = ""

    sort = sorted(temp_list)

    return [str(item) + last_char for item in sort]

def sort_by_size(l):
    # no character means it's bytes which is the smallest
    # then it goes K, M, G

    #okay let's put the each in their own list and sort those, then just join them together

    gigs = []
    megs = []
    kilos = []
    bytes = []

    for item in l:
        last_char = item[-1]
        if last_char == "G":
            gigs.append(item)
        elif last_char == "M":
            megs.append(item)
        elif last_char =="K":
            kilos.append(item)
        else:
            bytes.append(item)

    list_of_lists = [bytes, kilos, megs, gigs]
    sorted_lists = []

    for li in list_of_lists:
        sorted_lists.append(sort_list(li))

    final_list = []

    for li in sorted_lists:
        final_list += li

    return final_list

def is_prime(num):
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def prime(num):
    final = []

    for i in range(2, num+1):
        if is_prime(i):
            print i    

    return final

def main():
    reverselist("I am hungry")
    print count_words(["hello", "world","world"])
    print html_table([["one","uno"],['two','dos'],['three','tres']])
    print sort_by_size(["1M", "20G", "5012"])
    print prime(100)

main()