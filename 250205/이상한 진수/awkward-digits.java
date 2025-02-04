import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        Set<Long> anum = possibleBinarySet(a);
        Set<Long> bnum = possibleTernarySet(b);
        Long result = 0l;
        for (Long num: anum){
            if (bnum.contains(num)){
                result = num;
                break;
            }
        }
        System.out.println(result);       
    }

    public static Set<Long> possibleBinarySet(String binary){
        Set<Long> possibleNums = new HashSet<>();
        for ( int i= 0; i< binary.length();i++){
            char[] chars = binary.toCharArray();
            chars[i] = (chars[i] == '0') ? '1' : '0';
            possibleNums.add(Long.parseLong(new String(chars),2));
        }
        return possibleNums;
    }

    public static Set<Long> possibleTernarySet(String ternary){
        Set<Long> possibleNums = new HashSet<>();
        for (int i=0;i<ternary.length();i++){
            char[] chars = ternary.toCharArray();
            char originChar = chars[i];
            for (char j='0';j<'3';j++){
                if(originChar!=j){
                    chars[i] = j;
                    possibleNums.add(Long.parseLong(new String(chars),3));
                }
            }
        }
        return possibleNums;
    }
}