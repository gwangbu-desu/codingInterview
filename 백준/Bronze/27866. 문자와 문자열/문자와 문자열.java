import java.util.*;
import java.io.*;
//import하는 부분

public class Main { //main클래스
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int a = Integer.parseInt(br.readLine());
        System.out.println(str.charAt(a-1));
    }
}
