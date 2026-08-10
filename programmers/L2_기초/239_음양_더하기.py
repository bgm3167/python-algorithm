# 음양 더하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 알고리즘: 배열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:44:06

def solution(absolutes, signs):
    ans = 0
    for i in range(len(signs)):
        if signs[i] == True:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]
    return ans