#모호한 변수명과 함수명을 변경해보고
#의도와 속성이 명확하게 나타나도록
#사소한 부분까지 모두 가독성을 고려하여 변경할 것
#상수화
#상수변수는 대문자로 표현


#AS IS
def ride_bus(obj, var):
    # 버스가 만석인지 확인합니다.
    # 버스가 만석이라면 함수를 종료하고, 그렇지 않다면 유저가 해당 버스에 탑승합니다.
    if obj.check():
        return
    else:
        var.fun(obj)

    # 탑승해서 나의 나이에 맞게 사용요금을 냅니다.
    if var.prop < 19:
        var.fun2(800)
    elif var.prop > 65:
        pass
    else:
        var.fun2(1300)

    # 만약 버스의 현재 위치가 내가 내리고 싶은 종착지라면 하차합니다.
    if obj.loc == var.dst:
        var.fun3(obj)


#TO BE

ADULT_AGE = 19
CHILD_FEE = 800
ADULT_FEE = 1300
THE_ELDERLY_AGE = 65


def func(bus, user):

    if bus.is_full():
        return
    else:
        user.get_on(bus)

    if user.prop < ADULT_AGE:
        user.age(CHILD_FEE)
    elif user.prop > THE_ELDERLY_AGE:
        pass
    else:
        user.age(ADULT_FEE)

    if bus.location == user.destination:
        user.get_off(bus)