class Solution:

    def longestKSubstr(self, s, k):
        # code here
        
        max_length = -1
        char_count = {}  
        i = 0
        for j in range(len(s)):
            char_count[s[j]] = char_count.get(s[j], 0) + 1
            while len(char_count) > k:
                char_count[s[i]] -= 1
                if char_count[s[i]] == 0:
                    del char_count[s[i]]
                i += 1
            if len(char_count) == k:
                max_length = max(max_length, j - i + 1)
                
        return max_length
