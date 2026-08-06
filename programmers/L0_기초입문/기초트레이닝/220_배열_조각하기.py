# 배열 조각하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181893
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 08. 06. 10:05:07

def solution(arr, query):
    for i, q in enumerate(query):
        if i % 2 == 0:
            arr = arr[:q + 1]
        else:
            arr = arr[q:]

    return arr