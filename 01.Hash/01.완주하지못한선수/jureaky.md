## Code 01
```C++
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    // 완주한 사람 목록을 훑으면서 참가자 목록에서 제거
    for (int i = 0; i < completion.size(); ++i) {
        string completed = completion[i];
        
        vector<string>::iterator iter;
        iter = find(participant.begin(), participant.end(), completed);
        
        participant.erase(iter);
    }
    
    // 참가자 목록에 남은 한 명이 완주하지 못한 사람
    answer = participant[0];
    return answer;
}
```

**결과**
- 정확성

테스트 1 〉	통과 (0.02ms, 3.75MB) <br/>
테스트 2 〉	통과 (0.01ms, 3.75MB) <br/>
테스트 3 〉	통과 (0.51ms, 3.83MB) <br/>
테스트 4 〉	통과 (2.13ms, 3.92MB) <br/>
테스트 5 〉	통과 (1.85ms, 3.91MB) <br/>

- 효율성

테스트 1 〉	실패 (시간 초과) <br/>
테스트 2 〉	실패 (시간 초과) <br/>
테스트 3 〉	실패 (시간 초과) <br/>
테스트 4 〉	실패 (시간 초과) <br/>
테스트 5 〉	실패 (시간 초과) <br/>

정확성: 50.0 <br/>
효율성: 0.0 <br/>
합계: 50.0 / 100.0 <br/>
