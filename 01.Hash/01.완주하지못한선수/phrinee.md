```python

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append("n")
    n = 0
    for i in participant:
        if  i == completion[n]:
            n += 1
            continue
        answer = participant[n]

    return answer

```



# 정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.6MB)
테스트 3 〉	통과 (0.26ms, 10.9MB)
테스트 4 〉	통과 (0.54ms, 11MB)
테스트 5 〉	통과 (0.51ms, 11MB)
>
# 효율성  테스트
테스트 1 〉	통과 (41.12ms, 86.6MB)
테스트 2 〉	통과 (69.07ms, 126MB)
테스트 3 〉	통과 (86.03ms, 154MB)
테스트 4 〉	통과 (88.76ms, 166MB)
테스트 5 〉	통과 (90.12ms, 166MB)
# 채점 결과
정확성: 50.0
효율성: 50.0
합계: 100.0 / 100.0
