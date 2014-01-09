
d = {"f":["f","F"],"a":["a","A","4","@"],"c":["c","C"],"e":["e","E","3"]}

def password_permute(s):
    global d
    if len(s) == 1:
        return d.get(s)
    else:
        l = password_permute(s[1:])

        answer = []

        for string in l:
            for c in d.get(s[0]):
                answer.append(c+string)

        return answer