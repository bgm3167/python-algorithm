# 문자열 정수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181849
# 알고리즘: 함수(메서드)
# 작성자: 백관민
# 작성일: 2026. 07. 24. 13:57:57

def solution(num_str):
    a = 0
    for i in num_str:
        a += int(i)
    
    return a
        
        