class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(sorted(s))
        t_map = Counter(sorted(t))

        return s_map == t_map