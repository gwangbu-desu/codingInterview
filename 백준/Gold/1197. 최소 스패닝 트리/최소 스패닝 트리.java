import java.io.*;
import java.util.*;
public class Main {
    public static int V,E;
    public static int[] parents;
    public static int[][] edges;
    public static int parent(int index){
        if(parents[index] != index){
            parents[index] = parent(parents[index]);
        }
        return parents[index];
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        parents = new int[V];
        edges = new int[E][3]; // from to weight
        for(int i=0;i<V;i++){
            parents[i] = i;
        }

        for(int i=0;i<E;i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            edges[i][0] = from-1;
            edges[i][1] = to-1;
            edges[i][2] = weight;
        }
        long answer = 0;
        Arrays.sort(edges,(a,b) -> a[2] - b[2]);
        for(int[] current:edges){
            int parentA = parent(current[0]);
            int parentB = parent(current[1]);
            if(parentA == parentB){
                continue;
            }else if(parentA > parentB){
                parents[parentB] = parentA;
                answer += current[2];
            }else{
                parents[parentA] = parentB;
                answer += current[2];
            }
        }
        System.out.println(answer);
    }
}