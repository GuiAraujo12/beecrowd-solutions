class Solution {
    public boolean contains(char[] v, char a) {
        for (int i = 0; i < v.length; i++) {
            if (a == v[i]) return true;
        }
        return false;
    }

    public String reverseVowels(String s) {
        char[] vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        char[] v = new char[s.length()];
        int w = 0;
        for (int i = 0; i < s.length(); i++) {
            if (contains(vowels, s.charAt(i))) {
                v[w] = s.charAt(i);
                w++;
            }
        }
        String e = "";
        for (int i = 0; i < s.length(); i++) {
            if (contains(vowels, s.charAt(i))) {
                e += v[w - 1];
                w--;
            } else e += s.charAt(i);
        }
        return e;
    }
}
