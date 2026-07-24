# 배열의 길이에 따라 다른 연산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181854
# 알고리즘: 함수(메서드)
# 작성자: 백관민
# 작성일: 2026. 07. 24. 16:09:00

def solution(arr, n):
    target = 0 if len(arr) % 2 == 1 else 1

    return [
        value + n if index % 2 == target else value
        for index, value in enumerate(arr)
    ]
   
    