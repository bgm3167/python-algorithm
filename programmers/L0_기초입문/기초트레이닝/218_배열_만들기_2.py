# 배열 만들기 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181921
# 알고리즘: 반복문
# 작성자: 백관민
# 작성일: 2026. 08. 06. 09:57:38

def solution(l, r):
    answer = []

    for num in range(l, r + 1):
        if all(digit in ('0', '5') for digit in str(num)):
            answer.append(num)

    return answer if answer else [-1]
            