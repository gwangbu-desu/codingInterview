class Solution {
    public int solution(int m, int n, int[][] puddles) {
        
        int answer = 0;
        try{
            boolean[][] new_pubble = new boolean[n][m];
            int[][] dp = new int[n][m];
            dp[0][0]=1;
            for(int[] puddle : puddles){
                int y = puddle[1];
                int x = puddle[0];
                new_pubble[y-1][x-1] = true;
            }
            for(int i=0;i<n;i++) {
                for(int j=0;j<m;j++){
                    if(new_pubble[i][j]) continue;
                    if(i==0 && j==0) continue;
                    if(i==0){
                        dp[i][j] = dp[i][j-1]; 
                    }
                    else if(j==0){
                        dp[i][j] = dp[i-1][j];
                    }
                    else{
                     
                        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1_000_000_007;   
                    }
                }
            }
            answer = dp[n-1][m-1];
            
        }catch(Exception e){
            e.printStackTrace();
        }finally{
            
            return answer;
        }
        
    }
}