class parent():
    def give(self):
        print("give")


    def take(self):
        print("take")


class Child_one():
    pass


# 자식클래스(부모클래스) 형식으로
# 부모클래스의 속성을 상속받는다.
class Child_two(parent):
    def eat(self):
        print("eat")


Father = parent()
Father.give
Father.take

Chulsoo = Child_two()
Chulsoo.give
Chulsoo.take
Chulsoo.eat

# Child_one은 상속이나 속성없는 빈(empty) 클래스
# Child_two은 parent 클래스를 상속받아 give/take 속성사용가능