import java.util.*;

class Solution {
    HashMap<String,Integer> genreCount;
    class SongInfo implements Comparable<SongInfo>{
        String Genre;
        int SongCount;
        int idx;
        
        public SongInfo(String gc, int sc, int idx){
            this.Genre = gc;
            this.SongCount = sc;
            this.idx = idx;
        }
        
        @Override
        public int compareTo(SongInfo other) {
            if (!genreCount.get(this.Genre).equals(genreCount.get(other.Genre))) {
                return genreCount.get(other.Genre) - genreCount.get(this.Genre);
            }
            if (this.SongCount != other.SongCount) {
                return other.SongCount - this.SongCount;
            }
            return this.idx - other.idx;
        }
        @Override
        public String toString(){
            return this.Genre + this.SongCount + this.idx;
        }
    }
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();
        ArrayList<SongInfo> songList = new ArrayList<>();
        genreCount = new HashMap<>();
        for(int i=0; i<plays.length;i++){
            genreCount.put(genres[i], genreCount.getOrDefault(genres[i], 0) + plays[i]);
            songList.add(new SongInfo(genres[i], plays[i], i));
        }
        Collections.sort(songList);
        
        int beforeCount = 0;
        int cnt = 0;
        for(SongInfo i : songList){
            if (beforeCount == genreCount.get(i.Genre)){
                cnt ++;
            }else{
                cnt = 0;
                beforeCount = genreCount.get(i.Genre);
            }
            if (cnt >= 2){
                continue;
            }
            // System.out.println(cnt);
            answer.add(i.idx);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}

// 장르별로 2개씩.
// 정렬 기준 : 앨범 수록 기준 장르 count 높을 수록, 재생 count 높을 수록, 고유번호는 오름차순
