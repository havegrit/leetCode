class Solution {
    public int[] getAverages(int[] nums, int k) {
        int[] avgs = new int[nums.length];
        long sum = 0;
        int cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            avgs[i] = -1;
            sum += nums[i];
            if (i == k*2 + cnt) {
                if (cnt == 0) {
                    avgs[k+cnt] = (int) (sum / (long) ((k*2) + 1));
                } else {
                    sum -= nums[cnt-1];
                    avgs[k+cnt] = (int) (sum / (long) ((k*2) + 1));
                }
                cnt++;
            }
        }
        return avgs;
    }
}