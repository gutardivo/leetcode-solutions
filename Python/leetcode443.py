from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = [chars[0]]  # Stores the compressed characters
        char_count = 0  # Keeps track of the number of consecutive occurrences
        current_char = chars[0]  # The character we're currently counting
        
        for char in chars:
            if char == current_char:
                char_count += 1
            else:
                if char_count != 1:
                    compressed.extend(str(char_count))  # Append the count if more than 1
                compressed.append(char)  # Append the new character
                current_char = char  # Update the current character
                char_count = 1  # Reset the count for the new character
        
        if char_count != 1:  # After the loop, if the last group had more than 1 occurrence
            compressed.extend(str(char_count))
        
        chars[:len(compressed)] = compressed  # Copy the compressed result back to the input list
        print(compressed)
        return len(compressed) 


chars = ["a","a","b","b","c","c","c"]

s = Solution()
print(s.compress(chars))