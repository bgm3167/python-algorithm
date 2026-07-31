# 그림 확대
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181836
# 알고리즘: 반복문 활용
# 작성자: 백관민
# 작성일: 2026. 07. 31. 16:04:15

def solution(picture, k):
    answer = []

    for row in picture:
        expanded_row = ''.join(char * k for char in row)

        for _ in range(k):
            answer.append(expanded_row)

    return answer