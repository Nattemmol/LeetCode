class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        new_line = []
        
        for line in source:
            i = 0
            if not in_block:
                new_line = []
            
            while i < len(line):
                if not in_block and i + 1 < len(line) and line[i:i+2] == '/*':
                    in_block = True
                    i += 1
                elif in_block and i + 1 < len(line) and line[i:i+2] == '*/':
                    in_block = False
                    i += 1
                elif not in_block and i + 1 < len(line) and line[i:i+2] == '//':
                    break 
                elif not in_block:
                    new_line.append(line[i])
                i += 1
            
            if new_line and not in_block:
                res.append("".join(new_line))
        
        return res
