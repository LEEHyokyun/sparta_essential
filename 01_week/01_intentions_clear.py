def get_them(the_list):
    result = []
    for x in the_list:
        if x.p1 > 19:
            result.append(x)
    return result