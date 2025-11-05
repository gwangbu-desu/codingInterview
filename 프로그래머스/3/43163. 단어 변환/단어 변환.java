import java.util.*; 
class Solution {
    class Word{
        String word;
        int step;
        public Word(String word, int step){
            this.word = word;
            this.step = step;
        }
        public boolean change_possible(String next){
            int count = 0;
            for(int i=0;i<next.length();i++){
                if(this.word.charAt(i) != next.charAt(i)){
                    System.out.printf("%c, %c\n", this.word.charAt(i), next.charAt(i));
                    count++;
                }
            }
            System.out.printf("%s, %s, %d\n", this.word, next, count);
            return count == 1;// 1개만 다를 경우 true
        }
    }
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        boolean[] visited = new boolean[words.length];
        ArrayDeque<Word> dq = new ArrayDeque<>(); // idx, stepCount
        dq.add(new Word(begin, 0));
        while(!dq.isEmpty()){
            Word temp = dq.poll();
            // System.out.printf("%s, %d\n",temp.word, temp.step);
            for(int i=0;i<words.length;i++){
                if(visited[i]) continue; // 이미 방문했음.
                if(temp.change_possible(words[i])){                
                    if(words[i].equals(target)) return temp.step + 1;
                    dq.add(new Word(words[i],temp.step + 1));
                    visited[i] = true;
                }
                
            }

        }
        return 0;
    }
    
}