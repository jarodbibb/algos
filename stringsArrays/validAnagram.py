class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        for item in s:
            sDict[item] = sDict.get(item, 0) + 1
        for item in t:
            tDict[item] = tDict.get(item, 0) + 1
        return sDict == tDict