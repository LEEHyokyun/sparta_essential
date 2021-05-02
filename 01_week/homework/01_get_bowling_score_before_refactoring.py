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
    #점수대로 얻는 점수표와
    #추가점수를 얻는 점수표를 분리해서 생각하는 로직!

    additional_score = [0] * (len(table) + 2)
    result = 0

    #현재 프레임 및 볼을 던진 횟수를 저장하는 배열까지 생각하는 로직!
    #10프레임에서 S/P일 경우 점수를 반영하지 않는다
    frame = 1
    current_try_bowling_count = 0

    #S/P일 경우
    for i in range(len(table)):
        if table[i] == 'S':
            score = 10
            if frame < 10:
                additional_score[i + 1] = additional_score[i + 1] + 1
                additional_score[i + 2] = additional_score[i + 2] + 1
        elif table[i] == '-':
            score = 0
        #스페어 처리
        #두 프레임의 합이 10일 경우
        #이전에 0점, 그 이후에 10점이어도 스페어 인정
        #이전 프레임이 '-'일 경우에 대한 분기처리 필요
        elif table[i] == 'P':
            if frame < 10:
            #추가점수가 생긴다면 이후 인덱스에 추가점수를 일단 반영해놓고
            #다만 10번째 프레임에서는 보너스 점수 반영은 없어야 한다
                additional_score[i + 1] = additional_score[i + 1] + 1
            if table[i - 1] == '-':
                score = 10
            else:
                score = 10 - int(table[i - 1])
        else:
            score = int(table[i])

        current_try_bowling_count = current_try_bowling_count + 1
        if table[i] == 'S' or current_try_bowling_count == 2:
            frame = frame + 1
            current_try_bowling_count = 0
        #현재 결과에 누적하여 score를 더하고, 여기에 score를 또 더해줘서 추가점수를 반영하는 방식
        result = result + score * (1 + additional_score[i])

    print(table)
    print(additional_score)
    print(result)
    return result

assert get_bowling_score("9-8P72S9P-9S-P9-SS8") == 150
assert get_bowling_score("SSSSSSSSSSSS") == 300