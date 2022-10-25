def path(matrix,m,n):
    res=[]
    path=[[0 for i in range(n)] for j in range(m)]
    def dfs(s,matrix,row,column,path,step):
        
        if row==m-1 and column==n-1:
            path[row][column]=step
            for i in path:
                print(i)
            print(s,"\n")
            return
        if matrix[row][column]==False:
            return
        matrix[row][column]=False
        path[row][column]=step
        if row<m-1:
            dfs(s+"D", matrix,row+1,column,path,step+1)
        if column<n-1:
            dfs(s+"R", matrix ,row ,column+1,path,step+1)
        if row>0:
            dfs(s+"U", matrix, row-1, column,path,step+1)
        if column>0:
            dfs(s+"L", matrix, row, column-1,path,step+1)
        matrix[row][column]=True
        path[row][column]=0
        return res

    return dfs("",matrix,0,0,path,1)


m,n=3,3
matrix=[[True for i in range(n)]for j in range(m)]

print(path(matrix, m, n))