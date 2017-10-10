import turtle as t
import math

t.pensize(3)
t.speed(10)
for x in range(2):      # 태극기의 사각형 틀
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.pensize(2)
t.color("white")
t.lt(70)
t.fd(60)          # 건곤감리중 리를 그리는 코드

t.color("black")
t.rt(120)
t.fd(50)

t.color("white")  # 가운데 부분 시작
t.lt(90)
t.fd(10)
t.lt(90)

t.color("black")
t.fd(20)

t.color("white")
t.fd(10)

t.color("black")  # 공백 후 다시 가운데 마무리
t.fd(20)

t.color("white")  # 리 마무리
t.rt(90)
t.fd(10)

t.color("black")
t.rt(90)
t.fd(50)

t.color("white")      # 이 부분은 곤의 시작을 좀 밑에서 하면서 자연스럽게 하기위해
t.fd(15)


t.color("white")
t.lt(50)           #  곤 시작
t.fd(160)

t.color("black")
t.lt(65)
t.fd(20)

t.color("white")  # 첫번째 공백
t.fd(10)

t.color("black")
t.fd(20)

t.color("white")
t.rt(90)
t.fd(10)

t.color("black")
t.rt(90)
t.fd(20)

t.color("white")
t.fd(10)

t.color("black")
t.fd(20)

t.color("white")
t.lt(90)
t.fd(10)

t.color("black")
t.lt(90)
t.fd(20)

t.color("white")
t.fd(10)

t.color("black")
t.fd(20)              # 곤 마무리

t.color("white")
t.lt(25)
t.fd(90)

t.color("black")        # 감 시작
t.lt(45)
t.fd(20)

t.color("white")
t.fd(10)

t.color("black")
t.fd(20)

t.color("white")  # 가운데 부분 시작
t.lt(90)
t.fd(10)
t.lt(90)

t.color("black")
t.fd(50)

t.color("white")  # 감의 마무리
t.rt(90)
t.fd(10)
t.rt(90)

t.color("black")
t.fd(20)

t.color("white")
t.fd(10)

t.color("black")
t.fd(20)

t.color("white")      # 이 부분은 건의 시작을 좀 밑에서 하면서 자연스럽게 하기위해
t.fd(15)

t.lt(46)
t.fd(145)

t.color("black")   # 건의 시작
t.lt(65)
t.fd(55)

t.color("white")
t.rt(90)
t.fd(10)

t.color("black")
t.rt(90)
t.fd(55)

t.color("white")
t.lt(90)
t.fd(10)

t.color("black")    # 건의 마무리
t.lt(90)
t.fd(55)

t.color("white")
t.lt(26)              # 태극기 원을 그리기 위한 여정의 시작
t.fd(37)
t.lt(90)
t.fd(65)

t.lt(45)
n=100
t.color("red")                                     # 빨간 태극 문양 
t.begin_fill()
for x in range(n):
    t.rt(90 / n)
    t.fd((25 * math.sqrt(2) * (math.pi/2)) / n)      # 0.9도씩 꺾어서 호의길이만큼 이동
   
for y in range(n):    
    t.lt(90 / n)
    t.fd((25 * math.sqrt(2) * (math.pi / 2)) / n)   

t.lt(45)
 
for z in range(n):                                   # 1.8도씩 꺾어서 반원길이 만큼 이동                             
    t.lt(180 / n)
    t.fd((50 * math.pi )/n)                                         
t.end_fill()

t.lt(135)

t.color("blue")                                        #파란 태극문양
t.begin_fill()
for x in range(n):
    t.rt(90 / n)
    t.fd((25 * math.sqrt(2) * (math.pi/2)) / n)

for y in range(n):
    t.lt(90 / n)
    t.fd((25 * math.sqrt(2) * (math.pi / 2)) / n)

t.rt(137)

for z in range(n):
    t.rt(180 / n)
    t.fd((50 * math.pi )/n)
t.end_fill()
