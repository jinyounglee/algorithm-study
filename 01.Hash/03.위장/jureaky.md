## Code 01

```C++
#include <string>
#include <vector>
#include <utility>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 0;
    
    // 의상 종류, 의상 수의 pair 정보를 저장할 테이블
    vector<pair<string, int>> table;
    
    for (int i = 0; i < clothes.size(); ++i) {
        string type = clothes[i][1];
        string name = clothes[i][0];
        
        // 테이블에서 종류를 찾으면 개수를 추가
        bool isExist = false;
        for (int j = 0; j< table.size(); ++j) {
            if (table[j].first == type) {
                isExist = true;
                table[j].second++;
            }
        }
        
         // 테이블에 없으면 새로 테이블에 추가
        if (!isExist) {
            table.push_back(make_pair(type, 1));
        }
       
    }
    
    // 조합: (의상1 수 + 1) * (의상2 수 + 1) * ... * (의상n 수 + 1) - 1
    answer = 1;
    for (int i = 0; i < table.size(); ++i) {
        answer *= (table[i].second + 1);
    }
    answer--;
    return answer;
}
```

**결과**

- 정확성

테스트 1 〉	통과 (0.02ms, 3.77MB) <br/>
테스트 2 〉	통과 (0.01ms, 3.91MB) <br/>
테스트 3 〉	통과 (0.01ms, 3.78MB) <br/>
테스트 4 〉	통과 (0.01ms, 3.85MB) <br/>
테스트 5 〉	통과 (0.01ms, 3.8MB) <br/>
테스트 6 〉	통과 (0.01ms, 3.73MB) <br/>
테스트 7 〉	통과 (0.02ms, 3.7MB) <br/>
테스트 8 〉	통과 (0.03ms, 3.76MB) <br/>
테스트 9 〉	통과 (0.01ms, 3.82MB) <br/>
테스트 10 〉	통과 (0.01ms, 3.75MB) <br/>
테스트 11 〉	통과 (0.01ms, 3.89MB) <br/>
테스트 12 〉	통과 (0.01ms, 3.83MB) <br/>
테스트 13 〉	통과 (0.02ms, 3.73MB) <br/>
테스트 14 〉	통과 (0.01ms, 3.86MB) <br/>
테스트 15 〉	통과 (0.01ms, 3.73MB) <br/>
테스트 16 〉	통과 (0.00ms, 3.75MB) <br/>
테스트 17 〉	통과 (0.01ms, 3.74MB) <br/>
테스트 18 〉	통과 (0.01ms, 3.82MB) <br/>
테스트 19 〉	통과 (0.01ms, 3.81MB) <br/>
테스트 20 〉	통과 (0.01ms, 3.71MB) <br/>
테스트 21 〉	통과 (0.01ms, 3.82MB) <br/>
테스트 22 〉	통과 (0.00ms, 3.74MB) <br/>
테스트 23 〉	통과 (0.01ms, 3.77MB) <br/>
테스트 24 〉	통과 (0.01ms, 3.76MB) <br/>
테스트 25 〉	통과 (0.01ms, 3.75MB) <br/>
테스트 26 〉	통과 (0.02ms, 3.76MB) <br/>
테스트 27 〉	통과 (0.01ms, 3.81MB) <br/>
테스트 28 〉	통과 (0.01ms, 3.89MB) <br/>

정확성: 100.0 <br/>
합계: 100.0 / 100.0 <br/>
