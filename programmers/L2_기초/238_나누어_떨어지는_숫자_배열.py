# 나누어 떨어지는 숫자 배열
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12910
# 알고리즘: 배열, 정렬
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:39:57

def solution(arr, divisor):
    ans = []
    for i in arr:
        if i % divisor == 0:
            ans.append(i)
    if len(ans) > 0:
        return sorted(ans)
    return [-1]
        