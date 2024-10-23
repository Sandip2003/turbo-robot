import java.util.HashMap;

public class LongestRepeatingCharacterReplacement {

    public static int characterReplacement(String s, int k) {
        int n = s.length();
        int maxCount = 0;
        int start = 0;
        int end = 0;
        HashMap<Character, Integer> count = new HashMap<>();

        while (end < n) {
            count.put(s.charAt(end), count.getOrDefault(s.charAt(end), 0) + 1);
            maxCount = Math.max(maxCount, count.get(s.charAt(end)));

            if (end - start + 1 - maxCount > k) {
                count.put(s.charAt(start), count.get(s.charAt(start)) - 1);
                start++;
            }

            end++;
        }

        return end - start;
    }

    public static void main(String[] args) {
        String s = "ABABABABBCDE";
        int k = 2;

        int maxLength = characterReplacement(s, k);
        System.out.println("Longest repeating character replacement length: " + maxLength);
    }
}
