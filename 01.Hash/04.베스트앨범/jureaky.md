## Code 01

```C++

#include <string>
#include <vector>
#include <utility>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    
    // 장르, 재생횟수 저장 테이블
    vector<pair<string, int>> genresPlays;
    
    for (int i = 0; i < genres.size(); ++i) {
        string genre = genres[i];
        bool isExistGenre = false;
        for (int j = 0; j < genresPlays.size(); ++j) {
            if (genre == genresPlays[j].first) {
                isExistGenre = true;
                genresPlays[j].second += plays[i];
                break;
            }
        }
        if (!isExistGenre) {
            genresPlays.push_back(make_pair(genre, plays[i]));
        }
    }
    
    int numGenres = genresPlays.size();
    while(numGenres > 0) {
        int maxPlays = -1;
        int maxGenreIndex = -1;
        string maxGenre;
        
        for (int i = 0; i < genresPlays.size(); ++i) {
            if (maxPlays < genresPlays[i].second) {
                maxGenre = genresPlays[i].first;
                maxPlays = genresPlays[i].second;
                maxGenreIndex = i;
            }
        }
        genresPlays[maxGenreIndex].second = -987654321;
        
        int maxSongPlays = -1;
        int nextMaxSongPlays = -2;
        
        int maxSongPlaysIndex = -1;
        int nextMaxSongPlaysIndex = -2;
        
        bool isFound = true;
        int songCount = 1;
        while (isFound) {
            int maxSongPlays = -1;
            int maxSongPlaysIndex = -1;
            for (int i = 0; i < plays.size(); ++i) {
                if ((genres[i] == maxGenre) && (maxSongPlays < plays[i])) {
                    if (!isFound) {
                        isFound = true;
                    }
                    maxSongPlays = plays[i];
                    maxSongPlaysIndex = i;
                }
            }
            if (maxSongPlays == -1) {
                isFound = false;
            } else {
                songCount++;
            }
            
            if (isFound) {
                plays[maxSongPlaysIndex] = -987654321;
            }
            
            if (isFound) {
                answer.push_back(maxSongPlaysIndex);
            }
            
            if (songCount > 2) {
                break;
            }
            
        }
       
        numGenres--;
    }
    return answer;
}
```

**결과**

- 정확성


테스트 1 〉	통과 (0.01ms, 3.78MB) <br/>
테스트 2 〉	통과 (0.01ms, 3.77MB) <br/>
테스트 3 〉	통과 (0.01ms, 3.76MB) <br/>
테스트 4 〉	통과 (0.00ms, 3.82MB) <br/>
테스트 5 〉	통과 (0.01ms, 3.74MB) <br/>
테스트 6 〉	통과 (0.02ms, 3.91MB) <br/>
테스트 7 〉	통과 (0.01ms, 3.89MB) <br/>
테스트 8 〉	통과 (0.01ms, 3.8MB) <br/>
테스트 9 〉	통과 (0.01ms, 3.79MB) <br/>
테스트 10 〉	통과 (0.02ms, 3.91MB) <br/>
테스트 11 〉	통과 (0.01ms, 3.91MB) <br/>
테스트 12 〉	통과 (0.01ms, 3.68MB) <br/>
테스트 13 〉	통과 (0.02ms, 3.82MB) <br/>
테스트 14 〉	통과 (0.02ms, 3.75MB) <br/>
테스트 15 〉	통과 (0.01ms, 3.78MB) <br/>

정확성: 100.0 <br/>
합계: 100.0 / 100.0 <br/>
