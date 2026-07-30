# 문자열 반복해서 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181950
# 알고리즘: 출력
# 작성자: 백관민
# 작성일: 2026. 07. 31. 08:53:58

str, n = input().strip().split(' ')
n = int(n)

print(''.join(str * n))
