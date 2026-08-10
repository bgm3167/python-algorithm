# 정수 제곱근 판별
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 알고리즘: 수학
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:15:23

import math
def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return ((math.sqrt(n)+1)**2)
    return -1