class Solution {
    public String reverseWords(String s) {
        String saida = "";
        String[] palavras = s.trim().split("\\s+");
        for (int i = palavras.length - 1; i >= 0; i--) {
            saida += palavras[i];
            if (i != 0) saida += " ";
        }
        return saida;
    }
}
