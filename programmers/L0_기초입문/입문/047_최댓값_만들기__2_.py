# 최댓값 만들기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120862
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 09:15:42

def solution(numbers):
    numbers.sort()

    return max(
        numbers[0] * numbers[1],
        numbers[-1] * numbers[-2]
    )
    
        