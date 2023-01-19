# Scan the input string s to count the number of '0's in total, let it be m. This is the number of flips needed when the left window is empty and the right window is the whole string.
# Set ans = m.
# Scan the input string 's' again,
# for each character '0', decrease m by 1 and replace ans with m if m is smaller.
# for each character '1', increase m by 1.
# Return ans

class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        for c in s:
            if (c=='0'):
                m+=1
        ans = m

        for c in s:
            if (c=='0'):
                m-=1
                ans=min(ans,m)
            else:
                m+=1
        return ans
    
####