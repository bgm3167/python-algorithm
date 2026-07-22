# 외계어 사전
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120869
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 10:44:42

def solution(spell, dic):
    for word in dic:
        if all(ch in word for ch in spell):
            return 1
    return 2
                