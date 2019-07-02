## Code 01
```C++
#include <string>
#include <vector>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    
    // 이중 반복문을 돌면서 전화번호 비교
    for (int i = 0; i < phone_book.size() - 1; ++i) {
        for (int j = i + 1; j < phone_book.size(); ++j) {
            string firstPhone = phone_book[i];
            string secondPhone = phone_book[j];
            
            // firstPhone이 secondPhone보다 짧은 경우
            if (firstPhone.length() < secondPhone.length()) {
                // fristPhone이 secondPhone의 접두사이면 false를 반환
                if (firstPhone == secondPhone.substr(0, firstPhone.length())) {
                    answer = false;
                    return answer;
                }
                
            } else{ // secondPhone이 firstPhone보다 짧거나 같은 경우
                // secondPhone이 firstPhone의 접두사이면 false를 반환
                if (secondPhone == firstPhone.substr(0, secondPhone.length())) {
                    answer = false;
                    return answer;
                }
            }
        }
    }
    return answer;
}
```

**결과**

- 정확성

테스트 1 〉	통과 (0.01ms, 3.75MB) <br/>
테스트 2 〉	통과 (0.01ms, 3.78MB) <br/>
테스트 3 〉	통과 (0.00ms, 3.76MB) <br/>
테스트 4 〉	통과 (0.00ms, 3.88MB) <br/>
테스트 5 〉	통과 (0.01ms, 3.77MB) <br/>
테스트 6 〉	통과 (0.00ms, 3.82MB) <br/>
테스트 7 〉	통과 (0.01ms, 3.76MB) <br/>
테스트 8 〉	통과 (0.00ms, 3.86MB) <br/>
테스트 9 〉	통과 (0.00ms, 3.75MB) <br/>
테스트 10 〉	통과 (0.00ms, 3.74MB) <br/>
테스트 11 〉	통과 (0.01ms, 3.77MB) <br/>

- 효율성

테스트 1 〉	통과 (0.40ms, 4.38MB) <br/>
테스트 2 〉	통과 (0.50ms, 4.26MB) <br/>

정확성: 84.6 <br/>
효율성: 15.4 <br/>
합계: 100.0 / 100.0 <br/>
