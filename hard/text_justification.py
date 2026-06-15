# Time: O(n) - Single iteration over all words, one-time iteration over slots per word
# Space: O(n) - Storing all words during execution plus spaces, bounded by a multiple of n
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        curr_words = []
        curr_letters = 0  # Only tracks the raw length of characters (no spaces)

        for word in words:
            # Phase 1: Check if adding the word + minimum 1-space intervals exceeds limit
            # len(curr_words) represents the minimum number of spaces needed between words
            if curr_letters + len(word) + len(curr_words) > maxWidth:
                
                # Phase 2: Justification Math
                total_spaces = maxWidth - curr_letters
                slots = len(curr_words) - 1
                
                if slots == 0:
                    # Edge Case A: Only one word fits -> Left justify
                    result.append(curr_words[0] + ' ' * total_spaces)
                else:
                    # Regular Case: Distribute spaces evenly among internal slots
                    base_spaces = total_spaces // slots
                    leftover_spaces = total_spaces % slots
                    
                    line = ""
                    for j in range(slots):
                        line += curr_words[j]
                        # Give base spaces, plus 1 extra if we have leftovers (round-robin)
                        line += ' ' * (base_spaces + (1 if j < leftover_spaces else 0))
                    line += curr_words[-1]  # Append last word cleanly
                    result.append(line)
                
                # Reset containers for the next line
                curr_words = []
                curr_letters = 0
            
            # Keep collecting words if the line isn't full yet
            curr_words.append(word)
            curr_letters += len(word)
            
        # Phase 3: Handle the final line (Always Left-Justified)
        last_line = " ".join(curr_words)
        trailing_padding = maxWidth - len(last_line)
        result.append(last_line + ' ' * trailing_padding)
        
        return result
# 1. Utilize the concept of separation of concerns to adequately dissect the functionalities required. Do not immediately go down the path of least resistance.
