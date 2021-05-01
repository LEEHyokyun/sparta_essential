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


def get_result(order_histories, cartoon_info):
    result = ""

    for order_history in order_histories:
        result += f"{order_history['customer']} 주문 내역\n" #출력결과 추가하기
        #print(result)
        total_amount = 0  #총비용 계산하기
        point = 0 #포인트 계산하기

        for cartoon_consumption_history in order_history["cartoon_consumption_histories"]: #각 만화별 소비기록 for문
            #amount가 0으로 선언한후에, 아래 로직에서 사용된 후 다시 return 되고 있다.
            #굳이 여기서 선언될 필요없이, 아래 계산로직에 포함되도 무방하다.
            #amount = 0 #각 만화별 비용 계산하기
            # cartoon_id는 위 딕셔너리에서 사용되고있는, 유효한 key값
            cartoon = cartoon_info[cartoon_consumption_history["cartoon_id"]]  #만화 정보 가져오기
            amount = calculate_cost_of_comic(cartoon, cartoon_consumption_history)
            point += max(cartoon_consumption_history["view_count"] - 30, 0) #포인트 계산하기
            if cartoon["genre"] == "소년만화": # 만화 정보 가져오기 -> 나중에 포인트 계산
                point += math.floor(cartoon_consumption_history["view_count"] / 5) #포인트 계산하기

            result += f"{cartoon['name']} : {amount}원 {cartoon_consumption_history['view_count']} 권 대여 \n" #출력결과 출력하기
            total_amount += amount #총 비용 계산하기

        result += f"총액 {total_amount}원 " #출력결과 출력하기
        result += f"적립 포인트 {point}점\n \n" #출력결과 출력하기
    return result

#기존 amount 매개변수를 받았지만, 내부에서 선언되어 amount 인자를 받을 필요가 없어졌다!
def calculate_cost_of_comic(cartoon, cartoon_consumption_history):
    amount = 0 #각 만화별 비용 계산하기
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

#리팩토링의 중요한 사항은 assert를 통한 assertionError 확인하는 것!
#기존 result를 objective_result에 넣고, 리팩토링한 결과인 result와 비교!
#위 test 작업을 assertionError를 통해 리팩토링!

#objective_result의 문자열이 result 문자열에 들어있는가?
assert objective_result in result