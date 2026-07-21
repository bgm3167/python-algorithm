# 컨트롤 제트
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 14:20:34

def solution(s):
    answer = 0
    
    s = s.split()

    for i in range(len(s)):
        if s[i] == "Z":
            answer -= int(s[i-1])
        else:
            answer += int(s[i])

    return answer