class Solution {
    public int[] left = {3,0};
    public int[] right = {3,2};
    // 0, 1,2,3,4,5,6,7,8,9
    public int[][] number = {{3,1},{0,0},{0,1},{0,2},{1,0},{1,1},{1,2},{2,0},{2,1},{2,2}};
    public String solution(int[] numbers, String hand) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for(int i : numbers){
            if ( i == 1 || i == 4 || i == 7){
                // 왼손
                left[0] = number[i][0];
                left[1] = 0;
                sb.append("L");
            }else if(i==3 || i ==6||i==9){
                // 오른손
                right[0] = number[i][0];
                right[1] = 2;
                sb.append("R");
            }else{
                // 가운데
                int left_distance = 0;
                int right_distance = 0;
                
                left_distance = Math.abs(number[i][0]-left[0]) + Math.abs(number[i][1] - left[1]);
                right_distance = Math.abs(number[i][0]-right[0]) + Math.abs(number[i][1] - right[1]);
                
                if(left_distance < right_distance){
                    left[0] = number[i][0];
                    left[1] = number[i][1];
                    sb.append("L");
                }else if(right_distance < left_distance){
                    right[0] = number[i][0];
                    right[1] = number[i][1];
                    sb.append("R");
                } else{
                    // 거리가 같을때 -> hand를 기준으로
                    if( hand.equals("left")){
                        left[0] = number[i][0];
                        left[1] = number[i][1];
                        sb.append("L");
                    }else{
                        right[0] = number[i][0];
                        right[1] = number[i][1];
                        sb.append("R");
                    }
                }
            }
            System.out.printf("%d %d %d %d\n",left[0],left[1], right[0],right[1]);
        }
        return sb.toString();
    }
    public boolean check(int r, int c){
        return 0 <= r && r < 4 && 0<= c && c < 3;
    }
}