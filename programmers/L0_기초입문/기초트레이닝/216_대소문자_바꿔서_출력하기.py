# 대소문자 바꿔서 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181949
# 알고리즘: 출력
# 작성자: 백관민
# 작성일: 2026. 08. 06. 09:52:15

str = input()
ans = ''

for i in str:
    if ord(i) < 97:
        ans += i.lower()
    else:
        ans += i.upper()
print(ans)
        