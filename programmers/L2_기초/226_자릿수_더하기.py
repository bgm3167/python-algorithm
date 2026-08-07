# 자릿수 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 알고리즘: 문자열, 반복문
# 작성자: 백관민
# 작성일: 2026. 08. 07. 14:10:25

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

   

