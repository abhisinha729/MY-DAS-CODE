class Solution:
    #abhi
    def getRow(self, rowIndex: int) -> List[int]:
        a=[]
        for i in range (rowIndex+1):
            temp_list=[]
            for j in range(i+1):
                if j==0 or j==i:
                    temp_list.append(1)
                else:
                    temp_list.append(a[i-1] [j-1] + a[i-1] [j])
            a.append(temp_list)
        return a[rowIndex]
        # print(a)
        # print("pascal Triangle")
        # for i in range(rowIndex+1):
        #     for j in range(rowIndex-i):
        #          print(" ",end="" )
        #     for j in range(i+1):
        #         print(a[i][j],end=" ")
        #     print(" ")  
        # return a[rowIndex]                       