import java.io.*;
import java.util.*;
public class Main {
    public static int MAX_INT = Integer.MAX_VALUE;
    public static int n,s;
    public static long[] car; // 자동차 위치
    public static boolean[] state; // 연결 여부
    public static long[] oil;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken()) - 1; // 0-index
        car = new long[n];
        state = new boolean[n];
        oil = new long[n];

        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            car[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            oil[i] = Integer.parseInt(st.nextToken());
        }
        // car에서 오일만큼 +- 하기
        int left_idx = s;
        int right_idx = s;
        Queue<Integer> dq = new ArrayDeque<>();
        dq.add(s);
        state[s] = true;
        while(!dq.isEmpty()){
            int tmp = dq.poll();
            long next_left = car[tmp] - oil[tmp];
            long next_right = car[tmp] + oil[tmp];

            // 왼쪽 확장
            while(left_idx > 0 && car[left_idx - 1] >= next_left){
                left_idx--;
                if(!state[left_idx]){
                    state[left_idx] = true;
                    dq.add(left_idx);
                }
            }

            // 오른쪽 확장
            while(right_idx < n-1 && car[right_idx + 1] <= next_right){
                right_idx++;
                if(!state[right_idx]){
                    state[right_idx] = true;
                    dq.add(right_idx);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            if(state[i]) {
                sb.append(i + 1).append(" ");
            }
        }

        System.out.print(sb.toString().trim());
    }
}