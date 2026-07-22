# 삼각형의 완성조건 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120868
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 10:18:16

def solution(sides):
    sides.sort()
    answer = 0
    for i in range(1,sides[0]+sides[1]):
        if i < sides[1]:
            if i + sides[0] > sides[1]:
                answer += 1
        else:
            if i < sides[0] +sides[1]:
                answer += 1
                
    return answer
            
            
        