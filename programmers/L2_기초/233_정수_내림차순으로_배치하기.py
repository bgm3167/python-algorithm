# 정수 내림차순으로 배치하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 알고리즘: 문자열, 정렬
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:20:47

def solution(n):
    ans = ''
    for i in sorted(str(n))[::-1]:
        ans += i
    return int(ans)
            
    