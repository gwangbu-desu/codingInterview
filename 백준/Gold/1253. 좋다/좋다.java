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
        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        int answer = 0;
        for (int i=0 ;i<N; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.stream(arr).sorted();
        Arrays.sort(arr);
        for (int i=0;i<N;i++){
            int target = arr[i];
            int left = 0;
            int right = N-1;
            while(left<right){
                if (left == i){
                    left++;
                    continue;
                }
                if (right == i){
                    right--;
                    continue;
                }
                int sum = arr[left] + arr[right];
                if (sum == target){
                    answer++;
                    break;
                }
                else if(sum < target){
                    left++;
                }else{
                    right--;
                }
            }
        }
        System.out.println(answer);
    }
}