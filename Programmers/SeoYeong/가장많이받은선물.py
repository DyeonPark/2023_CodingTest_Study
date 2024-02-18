"""
input : 이번 달 선물 주고받은 기록
    ... 다음 달 선물 주고받을 기록 계산 ...
output : 다음 달 선물 가장 많이 받을 친구의 받을 선물 개수

if 선물주고받은기록 존재:
    이번 달 더 많이 준 사람이 다음 달에 하나 받기
elif 선물주고받은기록 없음 Or 선물주고받은개수 같음:
    선물지수 더 큰 사람이 작은 사람에게 하나 받기
    if 선물지수 같음:
        다음 달 선물 주고받지 않기

선물지수 = 이번 달 준 개수 - 받은 개수

선물받는 조건
- 선물 주고받은 기록 있을떼 선물 더 많이 줬으면 받음
- 선물 주고받은 기록 없으면
    - 선물 주고받은 수 같으면
        - 선물지수 더 크면 받음
"""

def solution(friends, gifts):
    answer = 0
    friend_to_idx = {f:i for i, f in enumerate(friends)}
    give_and_take = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for gift in gifts:
        giver, taker = gift.split()
        give_and_take[friend_to_idx[giver]][friend_to_idx[taker]] += 1

    answer = [0 for _ in range(len(friends))]

    for i in range(len(friends)):
        for j in range(len(friends)):      
            a_to_b = give_and_take[i][j]  
            b_to_a = give_and_take[j][i]
            a_gift_point = sum(give_and_take[i]) - sum(list(zip(*give_and_take))[i])
            b_gift_point = sum(give_and_take[j]) - sum(list(zip(*give_and_take))[j])

            if a_to_b > b_to_a or (a_to_b == b_to_a and a_gift_point > b_gift_point):
                answer[i]+=1

    return max(answer)

# 2
ans = solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]); print(ans)
# 4
ans = solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]); print(ans)
# 0
ans = solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]	); print(ans)