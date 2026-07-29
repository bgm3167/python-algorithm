# 할 일 목록
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181885
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:35:52

def solution(todo_list, finished):
    result =[]
    for i in range(len(todo_list)):
        if int(finished[i]) == 0:
            result.append(todo_list[i])
    return result
            