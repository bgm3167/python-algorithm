# 콜라츠 추측
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12943
# 알고리즘: 시뮬레이션, 반복문
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:36:23

def solution(num):
    n = 0
    while num > 1:
        if n == 500:
            return -1
            break
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num +1
        n += 1
    return n