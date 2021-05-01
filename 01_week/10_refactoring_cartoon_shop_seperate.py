import math

input_cartoon_info = {
    "진격의거인": {"name": "진격의 거인", "genre": "판타지"},
    "원피스": {"name": "원피스", "genre": "소년만화"},
    "짱구": {"name": "짱구는 못말려", "genre": "코믹"},
    "괴짜가족": {"name": "괴짜 가족", "genre": "코믹"},
}

input_order_histories = [
    {
        "customer": "의정부고",
        "cartoon_consumption_histories":
            [
                {
                    "cartoon_id": "진격의거인", "view_count": 55
                },
                {
                    "cartoon_id": "원피스", "view_count": 40
                },
                {
                    "cartoon_id": "짱구", "view_count": 20
                },
                {
                    "cartoon_id": "괴짜가족", "view_count": 15
                }
            ]
    },
    {
        "customer": "의여고",
        "cartoon_consumption_histories":
            [
                {
                    "cartoon_id": "진격의거인", "view_count": 20
                },
                {
                    "cartoon_id": "원피스", "view_count": 10
                },
                {
                    "cartoon_id": "짱구", "view_count": 50
                },
                {
                    "cartoon_id": "괴짜가족", "view_count": 60
                }
            ]
    },
]


# 메인 함수(result 얻기) / 신규 함수(result 출력하기) 기능분리
# 메인함수에서 return을 통해 결과 얻는 로직 추가
def get_result(order_histories, cartoon_info):
    # 결과얻기/출력하기의 완전한 분리를 위해, 먼저 메인함수의 중간데이터를 설정하고
    # 이 중간데이터에 아래 사용되는 신규함수 인자들을 모두 넣는다고 생각하면 된다.

    ##최종변수 인라인화
    ##order_data_list = get_order_data_list(cartoon_info, order_histories)

    ##아래 코드는 최종 중간데이터 내용을 반영한 후에 코드이고,
    ##이마저도 extract method하여 코드를 간결화한다!
    ##order_data_list = []
    ##for order_history in order_histories:

        # 각 주문내역의 만화별 소비내역에서 만화이름/총비용/총조회수를 for문 반복후
        # 반복후에 나오는 요소들을 집어넣기 위한 공배열 만들기
        # 중간배열로 작용한다
        ##cartoon_consumption_histories = []
        ##for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:
            # result 대신에 cartoon_consumption_histories 배열에 넣어 전달하는 방식으로 변경
            # result += f"{get_cartoon(cartoon_consumption_history, cartoon_info)['name']} : {calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info), cartoon_consumption_history)}원 {cartoon_consumption_history['view_count']} 권 대여 \n"  # 출력결과 출력하기
            ##cartoon_consumption_histories.append({
                # 만화이름 / 총비용 / 총조회수가 들어가야함
                ##"cartoon_name": get_cartoon(cartoon_consumption_history, cartoon_info)['name'],
                ##"amount": calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info), cartoon_consumption_history),
                ##"view_count": cartoon_consumption_history['view_count']
            ##})

        # order_data_list는 배열인데, 추가되는 인자는 딕셔너리
        ##order_data_list.append({
            # result = 를 얻기위해 필요한 인자들 정보는 무엇인가?
            # 1. 고객의 이름 'customer'
            # 배열내 딕셔너리 형태로 저장된 형식, 그대로 형식유지해서 넘겨준다
            # [{"customer" : "의정부고"},{"customer" : "의여고"}] 형태로 저장
            # key값을 사용하여, 안의 value값을 넘겨줄 수 있도록(그대로 형태유지) 설정해준다
            ##"customer": order_history['customer'],

            # 2. 각 주문내역의 총 만화비용 'total_amount'
            # [{"customer" : "의정부고", "total_amount" : total_amount},{"customer" : "의여고", "total_amount" : total_amount}] 형태로 저장
            ##"total_amount": calculate_total_amount_from_histories(cartoon_info, order_history),

            # 3 각 주문내역의 총 포인트 'point'
            # [{"customer" : "의정부고", "total_amount" : total_amount, "point" : point},{"customer" : "의여고", "total_amount" : total_amount, "point" : point}] 형태로 저장
            ##"point": calculate_point_from_histories(cartoon_info, order_history),

            # 4. 각 주문내역의 만화별 소비 내역에서 만화이름  '배열로 표시'
            # 5. 각 주문내역의 만화별 소비 내역에서 총 비용 '배열로 표시'
            # 6. 각 주문내역의 만화별 소비 내역에서 총 조회수 '배열로 표시'
            ## 2/3/4 표시방법)
            ## [{"cartoon_name", "amount", "view_count"}]로 배열형태로 저장
            ## cartoon_consumption_histories 배열에 저장된다
            ##"cartoon_consumption_histories": cartoon_consumption_histories
        ##})

    # 계산 / 포맷팅 분리하기 첫번째 작업 : 중간 데이터 만들기
    # 중간 데이터를 받아 출력만을 담당하는 함수 get_output_data 함수를 별도 생성하기
    # return get_output_data의 인자도 아래 중간데이터 반영에 따라 모두 달라지게 된다
    return get_output_data(get_order_data_list(cartoon_info, order_histories))


