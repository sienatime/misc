import pdb

def count_items(l):
    d = {}
    for item in l:
        counter = d.get(item, 0)
        counter += 1
        d[item] = counter

    return sorted(d.items(), key=lambda x: x[1])

print count_items(["hello","world","world","hello","hello"])

def templatize(template, values):
    d = {}
    for key, val in values:
        d[key] = val

    open_paren = False
    key = ""

    tokens = template.split()

    for i in range(len(tokens)):
        token = tokens[i]
        if "{" in token and "}" in token:
            start = token.index("{")
            end = token.index("}")
            key = token[start:end+1]
            val = d.get(key[1:-1])
            print val
            tokens[i] = tokens[i].replace(key, val)

    return " ".join(tokens)
    

print templatize("{name} uses {product}? I use {product} too!", [["name","John"],["product","vim"]])