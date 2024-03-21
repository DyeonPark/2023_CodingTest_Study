"""
평균 -> 해당 값으로 학점 부여
- 자기 자신을 평가한 점수가 유일한 최고점 or 최저점:
    해당 점수 제외, 평균
- 
"""

def solution(scores):
    from collections import Counter
    result = ""
    tranpose_result = list(map(list, zip(*scores)))

    for i in range(len(tranpose_result)):
        student_i_score = tranpose_result[i]
        cnt_each_score = Counter(tranpose_result[i])
        max_score, min_score = max(student_i_score), min(student_i_score)
        total = sum(student_i_score)
        if (student_i_score[i] == max_score and cnt_each_score[max_score] == 1) \
        or (student_i_score[i] == min_score and cnt_each_score[min_score] == 1):
            print(f'exclude {student_i_score[i]}')
            total -= student_i_score[i]
            avg_score = total / (len(student_i_score)-1)
        else:
            avg_score = total / len(student_i_score)
        
        if avg_score >= 90: result+='A'
        elif avg_score >=80: result+='B'
        elif avg_score >=70: result+='C'
        elif avg_score >=50: result+='D'
        else: result+='F'
        print(student_i_score, avg_score, result)

    return result
        


scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# scores = [[50,90],[50,87]]
# scores = [[70,49,90],[68,50,38],[73,31,100]]

ans = solution(scores=scores); print(ans)