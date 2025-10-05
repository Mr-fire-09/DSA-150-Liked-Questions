#  Day 2: Is Anagram? (Optimized Approach)
# Top 150 Notout DSA Series by Neeraj Singh

def isAnagram(s: str, t: str) -> bool:
    # Quick length check
    if len(s) != len(t):
        return False

    # Dictionaries to count character frequency
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    # Compare frequency maps
    return countS == countT


# --- User Input ---
s = input("Enter first string: ").strip().lower()
t = input("Enter second string: ").strip().lower()

# --- Output ---
if isAnagram(s, t):
    print("Yes, both strings are anagrams.")
else:
    print(" No, they are not anagrams.")
