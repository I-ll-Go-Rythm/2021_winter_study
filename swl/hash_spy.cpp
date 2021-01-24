#include <string>
#include <vector>
#include <map>
using namespace std;

int solution(vector<vector<string>> clothes) {
	int answer = 1;
	        
	map<string, int> ans;
		        
	for(int i = 0; i < clothes.size(); i++){
		ans[clothes[i][1]] ++;   
				        }
		        
        for(pair<string, int> i: ans)
	        answer = answer * (i.second + 1);
			    
	answer--;
      
	return answer;
}
