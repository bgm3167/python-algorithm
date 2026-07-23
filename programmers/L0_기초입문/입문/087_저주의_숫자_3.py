# 저주의 숫자 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120871
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 23. 09:27:53

def solution(n):
    num = 0
    count = 0

    while count < n:
        num += 1

        if num % 3 == 0 or "3" in str(num):
            continue

        count += 1

    return num