// Last updated: 7/27/2025, 8:12:38 PM
class Solution {
public:
    unordered_map<string,bool> memo;
    bool isScramble(string s1, string s2) {
        //dp with memoisation
        

        if(s1 == s2){
            return true;
        }
        string key = s1 + "" + s2;
        if(memo.count(key)){
            return memo[key];
        }
        
        // if(s1.size() != s2.size()){
        //     (return) false;
        // }
        string sorted1 = s1;
        string sorted2 = s2;
        sort(sorted1.begin(),sorted1.end());
        sort(sorted2.begin(),sorted2.end());
        if(sorted1 != sorted2){

            return memo[key] = false;
        }
        int n = s1.size();
        for(int i = 1; i<n ; i++){
            // no swap
            if(isScramble(s1.substr(0,i),s2.substr(0,i)) && isScramble(s1.substr(i),s2.substr(i))){
                return memo[key] = true;
            }

            // swap
            if(isScramble(s1.substr(0,i),s2.substr(n-i)) && isScramble(s1.substr(i),s2.substr(0,n-i))){
                return memo[key] = true;
            }
        }
        return memo[key] = false;
        //Time complexity:O(N^4) worst case
       // space O(N^3)n-
    }
};