# Time: O(n) - Single iteration over string and linear-time reverse()
# Space: O(n) - Scales with input string due to arrays storing up to len(s) elements
class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        word = []

        for i in range(len(s)):
            if len(word) > 0 and s[i] == ' ':
                output.append(''.join(word))
                word = []
            elif s[i] != ' ':
                word.append(s[i])
        
        if (len(word) > 0):
            output.append(''.join(word))
        
        output.reverse()
        return ' '.join(output)
