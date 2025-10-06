class Solution {
    public String solution(String p) {
        String answer = "";

        answer = private_solution(p);
        return answer;
    }
    public String private_solution(String word){
        // 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
        if (word.length() == 0){
            return word;
        }
        
        // 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
        String[] splitted = split(word);
        // 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
        // 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        if(check_right_word(splitted[0])){    
            //   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
            String result = private_solution(splitted[1]);
            splitted[0] += String.valueOf(result);
            return splitted[0];
        } else{
            // 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.   
            //   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            String empty = "(";
            //   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            String result = private_solution(splitted[1]);
            empty += String.valueOf(result);
            //   4-3. ')'를 다시 붙입니다. 
            empty += String.valueOf(")");
            //   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
            char[] temp = splitted[0].substring(1,splitted[0].length()-1).toCharArray();
            for(int i=0;i<temp.length;i++){
                if( temp[i] == '('){
                    temp[i] = ')';
                }else{
                    temp[i] = '(';
                }
            }
            empty += String.valueOf(new String(temp));
            //   4-5. 생성된 문자열을 반환합니다.
            return empty;
        } 
    }
    public String[] split(String word){
        // 앞부분부터 탐색하며 균형잡힌 괄호 문자열로 분리. 
        char[] w = word.toCharArray();
        int count = 0;
        int idx = 0;
        // 짝수길이니 2개씩 증가.
        for(int i=0;i<w.length;i = i + 2){
            for(int j=0;j<2;j++){
                if(w[i+j] == '('){
                    count ++;
                }else if (w[i+j] == ')'){
                    count --;
                }
            }
            if (count == 0){
                idx = i+1;
                break;
            }
        }
        String[] uv = new String[2];
        uv[0] = word.substring(0,idx+1);
        uv[1] = word.substring(idx+1,w.length);
        System.out.println(uv[0]);
        System.out.println(uv[1]);
        return uv;
    }
    public boolean check_right_word(String u){
        char[] w = u.toCharArray();
        int count = 0;
        for(char i : w){
            // count를 할때 음수가 되지 않아야함.
            if ( i == '('){
                count++;
            }else{
                count--;
            }
            if(count < 0){
                return false;
            }
        }
        return true;
    }
}