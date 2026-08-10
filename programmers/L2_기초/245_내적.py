# 내적
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/70128
# 알고리즘: 배열, 수학
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:12:47

def solution(a, b):
    ans = 0
    for i in range(len(a)):
        ans += a[i]*b[i]
    return ans
        