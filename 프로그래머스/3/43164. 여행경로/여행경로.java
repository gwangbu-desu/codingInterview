import java.util.*;

class Solution {
    String[][] tickets;
    boolean[] visited;
    String[] answer;
    int length;
    int count = 0;
    public String[] solution(String[][] tickets) {
        this.tickets = tickets;
        length = tickets.length;
        visited = new boolean[length];
        answer = new String[length+1];
        Arrays.sort(tickets, (a,b)->a[1].compareTo(b[1]));
        // for(String[] ticket:tickets){
        //     System.out.printf("%s ,%s\n",ticket[0],ticket[1]);
        // }
        answer[count++] = "ICN";
        backtracking("ICN");
        return answer;
    }
    public void backtracking(String before_name){
        if(count == length + 1){
            // System.out.println("Check");
            return;
        }
        for(int i=0;i<length;i++){
            if(visited[i]) continue;
            if(!tickets[i][0].equals(before_name)) continue;
            visited[i] = true;
            answer[count] = tickets[i][1];
            // System.out.println(answer[count]);
            count++;
            backtracking(tickets[i][1]);
            if(count == length + 1) break;
            
            count--;
            visited[i] = false;
        }
        
    }
}