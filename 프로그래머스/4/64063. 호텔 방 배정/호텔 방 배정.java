import java.util.*;
class Solution {
    HashMap<Long,Long> room = new HashMap<>();
    public long[] solution(long k, long[] room_number) {
        long[] answer = new long[room_number.length];
        int cnt = 0;
        for(long number : room_number){
            long check_number = find_room(number);
            
            answer[cnt++] = check_number;
        }
        return answer;
    }
    public long find_room(long number){
        if(room.get(number) == null){
            room.put(number,number+1);
            return number;
        }
        long empty_room = find_room(room.get(number));
        room.put(number, empty_room+1);
        return empty_room;
    }
}