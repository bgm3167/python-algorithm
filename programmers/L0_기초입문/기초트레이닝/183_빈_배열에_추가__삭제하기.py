# 빈 배열에 추가, 삭제하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181860
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 30. 10:01:37

def solution(arr, flag):
    X = []

    for i in range(len(arr)):
        if flag[i]:
            X.extend([arr[i]] * (arr[i] * 2))
        else:
            del X[-arr[i]:]

    return X
            
 