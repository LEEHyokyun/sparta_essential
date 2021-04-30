#의도적인 예외처리를 할 경우


#AS IS
#get_video 함수를 호출하여 사용하는 다른 함수가 있을때
#get_video 값에 따른 분기처리를 또 다시 해줘야 한다.
#if video is not None : ~ else : ~

#TO BE
#raise Exception으로 의도적인 예외처리를 통해, get_video는 어찌되었던 무조건 올바른 값만 반환(예외발생시 return 없음)
#각 예외처리별 다른 동작 및 처리가 필요할 경우
#예외처리를 적용할 경우

#from enum import Enum

#class ErrorCode(Enum):
    #MUST_HAVE_LICENSE = 1
    #CURRENT_VIEW_COUNT_OVER_FOUR = 2

#소괄호내 특정 클래스를 넣어 하나의 클래스에 상속시킨다
class MustHaveLicenseError(Exception): #예외 개별 클래스화
    pass

def display_video(video, user):
    try:
        video = get_video(video, user)
    except Exception as e:
        if e.args[0] == "사용권이 있어야만 볼 수 있습니다":
            pass #사용권 구매 페이지로 이동하는 로직
        ...#예외 개별클래스를 사용하여 이에 대한 동작을 처리하도록 설정


    #video = get_video(video, user)
    #if video == ErrorCode.MUST_HAVE_LICENSE
    #    ....

def get_video(video, user):
    if not user.has_licensed():
        #return None
        raise Exception("사용권이 있어야만 볼 수 있습니다")
        #return ErrorCode.MUST_HAVE_LICENSE
    elif user.license.current_view_count >= 4:
        raise Exception("현재 시청자가 많아 시청이 불가합니다")
        #return ErrorCode.CURRENT_VIEW_COUNT_OVER_FOUR
    return get_video_contents(video)


def get_video_contents(video):
    ...
    return video

