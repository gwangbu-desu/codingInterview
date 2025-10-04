
class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        int result[] = new int[3];
        int idx = 0;
        int score = 0;
        int before = 0;
        String sc = "";
        for(int i=0;i<dartResult.length();i++){
            char a = dartResult.charAt(i);
            System.out.println(sc);
            switch (a){
                case 'S':
                    score = Integer.parseInt(sc);
                    result[idx++] = score;
                    sc = "";
                    break;
                case 'D':
                    score = Integer.parseInt(sc);
                    result[idx++] = (int) Math.pow(score,2);
                    sc = "";
                    break;
                case 'T':
                    score = Integer.parseInt(sc);
                    result[idx++] = (int) Math.pow(score,3);
                    sc = "";
                    break;
                case '*':
                    before = idx - 1;
                    if( before != 0){
                        result[before - 1] *= 2;   
                    }
                    result[before] *= 2;
                    break;
                case '#':
                    result[idx - 1] *= -1;
                    break;
                default:
                    sc += String.valueOf(a);
                    break;
            }
            
        }
        answer = result[0] + result[1] + result[2];
        return answer;
    }
}