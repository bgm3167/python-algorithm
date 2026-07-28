# 배열의 원소만큼 추가하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181861
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 28. 13:49:55

def solution(arr):
    answer = []
    for i in arr:
        n = 1
        while n <= i: 
            answer.append(i)
            n += 1
    return answer