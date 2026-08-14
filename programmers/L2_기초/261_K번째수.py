# K번째수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 알고리즘: 정렬
# 작성자: 백관민
# 작성일: 2026. 08. 14. 09:17:46

def solution(array, commands):
    ans = []
    for i in commands:
        ans.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return ans