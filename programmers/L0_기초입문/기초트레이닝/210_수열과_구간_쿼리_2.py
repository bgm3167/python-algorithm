# 수열과 구간 쿼리 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181923
# 알고리즘: 반복문
# 작성자: 백관민
# 작성일: 2026. 07. 31. 10:32:52

def solution(arr, queries):
    ans = []
    for i in queries:
        a,b,c = i
        ytn = []
        for j in range(a,b+1):
            if arr[j] > c:
                ytn.append(arr[j])
        if len(ytn) == 0:
            ans.append(-1)
        else:
            ans.append(min(ytn))
    return ans
            