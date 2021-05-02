#1. 1게임은 총 10프레임으로 구성되어 있다.
#2. 각 프레임마다 볼링핀 10개를 세워두고 공으로 쓰러뜨리는 것이며 기본적으로 볼링핀 1개당 1점이다.
#3. 각 프레임마다 2번의 기회가 주어지며 첫 번째 기회에 10개의 핀을 모두 쓰러뜨리는 것을 스트라이크(S)라고 한다.
#4. 두 번째 기회까지 사용하여 10개의 핀을 쓰러뜨리는 것을 스페어(P)라고 한다.
#5. 스트라이크를 치면 다음 두 번의 기회동안 쓰러뜨린 볼링핀의 개수만큼 추가점수를 얻게 된다.
#6. 10프레임을 제외한 프레임에서 스트라이크를 치면 해당 프레임의 두 번째 기회는 사라진다.
#7. 스페어를 치면 다음 한번의 기회동안 쓰러뜨린 볼링핀의 개수만큼 추가점수를 얻게 된다.
#8. 마지막 10번째 프레임에서 스트라이크를 칠 경우 두번의 보너스 기회가 제공된다. 이때 두번의 보너스 기회동안 추가점수는 존재하지 않는다.
#9. 마지막 10번째 프레임에서 스페어를 칠 경우 한번의 보너스 기회가 제공된다. 이때 한번의 보너스 기회동안 추가점수는 존재하지 않는다.
#이때 스트라이크는 S, 스페어는 P, 핀을 하나도 못 쓰러뜨린 것은 -으로 주어진다.

def get_bowling_score(table):

    additional_score = [0] * (len(table) + 2)  # 추가점수구하기
    result = 0  # 총점수구하기

    frame = 1  # 추가점수구하기
    current_try_bowling_count = 0  # 추가점수구하기


    for i in range(len(table)):
        # 점수구하기로직
        #score변수 인라인화
        #score = get_score(i, table)

        #추가점수구하기로직
        set_additional_score(additional_score, frame, i, table)

        #프레임수구하기로직
        #current_try_bowling_count 인자를 다시 넘겨주는 이유 살펴보기
        #Tuple형식
        frame, current_try_bowling_count = set_frame_and_try_count_at_frame(current_try_bowling_count, frame, i, table)

        result = result + get_score(i, table) * (1 + additional_score[i]) #점수구하기+추가점수구하기

    print(table)
    print(additional_score)
    print(result)
    return result


def set_frame_and_try_count_at_frame(current_try_bowling_count, frame, i, table):
    current_try_bowling_count = current_try_bowling_count + 1  # 프레임수구하기
    if table[i] == 'S' or current_try_bowling_count == 2:  # 프레임수구하기
        frame = frame + 1  # 프레임수구하기
        current_try_bowling_count = 0  # 프레임수구하기
    return frame, current_try_bowling_count


def set_additional_score(additional_score, frame, i, table):
    if table[i] == 'S':
        if frame < 10:  # 추가점수구하기
            additional_score[i + 1] = additional_score[i + 1] + 1  # 추가점수구하기
            additional_score[i + 2] = additional_score[i + 2] + 1  # 추가점수구하기
    elif table[i] == 'P':
        if frame < 10:  # 추가점수구하기
            additional_score[i + 1] = additional_score[i + 1] + 1  # 추가점수구하기


def get_score(i, table):
    if table[i] == 'S':
        score = 10  # 그냥 점수 구하기
    elif table[i] == '-':
        score = 0  # 그냥 점수 구하기
    elif table[i] == 'P':
        if table[i - 1] == '-':
            score = 10  # 그냥점수구하기
        else:
            score = 10 - int(table[i - 1])  # 그냥점수구하기
    else:
        score = int(table[i])  # 그냥점수구하기
    return score


assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300