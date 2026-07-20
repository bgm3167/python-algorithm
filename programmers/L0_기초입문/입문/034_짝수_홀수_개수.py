# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 11:38:28

def solution(num_list):
    answer = [0, 0]

    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer