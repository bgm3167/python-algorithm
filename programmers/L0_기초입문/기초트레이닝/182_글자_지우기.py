# 글자 지우기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181900
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 15:25:28

def solution(my_string, indices):
    return ''.join(
        char for i, char in enumerate(my_string)
        if i not in indices
    )