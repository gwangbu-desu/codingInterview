import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N;
        int M;
        int[] arr;
        int max_money = 0;
        int total_money = 0;
        N = Integer.parseInt(st.nextToken());
        arr = new int[N];
        M = Integer.parseInt(st.nextToken());

        for (int i=0;i<N;i++){
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
            if (max_money < arr[i]){
                max_money = arr[i];
            }
            total_money += arr[i];
        }
        int left = max_money;
        int right = total_money;
        int answer = total_money;
        while(left<= right){
            int mid = (left+ right)/2;
            if(is_possible(arr,N,M,mid)){
                answer = mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        System.out.println(answer);
    }

    public static boolean is_possible(int[] arr,int N, int M, int k){
        int count = 1;
        int money = k;
        for(int i=0;i<N;i++){
            if (arr[i] > k ) return false;
            if (money < arr[i]){ // 돈이 부족하면
                count++; // 다시 인출
                money = k;
            }
            money -= arr[i];
        }
        return count <= M;
    }
}