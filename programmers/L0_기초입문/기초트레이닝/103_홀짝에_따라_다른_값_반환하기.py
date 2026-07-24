# 홀짝에 따라 다른 값 반환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181935
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 24. 10:09:47

def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(1,n+1,2):
            answer += i
    else:
        for i in range(0,n+1,2):
            answer += i**2
            
    return answer