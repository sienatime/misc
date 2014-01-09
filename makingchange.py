def change(num):
    # so, you can optimize, by taking out the biggest numbers first...that would get you one way. so maybe you should just doooo thaattttt. it's like, the number of ways to do it optimizing for quarters plus the number of ways you can make quarters.......or something like that.
    if num == 1:
        return 1
    elif num == 5:
        return 2
    elif num == 10:
        return 4
    elif num == 15:
        return change(10) + change(5)
    else:
        denom = num / 10
        if denom > 0:
            return change(10)
        return 0 + change(num-1)