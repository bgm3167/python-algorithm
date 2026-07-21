# 약수 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 09:29:15

def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.append(i)
    return answer
        