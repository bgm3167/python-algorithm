# 피자 나눠 먹기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 10:05:49

def solution(n):
    answer = 1
    while True:
        if answer * 6 % n == 0:
            return answer
            break
        else:
            answer += 1
        