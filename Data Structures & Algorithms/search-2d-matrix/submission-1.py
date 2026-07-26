class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow,ncol=len(matrix),len(matrix[0])
        total=nrow*ncol
        low,high=0,total-1
        while(low<=high):
            mid=(low+high)//2
            row,column=(mid//ncol),mid%ncol
            #print(low,high,matrix[row][column])
            if matrix[row][column]==target:
                return True
            if matrix[row][column]<target:
                low=mid+1
            else:
                high=mid-1
        return False
        