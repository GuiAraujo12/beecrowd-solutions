import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = candies[1];
        List<Boolean> array = new ArrayList<>();
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] > max) max = candies[i];
        }
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= max) array.add(true);
            else array.add(false);
        }
        return array;
    }
}
