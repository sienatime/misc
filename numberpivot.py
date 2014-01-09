def find_pivot(l):
    for i in range(1, len(l)-1):
        if sum(l[:i]) == sum(l[i+1:]):
            return i

def main():
    l = [4,6,1,3,7,2,1,1]
    
    print find_pivot(l)

main()