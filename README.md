<!-- 🏏✨ TOP 150 NOTOUT - DSA MASTERY SERIES ✨🏏 -->

<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/Top150-NotOut/main/assets/banner.png" alt="Top 150 NotOut Banner" width="90%" />
</p>

<h1 align="center">🏏 Top 150 NotOut – DSA Mastery Series</h1>

<p align="center">
  <i>"Every coder faces challenges — but legends stay <b>NotOut</b> 💫"</i>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Language-Java-orange?style=for-the-badge&logo=java" />
  <img src="https://img.shields.io/badge/Problems-150-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge" />
</p>

---

## 🌟 Overview  

Welcome to **Top 150 NotOut Liked Questions**, a curated collection of 150 must-solve coding problems designed to enhance your **Data Structures & Algorithms** skills and prepare you for **technical interviews** with confidence.

Each problem includes:  
📘 Problem Description  
💡 Approach / Intuition  
💻 Python & Java Implementations  
⏱️ Time & Space Complexity  
🧩 Example Test Cases  

---

## 📚 Topics Covered  

| 🧠 Core DSA | 💎 Advanced Concepts |
|-------------|----------------------|
| Arrays & Hashing | Trees & Graphs |
| Two Pointers | Recursion & Backtracking |
| Sliding Window | Dynamic Programming |
| Stack / Queue | Greedy Algorithms |
| Binary Search | Bit Manipulation |
| Linked List | Math & Misc Problems |

---

## 🧠 Example Format  

### Problem: **Two Sum**  
**Difficulty:** 🟢 Easy  
**Approach:** Hash Map  
**Time Complexity:** O(n)  
**Space Complexity:** O(n)  

```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff))
                return new int[]{map.get(diff), i};
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}
💻 Creator

👨‍💻 By Neeraj Singh

📍 Aspiring Full Stack & Android Developer | Passionate about DSA and Problem Solving

💫 GitHub Aesthetic Tips

✨ Make your repo stand out:

Use a custom banner (like above).
🎨 Create one using Canva with this prompt:

“A minimalist dark-themed coding banner with neon blue accents, a glowing laptop, and the text ‘Top 150 NotOut – DSA Mastery Series’ in futuristic font.”

Add your GitHub stats cards:

![Neeraj's GitHub stats](https://github-readme-stats.vercel.app/api?username=yourusername&show_icons=true&theme=radical)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=yourusername&layout=compact&theme=radical)


Include cool badges:

![Python](https://img.shields.io/badge/Code-Python-blue)
![Java](https://img.shields.io/badge/Code-Java-orange)
![Status-InProgress](https://img.shields.io/badge/Status-In%20Progress-yellow)

🧩 Bonus: LinkedIn Branding Ideas

Post your daily problems with aesthetic consistency 🎯

🔖 Hashtag Series	Example Caption
🏏 #CodeNotOut	“Day 14/150 – Solved Longest Substring Without Repeating Characters 💻 #CodeNotOut #DSA150ByNeeraj”
💡 #DSA150ByNeeraj	“Cracking logic one day at a time ⚡ #DSA150ByNeeraj #Top150Challenge”
🚀 #Top150Challenge	“Building the coder mindset through consistency 🚀 Day 20/150 #Top150Challenge”
🌸 #ZenCode150	“Calm mind. Clean logic. Beautiful code. 🌸 #ZenCode150”
🏁 Let’s Begin the Journey

💫 “Don’t just solve problems. Understand them. Refactor them. Master them.”

📍 Repository: Top150-NotOut

👨‍💻 Created by: Neeraj Singh

🚀 #CodeNotOut | #DSA150ByNeeraj | #Top150Challenge
