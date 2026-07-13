class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for i in strs:
            if tuple(sorted(i)) not in output:
                output[tuple(sorted(i))] = []
            
            output[tuple(sorted(i))].append(i)
        return list(output.values())    