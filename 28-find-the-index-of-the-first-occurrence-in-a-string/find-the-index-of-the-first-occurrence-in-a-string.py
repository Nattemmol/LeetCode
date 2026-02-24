class Solution(object):
    def strStr(self, haystack, needle):
        index = haystack.find(needle)
        if index!=-1:
            return index
        else:
            return -1
        