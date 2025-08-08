class Solution {
    public int solution(int[] money) {
        int n = money.length;

        // 첫 집 털었을 경우
        int prev0 = 0;        // 직전 집 안 털었을 때
        int prev1 = money[0]; // 직전 집 털었을 때
        for (int i = 1; i < n - 1; i++) { // 마지막 집은 제외
            int temp0 = Math.max(prev0, prev1);
            int temp1 = prev0 + money[i];
            prev0 = temp0;
            prev1 = temp1;
        }
        int case1 = Math.max(prev0, prev1);

        // 첫 집 안 털었을 경우
        prev0 = 0;
        prev1 = money[1];
        for (int i = 2; i < n; i++) {
            int temp0 = Math.max(prev0, prev1);
            int temp1 = prev0 + money[i];
            prev0 = temp0;
            prev1 = temp1;
        }
        int case2 = Math.max(prev0, prev1);

        return Math.max(case1, case2);
    }
}
