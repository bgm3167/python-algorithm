# 평균 구하기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12944
# 알고리즘: 기본연산, 배열
# 작성자: 백관민
# 작성일: 2026. 08. 07. 13:52:18

def solution(arr):
    a = 0
    for i  in arr:
        a += i
    return a / len(arr)