def get_order_data_list(cartoon_info, order_histories):
    order_data_list = []
    for order_history in order_histories:

        # 각 주문내역의 만화별 소비내역에서 만화이름/총비용/총조회수를 for문 반복후
        # 반복후에 나오는 요소들을 집어넣기 위한 공배열 만들기
        # 중간배열로 작용한다
        cartoon_consumption_histories = []
        for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:
            # result 대신에 cartoon_consumption_histories 배열에 넣어 전달하는 방식으로 변경
            # result += f"{get_cartoon(cartoon_consumption_history, cartoon_info)['name']} : {calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info), cartoon_consumption_history)}원 {cartoon_consumption_history['view_count']} 권 대여 \n"  # 출력결과 출력하기
            cartoon_consumption_histories.append({
                # 만화이름 / 총비용 / 총조회수가 들어가야함
                "cartoon_name": get_cartoon(cartoon_consumption_history, cartoon_info)['name'],
                "amount": calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info),
                                                  cartoon_consumption_history),
                "view_count": cartoon_consumption_history['view_count']
            })

        # order_data_list는 배열인데, 추가되는 인자는 딕셔너리
        order_data_list.append({
            # result = 를 얻기위해 필요한 인자들 정보는 무엇인가?
            # 1. 고객의 이름 'customer'
            # 배열내 딕셔너리 형태로 저장된 형식, 그대로 형식유지해서 넘겨준다
            # [{"customer" : "의정부고"},{"customer" : "의여고"}] 형태로 저장
            # key값을 사용하여, 안의 value값을 넘겨줄 수 있도록(그대로 형태유지) 설정해준다
            "customer": order_history['customer'],

            # 2. 각 주문내역의 총 만화비용 'total_amount'
            # [{"customer" : "의정부고", "total_amount" : total_amount},{"customer" : "의여고", "total_amount" : total_amount}] 형태로 저장
            "total_amount": calculate_total_amount_from_histories(cartoon_info, order_history),

            # 3 각 주문내역의 총 포인트 'point'
            # [{"customer" : "의정부고", "total_amount" : total_amount, "point" : point},{"customer" : "의여고", "total_amount" : total_amount, "point" : point}] 형태로 저장
            "point": calculate_point_from_histories(cartoon_info, order_history),

            # 4. 각 주문내역의 만화별 소비 내역에서 만화이름  '배열로 표시'
            # 5. 각 주문내역의 만화별 소비 내역에서 총 비용 '배열로 표시'
            # 6. 각 주문내역의 만화별 소비 내역에서 총 조회수 '배열로 표시'
            ## 2/3/4 표시방법)
            ## [{"cartoon_name", "amount", "view_count"}]로 배열형태로 저장
            ## cartoon_consumption_histories 배열에 저장된다
            "cartoon_consumption_histories": cartoon_consumption_histories
        })
    return order_data_list


# 출력용 함수를 만들고, 어떤 인자를 추가로 넘겨줘야 하는지 파악한다.
# cartoon_info 인자 사용되지 않음
# order_histories도 order_data로 변경
def get_output_data(order_data_list):
    result = ""
    # get_result에서, 결국엔 result를 출력해야하므로, result를 구하는 모든 과정들을 불러오기

    # customer 넘겨받기
    #for index in range(len(order_data_list)):
    for order_data in order_data_list:
        # order_data_list는 배열이므로, 배열에서 정보를 뽑아쓰기위해 for문을 index 형식으로 변경하고
        # 이를 order_data에 넣은후, order_data에서 customer를 뽑아쓰는 형식으로 변경
        # for index in range(len(order_data_list)) 문에서 for order_data in order_data_list로 변경후엔 order_data 변수선언 필요없어짐
        #order_data = order_data_list[index]

        #order_history 사용되지 않음(포매팅후 반영된 코드임)
        #order_history = order_histories[index]

        # for order_history in order_histories:
        result += f"{order_data['customer']} 주문 내역\n"  # 출력결과 추가하기
        # print(result)

        # 반복문 쪼개기 2_누적되는 값에 대한 특정반복문을 구현한다
        # 특정 변수에 대한 반복문 쪼개기가 구성되면 또 함수를 추출한다!(리팩토링 할 수 있을때까지 리팩토링 지속)
        # total_amount는 이제 임시변수! 이를 함수화해서 사용하는 방식으로 다시 리팩토링!
        # total_amount = calculate_total_amount_from_histories(cartoon_info, order_history)

        # 반복문 쪼개기 1_누적되는 값에 대한 특정반복문을 구현한다
        # 특정 변수에 대한 반복문 쪼개기가 구성되면 또 함수를 추출한다!(리팩토링 할 수 있을때까지 리팩토링 지속)
        # point는 이제 임시변수! 이를 함수화해서 사용하는 방식으로 다시 리팩토링!
        # point = calculate_point_from_histories(cartoon_info, order_history)

        # 1변수 1반복문

        # order_data를 이용하여 위 배열로 저장된 2/3/4 데이터를 받아온다
        # for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:  # 각 만화별 소비기록 for문

        #중간배열로 받은 결과를 반영한 최종 for문
        for cartoon_consumption_history in order_data['cartoon_consumption_histories']:
            result += f"{cartoon_consumption_history['cartoon_name']} : {cartoon_consumption_history['amount']}원 {cartoon_consumption_history['view_count']} 권 대여 \n"  # 출력결과 출력하기

            # amount가 0으로 선언한후에, 아래 로직에서 사용된 후 다시 return 되고 있다.
            # 굳이 여기서 선언될 필요없이, 아래 계산로직에 포함되도 무방하다.
            # amount = 0 #각 만화별 비용 계산하기
            # cartoon_id는 위 딕셔너리에서 사용되고있는, 유효한 key값
            # cartoon = get_cartoon(cartoon_consumption_history, cartoon_info)  #만화 정보 가져오기 #cartoon_info 대입후 사용하지 않는 임시변수
            # amount = calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info), cartoon_consumption_history) #amount도 변화하는 값이 아닌, 대입후 변하지 않는 임시변수

            # 중간변수 order_data로 넘겨준 이후엔 result에 넘겨줄때 작동하는 함수가 달라진다
            # 임시변수 제거후 split 가능해짐..split하기
            # 변수와, 함수 매개변수는 되도록이면 중복을 피하고, 함수 내부에서 처리하도록 유도하기
            # result += f"{get_cartoon(cartoon_consumption_history, cartoon_info)['name']} : {calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info), cartoon_consumption_history)}원 {cartoon_consumption_history['view_count']} 권 대여 \n"  # 출력결과 출력하기

        # result += f"총액 {calculate_total_amount_from_histories(cartoon_info, order_history)}원 "  # 출력결과 출력하기
        result += f"총액 {order_data['total_amount']}원 "
        # result += f"적립 포인트 {calculate_point_from_histories(cartoon_info, order_history)}점\n \n"  # 출력결과 출력하기
        result += f"적립 포인트 {order_data['point']}점\n \n"  # 출력결과 출력하기
    return result


