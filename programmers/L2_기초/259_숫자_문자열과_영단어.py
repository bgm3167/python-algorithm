# 숫자 문자열과 영단어
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 알고리즘: 문자열, 해시
# 작성자: 백관민
# 작성일: 2026. 08. 13. 11:39:05

def solution(s):
    words = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]

    for i in range(10):
        s = s.replace(words[i], str(i))

    return int(s)