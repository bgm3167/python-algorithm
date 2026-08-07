# 직사각형 별찍기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12969
# 알고리즘: 반복문
# 작성자: 백관민
# 작성일: 2026. 08. 07. 14:03:29

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*'*a)