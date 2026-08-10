# 두 정수 사이의 합
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 알고리즘: 수학
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:30:40

def solution(a, b):
    ans = 0
    if a >= b:
        for i in range(b,a+1):
            ans += i
    else:
        for i in range(a,b+1):
            ans += i      
    return ans