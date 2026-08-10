# 핸드폰 번호 가리기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:50:33

def solution(phone_number):
    ans = ''
    a = len(phone_number) 
    ans += '*'*(a-4) + phone_number[a-4::]
    return ans