def calculate_total_amount_from_histories(cartoon_info, order_history):
    total_amount = 0  # 총비용 계산하기
    for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:  # 각 만화별 소비기록 for문
        total_amount += calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info),
                                                cartoon_consumption_history)  # 총 비용 계산하기
    return total_amount


def calculate_point_from_histories(cartoon_info, order_history):
    point = 0  # 포인트 계산하기
    for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:  # 각 만화별 소비기록 for문
        point = point + calculate_point(cartoon_consumption_history, cartoon_info)
    return point


def calculate_point(cartoon_consumption_history, cartoon_info):
    point = 0
    point += max(cartoon_consumption_history["view_count"] - 30, 0)  # 포인트 계산하기
    if get_cartoon(cartoon_consumption_history, cartoon_info)["genre"] == "소년만화":  # 만화 정보 가져오기 -> 나중에 포인트 계산
        point += math.floor(cartoon_consumption_history["view_count"] / 5)  # 포인트 계산하기
    return point


def get_cartoon(cartoon_consumption_history, cartoon_info):
    return cartoon_info[cartoon_consumption_history["cartoon_id"]]


# 기존 amount 매개변수를 받았지만, 내부에서 선언되어 amount 인자를 받을 필요가 없어졌다!
def calculate_cost_of_comic(cartoon, cartoon_consumption_history):
    amount = 0  # 각 만화별 비용 계산하기
    if cartoon["genre"] == "판타지":  # 장르확인 -> 나중에 만화 비용 계산
        amount += 1000 * (cartoon_consumption_history["view_count"] - 30)  # 만화 비용 계산하기
    elif cartoon["genre"] == "코믹":  # 장르확인 -> 나중에 만화 비용 계산
        amount = 30000  # 만화 비용 계산하기
        if cartoon_consumption_history["view_count"] > 20:  # 만화 비용 계산하기
            amount += 10000 + 500 * (cartoon_consumption_history["view_count"] - 20)  # 만화 비용 계산하기
    else:  # 장르확인 -> 나중에 만화 비용 계산
        amount = 4000 * cartoon_consumption_history["view_count"]  # 만화 비용 계산하기
    return amount


result = get_result(input_order_histories, input_cartoon_info)

objective_result = """의정부고 주문 내역
진격의 거인 : 25000원 55 권 대여 
원피스 : 160000원 40 권 대여 
짱구는 못말려 : 30000원 20 권 대여 
괴짜 가족 : 30000원 15 권 대여 
총액 245000원 적립 포인트 43점
 
의여고 주문 내역
진격의 거인 : -10000원 20 권 대여 
원피스 : 40000원 10 권 대여 
짱구는 못말려 : 55000원 50 권 대여 
괴짜 가족 : 60000원 60 권 대여 
총액 145000원 적립 포인트 52점"""
print(result)

# 리팩토링의 중요한 사항은 assert를 통한 assertionError 확인하는 것!
# 기존 result를 objective_result에 넣고, 리팩토링한 결과인 result와 비교!
# 위 test 작업을 assertionError를 통해 리팩토링!

# objective_result의 문자열이 result 문자열에 들어있는가?
assert objective_result in result
