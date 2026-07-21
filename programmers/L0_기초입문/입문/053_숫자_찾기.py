# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 09:45:19

def solution(num, k):
    num = str(num)
    k = str(k)

    return num.index(k) + 1 if k in num else -1