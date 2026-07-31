class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int v = 0;
        int len = flowerbed.length;
        for (int i = 0; i < len; i++) {
            if (flowerbed[i] == 0) {
                if (((i == 0) || flowerbed[i - 1] == 0) && ((i == len - 1) || flowerbed[i + 1] == 0)) {
                    v++;
                    flowerbed[i] = 1;
                }
            }
        }
        return v >= n;
    }
}
