import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        HashMap<String,Integer> genreMap = new HashMap<>();
        PriorityQueue<int[]> ranking = new PriorityQueue<>((a,b) ->{
            if (b[0] != a[0]){            
                return b[0] - a[0];   
            }else{
                if(a[1] != b[1]){
                    return b[1] - a[1];
                }
                return a[2]-b[2];
            }
        });
        for(int i=0; i<genres.length;i++){
            genreMap.put(genres[i], genreMap.getOrDefault(genres[i],0) + plays[i]);
        }
        // 장르 랭킹 결정
        for(int i=0;i<plays.length;i++){
            ranking.add(new int[]{genreMap.get(genres[i]),plays[i],i});
        }
        List<Integer> tmp = new ArrayList<>();
        while(!ranking.isEmpty()){
            int genreTotal = ranking.peek()[0];
            for(int i=0;i<2;i++){
                if(ranking.isEmpty() || ranking.peek()[0] != genreTotal) break;
                tmp.add(ranking.poll()[2]);
            }
            while(!ranking.isEmpty() && ranking.peek()[0] == genreTotal) ranking.poll();
        }
        return tmp.stream().mapToInt(Integer::intValue).toArray();
    }
}