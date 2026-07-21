# 합성수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 10:28:26

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count > 2:
            answer += 1

    return answer