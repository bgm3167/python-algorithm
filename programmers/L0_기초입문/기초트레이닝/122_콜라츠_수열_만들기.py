# 콜라츠 수열 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181919
# 알고리즘: 반복문
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:05:53

def solution(n):
    answer = [n]
    while not n == 1:
        if n % 2 == 0:
            n /= 2
            answer.append(n)
        else:
            n = 3 * n + 1
            answer.append(n)
    return answer
            