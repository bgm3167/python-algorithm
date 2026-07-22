# 구슬을 나누는 경우의 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120840
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 10:28:29

def solution(balls, share):
    share = min(share, balls - share)
    answer = 1

    for i in range(1, share + 1):
        answer = answer * (balls - share + i) // i

    return answer