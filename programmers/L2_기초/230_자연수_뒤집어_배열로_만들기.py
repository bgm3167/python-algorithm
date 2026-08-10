# 자연수 뒤집어 배열로 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 알고리즘: 문자열, 배열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:11:51

def solution(n):
    return [int(x) for x in str(n)[::-1]]