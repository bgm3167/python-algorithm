# 0 떼기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181847
# 알고리즘: 함수(메서드)
# 작성자: 백관민
# 작성일: 2026. 07. 24. 12:31:52

def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != "0":
            return n_str[i:]