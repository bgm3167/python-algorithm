# 7의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120912
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 11:38:29

def solution(array):
    boot = ''

    for num in array:
        boot += str(num)

    return boot.count('7')