import java.util.*;
import java.io.*;

public class Main {
    public static int INF = (int)1e9;
    public static int[] dx = new int[]{1,0,-1,0};
    public static int[] dy = new int[]{0,1,0,-1};
    public static int N,M;
    public static int[][] arr;
    public static boolean[][] visited;
    public static int[][] distance;
    public static int dijkstra(int start, int end){
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[2] - b[2]);
        distance[start][end] = 0;
        visited[start][end] = true;
        int[] tmp;
        int next_start,next_end;
        pq.add(new int[]{start,end,arr[0][0]});
        while(!pq.isEmpty()){
            tmp = pq.poll();
            for(int i=0;i<4;i++){
                next_start = tmp[0] + dx[i];
                next_end = tmp[1] + dy[i];
                if(next_start >= 0 && next_end >=0 && next_start < M && next_end <N){
                    if(!visited[next_start][next_end] && distance[next_start][next_end]
                     > distance[tmp[0]][tmp[1]]+ arr[tmp[0]][tmp[1]]){
                        distance[next_start][next_end] = distance[tmp[0]][tmp[1]] + arr[next_start][next_end];
                        pq.add(new int[]{next_start,next_end,distance[next_start][next_end]});
                    }
                }
            }
        }
        return distance[M-1][N-1];
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[M][N];
        visited = new boolean[M][N];
        distance = new int[M][N];
        for(int i=0;i<M;i++){
            String tmp = br.readLine();
            for(int j=0;j<N;j++){
                arr[i][j] = tmp.charAt(j) - '0';
            }
        }
        for(int i=0;i<M;i++){
            Arrays.fill(distance[i], INF);
        }
        int answer = dijkstra(0,0);
        System.out.println(answer);
    }
}
