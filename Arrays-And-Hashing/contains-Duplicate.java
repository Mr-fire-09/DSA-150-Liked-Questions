// 🏏 Top 150 NotOut - Contains Duplicate
// Author: Neeraj Singh

import java.util.*;

public class ContainsDuplicate {
    public static boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter numbers separated by space: ");
        String[] input = sc.nextLine().split(" ");
        int[] nums = new int[input.length];

        for (int i = 0; i < input.length; i++) {
            nums[i] = Integer.parseInt(input[i]);
        }

        if (hasDuplicate(nums)) {
            System.out.println("✅ Yes, the array contains duplicates.");
        } else {
            System.out.println("🎯 No, all elements are unique.");
        }

        sc.close();
    }
}
