nclude <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
	    sort(phone_book.begin(), phone_book.end());
	        for(unsigned int i = 0; i< phone_book.size()-1; i++){
			        if(to_string(stoi(phone_book[i])+1)>phone_book[i+1]) return false;
				    }
		    return true;
}
