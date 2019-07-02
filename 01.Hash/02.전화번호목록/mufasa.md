```java
import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        int bookLength = phone_book.length;
        for(int i=0;i<bookLength;i++){
            String phone1 = phone_book[i];
            for(int j=(i+1);j<phone_book.length;j++) {
                if(phone_book[j].indexOf(phone1) == 0) {
                    answer = false;
                    break;
                }
            }
        }
        return answer;
    }
}
```

테스트 1 〉	통과 (1.11ms, 45.7MB) <br/>
테스트 2 〉	통과 (1.00ms, 48.4MB) <br/>
테스트 3 〉	통과 (1.03ms, 44.4MB) <br/>
테스트 4 〉	통과 (1.07ms, 45.3MB)<br/>
테스트 5 〉	통과 (0.91ms, 48.1MB)<br/>
테스트 6 〉	통과 (0.99ms, 46.6MB)<br/>
테스트 7 〉	통과 (0.99ms, 44.8MB)<br/>
테스트 8 〉	통과 (0.97ms, 47.8MB)<br/>
테스트 9 〉	통과 (1.16ms, 45.6MB)<br/>
테스트 10 〉	통과 (0.99ms, 44.7MB)<br/>
테스트 11 〉	통과 (1.00ms, 45.1MB)<br/>
효율성  테스트<br/>
테스트 1 〉	통과 (460.80ms, 54.8MB)<br/>
테스트 2 〉	통과 (455.17ms, 54.4MB)<br/>
채점 결과<br/>
정확성: 84.6<br/>
효율성: 15.4<br/>
합계: 100.0 / 100.0<br/>