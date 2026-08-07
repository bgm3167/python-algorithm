# 나머지가 1이 되는 수 찾기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87389
# 알고리즘: 수학, 반복문
# 작성자: 백관민
# 작성일: 2026. 08. 07. 14:13:05

def solution(n):
    for i in range(2,n+1):
        if n % i == 1:
            return i