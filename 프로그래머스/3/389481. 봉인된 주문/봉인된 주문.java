import java.util.*;


class Solution {
    public long calculator(String word){
        char[] tmp_word = word.toCharArray();
        int length = word.length();
        long count = 0;
        long multiplier = 1;
        for (int i=length - 1;i >= 0;i--){
            count += multiplier * (tmp_word[i]-'a'+1);
            multiplier *= 26;
        }
        // System.out.println(count);  
        return count;
    }
    public String reverse(long index){
        StringBuilder sb = new StringBuilder();
        while(index > 0){
            index--;
            long remains = index % 26;
            sb.append((char) (remains + 'a'));
            index /= 26;
        }
        return sb.reverse().toString();
    }
    public String solution(long n, String[] bans) {
        String answer = "";
        // 26 진수 abcde fghij klmno pqrst uvwxy z
        long count = 0; // n 이하에서 삭제된 주문 개수 세기
        Arrays.sort(bans, (str1, str2) -> {
            if (str1.length() != str2.length()){
                return Integer.compare(str1.length(), str2.length());
            } else{
                return str1.compareTo(str2);   
            }
            });
        
        for (String word : bans){
            // System.out.println(word);
            long index = calculator(word);
            if(index <= n + count){
                count += 1;
            }
            
        }
        answer = reverse((long) (n+count));
        return answer;
    }
}