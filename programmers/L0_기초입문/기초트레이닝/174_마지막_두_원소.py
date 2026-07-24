# 마지막 두 원소
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181927
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 24. 14:13:46

def solution(num_list):
    s = (
        num_list[-1] - num_list[-2]
        if num_list[-1] > num_list[-2]
        else num_list[-1] * 2
    )

    num_list.append(s)
    return num_list