# 최빈값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120812
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 27. 09:36:34

def solution(array):
    counts = {}

    # 각 숫자의 등장 횟수 세기
    for num in array:
        counts[num] = counts.get(num, 0) + 1

    # 가장 많이 등장한 횟수
    max_count = max(counts.values())

    # 가장 많이 등장한 숫자들
    modes = [num for num, count in counts.items() if count == max_count]

    # 최빈값이 하나면 반환, 여러 개면 -1
    if len(modes) == 1:
        return modes[0]
    return -1