# 외계행성의 나이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 10:13:31

def solution(age):
    answer = ''

    for i in str(age):
        answer += chr(int(i) + 97)

    return answer
    
        