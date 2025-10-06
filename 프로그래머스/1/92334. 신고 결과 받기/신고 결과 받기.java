import java.util.*;
class Solution {
    public HashMap<String, Integer> reportCount = new HashMap<>();
    public HashMap<String, Integer> id_idx = new HashMap<>();
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = {};
        int[] sum = new int[id_list.length];
        Set<String> reportSet = new HashSet<>(Arrays.asList(report));
        // 신고횟수 누적
        for(String r : reportSet){
            String[] split = r.split(" ");
            String reported = split[1];
            reportCount.put(reported, reportCount.getOrDefault(reported,0) + 1);
        }
        // k 보다 높은 목록 찾기
        List<String> banned = new ArrayList<>();
        for(int idx = 0; idx < id_list.length;idx++){
            id_idx.put(id_list[idx],idx);
            if(reportCount.getOrDefault(id_list[idx],0) >= k){
                banned.add(id_list[idx]);
            }
        }
        for(String r : reportSet){
            String split[] = r.split(" ");
            String reportee = split[0];
            String reported = split[1];
            if( banned.contains(reported)){
                sum[id_idx.get(reportee)]++;   
            }
        }
        
        return sum;
    }
}