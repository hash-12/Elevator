'''
<작동 방식에 대한 간략한 설명>

엘리베이터는 엘리베이터 객체를 통해 구현

엘리베이터 객체의 구성 변수 = {
    limit: 엘리베이터 정원
    condition: 엘리베이터의 현재 상태(정지, 상승, 하강)
    order_up: 현재 엘리베이터에 요청된 위층으로 이동하며 멈춰야 하는 층들의 리스트
    order_down: 현재 엘리베이터에 요청된 아래층으로 이동하며 멈춰야 하는 층들의 리스트
    elevator: 엘리베이터 내부 탑승자들의 리스트
    location: 엘리베이터의 현재 층
}

엘리베이터는 정지, 상승, 하강 상태 중 하나임
1. 엘리베이터가 정지 상태일 경우(condition == 'stop'인 경우) 명령을 대기함
2. 엘리베이터가 상승 상태일 경우(condition == 'up'인 경우) order_up 리스트를 하나씩 읽어 가며 해당 층에 정지, order_up리스트가 비어 있을 때까지 층을 올라감
3. 엘리베이터가 하강 상태일 경우(condition == 'down'인 경우) order_down 리스트를 하나씩 읽어 가며 해당 층에 정지, order_down리스트가 비어 있을 때까지 층을 내려감

run_elevator 함수를 실행할 경우 다음을 루프한다

1. 엘리베이터가 정지 상태일 경우 명령을 대기
    명령은 한 번에 여러 개 입력할 수 있음
    명령은 2개의 정수로 구성되며 튜플로 읽어들여짐 (탑승하는 하는 층, 내리고자 하는 층)
    명령 입력이 완료될 경우 end입력
    명령은 입력된 순서대로 읽어들여짐
    정지 상태에서 들어온 탑승하고자 하는 층, 내리고자 하는 층은 현재 엘리베이터의 위치에 따라 order_up리스트 또는 order_down리스트에 삽입됨
1. 정지 상태가 아닐 경우에도 새로운 명령을 입력 받음

2. 엘리베이터가 상승 상태일 경우
    order_up리스트가 비어있지 않다면 order_up[0]에 있는 층으로 이동 / 비어있다면 condition = 'stop'
    이후 order_up.pop(0)

3. 엘리베이터가 하강 상태일 경우
    order_down리스트가 비어있지 않다면 order_down[0]에 있는 층으로 이동 / 비어있다면 condition = 'stop'
    이후 order_down.pop(0)

궁극적으로 run_elevator 함수는 입력된 대기자들이 대기한 총 시간을 return함
대기자들이 대기한 총 시간은 waitTime변수에 담김
대기한 시간을 계산하는 방법은 다음과 같음
1. 엘리베이터에 명령이 들어왔을 경우 명령이 들어온 시각을 해당 튜플과 함께 저장
2. 엘리베이터에서 내릴 때의 시각 - 엘리베이터에 탑승할 때의 시각을 waitTime에 더함

'''


import random
import math
import GeneticAlgorithm

class Elevator:
    limit = 16 # 엘리베이터 정원
    order_up = []
    order_down = []

    elevator = [] # 엘리베이터 내부
    condition = 'stop'
    location = 1


def time_calculator(beforeFloor, afterFloor):
    t = None
    # 계산식 추가
    return t
    

def run_elevator():
    elevator = Elevator()

    t = 0 # 경과 시간
    waitTime = 0 # 대기 시간의 총합

      
    while(True):

        # 정지 상태
        if elevator.condition == 'stop':
            order = input()
            while order != 'end':
                if(order > elevator.location):
                    elevator.order_up.append(order)
                    sorted(elevator.order_up)
                    elevator.condition = 'up'
                if(order < elevator.location):
                    elevator.order_down.append(order)
                    sorted(elevator.order_down)
                    elevator.condition = 'down'
        else:
            order = input()
            while order != 'end':
                if(order > elevator.location):
                    elevator.order_up.append(order)
                    sorted(elevator.order_up)
                if(order < elevator.location):
                    elevator.order_down.append(order)
                    sorted(elevator.order_down)

        # 상승 상태
        if elevator.condition == 'up':
            if not elevator.order_up:
                t += time_calculator(elevator.location, elevator.order_up[0])
                elevator.location = elevator.order_up[0]
                elevator.order_up.pop(0)
            else:
                elevator.condition = 'stop'
                
        # 하강 상태
        if elevator.condition == 'down':
            if not elevator.order_down:
                t += time_calculator(elevator.location, elevator.order_down[0])
                elevator.location = elevator.order_down[0]
                elevator.order_down.pop(0)
            else:
                elevator.condition = 'stop'

        print("----------------------------------------")
        print("엘리베이터의 현재 위치:", elevator.location)
        print("엘리베이터 내부:")
        for i in elevator.elevator:
            print(i)
        print("order_up:")
        for i in elevator.elevator:
            print(i)
        



