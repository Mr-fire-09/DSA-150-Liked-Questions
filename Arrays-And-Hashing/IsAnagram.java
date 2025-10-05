// Day 2: Is Anagram? | Top 150 Notout Series
// Author: Neeraj Singh

import java.util.*;

public class IsAnagram {
    public static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        Arrays.sort(sArr);
        Arrays.sort(tArr);

        return Arrays.equals(sArr, tArr);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter first string: ");
        String s = sc.nextLine().toLowerCase();

        System.out.print("Enter second string: ");
        String t = sc.nextLine().toLowerCase();

        if (isAnagram(s, t))
            System.out.println(" Yes, both strings are anagrams.");
        else
            System.out.println(" No, they are not anagrams.");
        
        sc.close();
    }
}
