# 가장 가까운 같은 글자
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 알고리즘: 해시
# 작성자: 백관민
# 작성일: 2026. 08. 14. 09:20:13

def solution(s):
    answer = []
    last = {}  # 각 문자가 마지막으로 나온 위치

    for i, char in enumerate(s):
        if char in last:
            answer.append(i - last[char])
        else:
            answer.append(-1)

        last[char] = i

    return answer