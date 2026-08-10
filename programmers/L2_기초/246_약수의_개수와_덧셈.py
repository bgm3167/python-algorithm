# 약수의 개수와 덧셈
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 알고리즘: 수학
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:17:33

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        ver = 0
        for j in range(1,i+1):
            if i % j == 0:
                ver += 1
        if ver % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
        