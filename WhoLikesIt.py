def likes(names):
    if len(names) < 1:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", "+names[1]+" and "+ names[2]+" like this"
    else:
        others = str(len(names)-2)
        return names[0] + ", "+names[1]+ " and " + others + " others like this" 