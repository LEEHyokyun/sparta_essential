#의도적인 예외처리를 할 경우


#AS IS
#get_video 함수를 호출하여 사용하는 다른 함수가 있을때
#get_video 값에 따른 분기처리를 또 다시 해줘야 한다.
#if video is not None : ~ else : ~

#TO BE
#raise Exception으로 의도적인 예외처리를 통해, get_video는 어찌되었던 무조건 올바른 값만 반환(예외발생시 return 없음)
#따라서 해당값 호출시 따로 분기처리를 안해줘도 특정값만 받아서 함수사용이 가능해짐

def get_video(video, user):
    if not user.has_licensed():
        #return None
        raise Exception("사용권이 있어야만 볼 수 있습니다")
    elif user.license.current_view_count >= 4:
        raise Exception("현재 시청자가 많아 시청이 불가합니다")
    return get_video_contents(video)


def get_video_contents(video):
    ...
    return video

