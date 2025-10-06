import java.util.*;

class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        String changed_n = Integer.toString(n,k);
        // System.out.println(changed_n);
        // 진수 변환 -> 0기준으로 split -> 최대값을 기준으로 소수 계산
        String[] candidate_list = changed_n.split("0+");
        for(String c:candidate_list){
            System.out.println(c);
        }
        double[] candidate_int_list = Arrays.stream(candidate_list)
            .mapToDouble(Double::parseDouble).toArray();
        
        for(double i : candidate_int_list){
            if(isPrime(i)) answer++;
        }
        
        return answer;
    }
    public boolean isPrime(double n){
        if(n<=1) return false;
        else if (n<=3) return true;
        
        for(double i=2;i<=Math.sqrt(n);i++){
            if(n%i == 0) return false;
        }
        return true;
    }
}