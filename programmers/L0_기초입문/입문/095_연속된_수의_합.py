# 연속된 수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 27. 09:42:33

def solution(num, total):
    a = 0
    b = []
    for i in range(1,num):
        a += i
    ans = (total - a) / num
    for k in range(num):
        b.append(ans+k)
    return b
        