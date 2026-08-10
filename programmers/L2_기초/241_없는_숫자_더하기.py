# 없는 숫자 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86051
# 알고리즘: 배열, 해시
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:07:10

def solution(numbers):
    ans = 45
    for i in numbers:
        ans -= i
    return ans
        
        