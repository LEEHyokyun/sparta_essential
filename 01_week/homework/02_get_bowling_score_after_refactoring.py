def get_bowling_score(s):
    frame = 1 #프레임수구하기
    stack = 0 #프레임수구하기
    answer = 0 #총점수구하기
    plus = [] #추가점수구하기

    for i in range(len(s)):
        #그냥점수구하기 로직
        #add변수 인라인화
        #add = get_score(i, s)

        #추가점수구하기 로직
        append_index_to_plus(frame, i, plus, s)

        #프레임수구하기
        frame, stack = set_frame_and_stack(frame, i, s, stack)

        answer += get_score(i, s) * (plus.count(i) + 1) #총점수구하기

    return answer

#stack 인자 초기화 필요
#함수내부에서 구한 이후에 반드시 초기화(return) 필요하다
#함수추출후, 어떤 인자를 추가로 초기화해야하는지 파악한다
def set_frame_and_stack(frame, i, s, stack):
    if s[i] == 'S':
        stack = 0  # 프레임수구하기
        frame += 1  # 프레임수구하기
    else:
        stack += 1  # 프레임수구하기
        if stack == 2:
            stack = 0  # 프레임수구하기
            frame += 1  # 프레임수구하기
    return frame, stack


def append_index_to_plus(frame, i, plus, s):
    if s[i] == 'S':
        if frame < 10:
            plus.append(i + 1)  # 추가점수구하기
            plus.append(i + 2)  # 추가점수구하기
    else:
        if s[i] == 'P':
            if frame < 10:
                plus.append(i + 1)  # 추가점수구하기


def get_score(i, s):
    if s[i] == 'S':
        add = 10  # 그냥 점수 구하기
    else:
        if s[i] == 'P':
            if s[i - 1] == '-':
                add = 10  # 그냥 점수 구하기
            else:
                add = 10 - int(s[i - 1])  # 그냥 점수 구하기
        elif s[i] == '-':
            add = 0  # 그냥 점수 구하기
        else:
            add = int(s[i])  # 그냥 점수 구하기
    return add


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300