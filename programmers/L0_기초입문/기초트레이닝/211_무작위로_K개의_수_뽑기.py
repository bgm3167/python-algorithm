# 무작위로 K개의 수 뽑기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181858
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 31. 15:31:23

def solution(arr, k):
    answer = []

    for num in arr:
        if num not in answer:
            answer.append(num)

        if len(answer) == k:
            break

    while len(answer) < k:
        answer.append(-1)

    return answer