# 특이한 정렬
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120880
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 23. 16:25:29

def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x - n), -x))