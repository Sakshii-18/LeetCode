class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = [0] * 2001
        for i in arr:
            freq[i+1000] +=1

        seenArr = [0] *1001
        for i in freq:
            if i>0:
                seenArr[i] +=1
                if seenArr[i] >1:
                    return False
        return True
        