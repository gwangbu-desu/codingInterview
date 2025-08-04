import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]); // 요청시간 기준 정렬

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]); // 소요시간 기준

        int now = 0, i = 0, answer = 0, count = 0;

        while (count < jobs.length) {
            // 현재 시간까지 들어온 작업을 모두 pq에 추가
            while (i < jobs.length && jobs[i][0] <= now) {
                pq.offer(new int[]{jobs[i][0], jobs[i][1]});
                i++;
            }

            if (pq.isEmpty()) {
                now = jobs[i][0]; // 다음 작업이 올 때까지 시간 점프
            } else {
                int[] job = pq.poll();
                now += job[1]; // 소요시간 만큼 진행
                answer += now - job[0]; // 종료시점 - 요청시각 = 대기+작업시간
                count++;
            }
        }

        return answer / jobs.length;
    }
}
