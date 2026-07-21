# 2차원으로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120842
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 10:35:41

def solution(num_list, n):
    answer = []

    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])

    return answer