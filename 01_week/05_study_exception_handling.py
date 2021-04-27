#예외처리 첫번째 : 배열
#try - except practice

#단순 try - exception
#예외내용을 모른다.
try:
    arr = [1, 2]
    print(arr[3])
    4 / 0
except:
    print("exception occurs")

#아래 오류발생시 나오는 에러문을 참조해서
#IndexError 발생시
#ZeroDivisionError 발생시 (0으로 나눌때)

try:
    arr = [1, 2]
    print(arr[3])
    4 / 0
except IndexError as error_Index:
    print(error_Index)
except ZeroDivisionError as error_Zero:
    print(error_Zero)