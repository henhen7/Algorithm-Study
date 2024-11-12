class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        int i ;
        for (i = 0; i < array.length; i++) {
            if (array[i] == n) {
            answer += 1;
            }
        }
        return answer;
    }
}