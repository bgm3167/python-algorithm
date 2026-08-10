# 수박수박수박수박수박수?
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12922
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:11:53

def solution(n):
    answer = ''
    x = 0
    while x < n:
        if x % 2 == 0:
            answer += '수'
        else:
            answer += '박'
        x += 1
    return answer