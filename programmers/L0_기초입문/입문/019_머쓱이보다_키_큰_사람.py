# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 12:29:00

def solution(array, height):
    return sum(1 for i in array if i > height)