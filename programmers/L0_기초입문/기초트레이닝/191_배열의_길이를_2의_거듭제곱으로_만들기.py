# 배열의 길이를 2의 거듭제곱으로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181857
# 알고리즘: 함수(메서드)
# 작성자: 백관민
# 작성일: 2026. 07. 30. 09:11:51

def solution(arr):
    n = 0
    while 2 ** n < len(arr):
        n += 1
    while len(arr) < 2 ** n:
        arr.append(0)
    return arr
        