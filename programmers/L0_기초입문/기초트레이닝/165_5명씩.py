# 5명씩
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181886
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:38:01

def solution(names):
    answer = []
    for i in range(len(names)):
        if i % 5 == 0:
            answer.append(names[i])
    return answer