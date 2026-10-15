class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen: set[str] = {*set(s), *set(t)}
    
        for c in seen:
            if s.count(c) != t.count(c): return False
        
        return True