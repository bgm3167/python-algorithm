# 문자 개수 세기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181902
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 31. 10:02:47

def solution(my_string):
    answer = [0] * 52

    for ch in my_string:
        if 'A' <= ch <= 'Z':
            answer[ord(ch) - ord('A')] += 1
        else:
            answer[26 + ord(ch) - ord('a')] += 1

    return answer
        