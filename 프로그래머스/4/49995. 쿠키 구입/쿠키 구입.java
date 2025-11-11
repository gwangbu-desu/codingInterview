class Solution {
    public int solution(int[] cookie) {
        int answer = 0;
        int cl = cookie.length;
        // 누적합 + 3중 for문
        int[] sum_cookie = new int[cl+1];
        sum_cookie[0] = cookie[0];
        for(int i=1;i<cl;i++){
            sum_cookie[i] = cookie[i] + sum_cookie[i-1];
        }
        // for(int i:sum_cookie){
        //     System.out.printf("%d ",i);
        // }
        // System.out.println();
        // j < m < i
        for(int m = 0;m<cl-1;m++){
            int left = m;
            int right = m+1;
            int leftSum = cookie[left];
            int rightSum = cookie[right];
            while(true){
                if(leftSum == rightSum){
                    answer = Math.max(answer, leftSum);
                }
                
                if(leftSum <= rightSum && left > 0){
                    left--;
                    leftSum += cookie[left];
                }else if(leftSum >= rightSum && right<cl-1){
                    right++;
                    rightSum += cookie[right];
                }else{
                    break;
                }
            }
        }
        return answer;
    }
}