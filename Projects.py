class Solution:
    def searchMatrix(self, matrix, target):
        # coords of min and max [y,x]
        min = [0,0]
        max = [len(matrix)-1,len(matrix[0])-1]
        if max == min or (min[0] == max[0] and min[1]+1 == max[1]) or :
            if matrix[max[0]][max[1]] == target or matrix[min[0]][min[1]] == target:
                return True
            else:
                return False
        # while min and max arent essentially 1 element away horizontally
        while min[0] != max[0] or min[1] + 1 != max[1]:
            # mid coords [y,x]
            minpos = min[0] * len(matrix[0]) + min[1]
            maxpos = max[0] * len(matrix[0]) + max[1]
            minpos = (minpos + maxpos)/2
            mid = [int(minpos/len(matrix[0])),int(minpos%len(matrix[0]))]
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] > target:
                max = mid
            elif matrix[mid[0]][mid[1]] < target:
                min = mid
        return False


L = Solution()
print(L.searchMatrix(matrix=[[1,1]],target=1))