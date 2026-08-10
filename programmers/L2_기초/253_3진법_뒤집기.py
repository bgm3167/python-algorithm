# 3진법 뒤집기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 알고리즘: 수학, 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:48:03

def solution(n):
    ans = ''
    num = n
    dap = 0

    while num > 0:
        ans += str(num % 3)
        num //= 3

    for i in range(len(ans)):
        dap += int(ans[i]) * (3 ** (len(ans)-i-1))

    return dap
        
        