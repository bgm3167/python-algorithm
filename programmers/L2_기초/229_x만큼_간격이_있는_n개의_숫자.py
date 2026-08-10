# x만큼 간격이 있는 n개의 숫자
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 알고리즘: 배열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:08:02

def solution(x, n):
     return [x * i for i in range(1, n + 1)]