class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            temp = [0] + res + [0]
            rows = []
            for j in range(len(res)+1):
                rows.append(temp[j] + temp[j+1])
            res = rows
        return res 
            