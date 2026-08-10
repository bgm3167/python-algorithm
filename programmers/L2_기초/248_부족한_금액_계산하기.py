# 부족한 금액 계산하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 알고리즘: 수학
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:22:45

def solution(price, money, count):
    ans = 0
    for i in range(1,count+1):
        ans += price * i
    if ans > money :
        return ans - money
    return 0
        