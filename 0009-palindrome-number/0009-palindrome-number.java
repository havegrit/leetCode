class Solution {
    public boolean isPalindrome(int x) {
        int originX = x;
        int reversed = 0;
        while(x>0){
            reversed = reversed*10 + x%10;
            x = x/10;
        }

        return originX == reversed;
    }
}