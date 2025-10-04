import java.util.*;

class Solution {
    public HashMap<String, Integer> dict = new HashMap<>();
    
    public int[] solution(String msg) {
        ArrayList<Integer> result = new ArrayList<>();
        int count = 1; // 보통 사전 인덱스는 1부터 시작
        
        // step1: A~Z 사전 초기화
        for (char a = 'A'; a <= 'Z'; a++) {
            dict.put(Character.toString(a), count++);
        }
        
        int i = 0;
        while (i < msg.length()) {
            int j = i + 1;
            // 사전에 있는 가장 긴 문자열 찾기
            while (j <= msg.length() && dict.containsKey(msg.substring(i, j))) {
                j++;
            }
            
            // 가장 긴 문자열 출력 (항상 dict에 존재함)
            String w = msg.substring(i, j - 1);
            result.add(dict.get(w));
            
            // 사전에 새로운 문자열 추가
            if (j <= msg.length()) {
                String newWord = msg.substring(i, j);
                dict.put(newWord, count++);
            }
            
            i += w.length(); // 다음 탐색 시작 위치 갱신
        }
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
