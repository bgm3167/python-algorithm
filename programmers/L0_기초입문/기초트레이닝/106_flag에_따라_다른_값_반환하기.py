# flag에 따라 다른 값 반환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181933
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 24. 10:20:22

def solution(a, b, flag):
    return(a+b if flag == True else a-b)