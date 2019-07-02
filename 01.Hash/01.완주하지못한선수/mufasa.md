```javascript
function solution(participant, completion) {
    participant.sort();
    completion.sort();

    for(let i = 0; i < participant.length; i+=1 ) {
        if(participant[i] !== completion[i]) {
            return participant[i]
        }
    }
}
```

같은 코드로 채점한 결과가 있습니다. <br/>
정확성  테스트 <br/>
테스트 1 〉	통과 (2.31ms, 36.7MB) <br/>
테스트 2 〉	통과 (2.36ms, 36.9MB) <br/>
테스트 3 〉	통과 (4.17ms, 37.2MB) <br/>
테스트 4 〉	통과 (8.86ms, 37.8MB) <br/>
테스트 5 〉	통과 (7.34ms, 37.6MB) <br/>
효율성  테스트 <br/>
테스트 1 〉	통과 (94.38ms, 52.9MB) <br/>
테스트 2 〉	통과 (172.37ms, 60.7MB) <br/>
테스트 3 〉	통과 (208.36ms, 67.7MB) <br/>
테스트 4 〉	통과 (222.06ms, 69.5MB) <br/>
테스트 5 〉	통과 (183.72ms, 69.5MB) <br/>
채점 결과 <br/>
정확성: 50.0 <br/>
효율성: 50.0 <br/>
합계: 100.0 / 100.0 <br/>
