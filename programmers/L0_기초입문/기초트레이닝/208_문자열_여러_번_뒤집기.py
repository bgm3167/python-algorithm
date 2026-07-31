# 문자열 여러 번 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181913
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 31. 10:08:35

def solution(my_string, queries):
    for a, b in queries:
        my_string = (
            my_string[:a]
            + my_string[a:b + 1][::-1]
            + my_string[b + 1:]
        )
    
    return my_string
        