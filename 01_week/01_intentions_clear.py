# 코드의 가독성을 높이는 방안을 고려해본다.
# 클린코드

# AS IS

def get_them(the_list):
    result = []
    for x in the_list:
        if x.p1 > 19:
            result.append(x)
    return result


# TO BE

ADULT_AGE = 19

def get_adults(people):
    adults = []
    for person in people:
        if person.age > ADULT_AGE:
            adults.append(person)
    return adults
