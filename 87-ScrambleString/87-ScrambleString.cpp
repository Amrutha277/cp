// Last updated: 7/27/2025, 8:42:32 PM
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int n = points.size();
        if(n<= 2){
            return n;
        }
        int maxResult = 0;

        for(int i = 0; i<n; i++){
            unordered_map<string, int> slopeCount ;
            int duplicates = 1;
            int vertical = 0;
            int localMax = 0;
            for(int j = i+1;j<n;j++){
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];
                if(dx == 0 && dy == 0){
                    duplicates++;
                }else{
                    int gcd = __gcd(dx,dy);
                    dx = dx/gcd;
                    dy = dy/gcd;
                    if(dx<0){
                        dx = -dx;
                        dy = -dy;
                    }
                    string slopeKey = to_string(dy) + "/" + to_string(dx);
                    slopeCount[slopeKey]++;
                    localMax = max(localMax, slopeCount[slopeKey]);
                }
            }
            maxResult = 
            max(maxResult,localMax+duplicates);
        }
        return maxResult;
        //O(n2)
        
    }
};