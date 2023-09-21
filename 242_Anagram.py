class Solution(object):
    def isAnagram(self, s, t,):
        dictonary = [0] * 26
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            dictonary[ord(s[i]) % 97] = dictonary[ord(s[i]) % 97] + 1
        for i in range(len(t)):
            dictonary[ord(t[i]) % 97] = dictonary[ord(t[i]) % 97] - 1
        return all([val ==0 for val in dictonary])



sol = Solution()
anagram_s1 = "anagram"
anagram_t1 = "nagaram"
anagram_s2 = "zxcvbnm"
anagram_t2 = "mnbvcxz"
anagram_s3 = "zxcvbn"
anagram_t3 = "qwerty"
print(sol.isAnagram(anagram_s1, anagram_t1))
print(sol.isAnagram(anagram_s2, anagram_t2))
print(sol.isAnagram(anagram_s3, anagram_t3))