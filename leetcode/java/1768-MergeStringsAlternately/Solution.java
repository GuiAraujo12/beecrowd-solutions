class Solution {
    public String mergeAlternately(String word1, String word2) {
        String a = "";
        int i = Math.max(word1.length(), word2.length());
        for (int j = 0; j < i; j++) {
            if (j < word1.length()) a += word1.charAt(j);
            if (j < word2.length()) a += word2.charAt(j);
        }
        return a;
    }
}
