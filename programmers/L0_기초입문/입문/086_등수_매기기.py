# 등수 매기기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120882
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 23. 09:21:42

def solution(score):
    total = [a + b for a, b in score]
    answer = []

    for s in total:
        rank = 1
        for t in total:
            if t > s:
                rank += 1
        answer.append(rank)

    return answer