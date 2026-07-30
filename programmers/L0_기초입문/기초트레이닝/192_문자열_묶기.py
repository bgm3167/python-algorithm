# 문자열 묶기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181855
# 알고리즘: 함수(메서드)
# 작성자: 백관민
# 작성일: 2026. 07. 30. 09:07:18

def solution(strArr):
    count = {}

    for s in strArr:
        length = len(s)
        count[length] = count.get(length, 0) + 1

    return max(count.values())