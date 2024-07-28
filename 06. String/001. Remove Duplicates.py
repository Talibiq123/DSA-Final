# Remove Duplicates
# Given a string str without spaces, the task is to remove all duplicate characters from it,
# keeping only the first occurrence.
# Note: The original order of characters must be kept the same. 
# Examples :
# Input: str = "zvvo"
# Output: "zvo"
# Explanation: Only keep the first occurrence

str = "zvvo"
seen = set()
result = []

for char in str:
    if char not in seen:
        seen.add(char)
        result.append(char)
 
ans = ''.join(result)   
print(ans)
