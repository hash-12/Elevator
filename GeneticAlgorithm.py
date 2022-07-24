import random
import math

fitness_meter = None
generation = []

# 사용자 설정
def set_fitness_meter(func):
    global fitness_meter 
    fitness_meter = func

# 첫 세대 생성
def generate_generation(range, pool_size):
    global generation
    for i in range(pool_size):
        generation.append(random.choice(range))

# 시뮬레이션 시작
def start(gen_size):
    global fitness_meter, generation


    if(fitness_meter == None):
        print("적합도 측정 함수가 지정되지 않았습니다.")
        return
    if not generation:
        print("첫 세대가 생성되지 않았습니다.")
        return


    for gen in range(gen_size):

        # 선택
        score = {}
        for i in generation:
            score[i] = fitness_meter(i)

        score = sorted(score, key = lambda x : score[x])






# 선택


# 교차

# 변이

