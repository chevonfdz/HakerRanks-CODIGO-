
N,M=map(int,input().split())
up=[[0 for i in range(M)]for n in range(N)]
left=[]
land=[[x for x in input()] for i in range(N)]
for i in range(N):
    left.append([0 for x in range(M)])
    for j in range(M):
        if j==0:
            left[i][j]=0 if land[i][j]!='x' else -1
        elif land[i][j]=='x':
            left[i][j]=-1
        else:
            left[i][j]=left[i][j-1]+1
for i in range(M):
    for j in range(N):
        if j==0:
            up[j][i]=0 if land[j][i]!='x' else -1
        elif land[j][i]=='x':
            up[j][i]=-1
        else:
            up[j][i]=up[j-1][i]+1
max_perimeter=-1
for row in range(N-1,0,-1):
    for column in range(M-1,0,-1):
        for k in range(column-left[row][column],column):
            for temp in range(1,min(up[row][column],up[row][k])+1):
                if left[row-temp][column]>=(column-k):
                    max_perimeter=max(max_perimeter,2*(temp+column-k))
print(max_perimeter if max_perimeter>0 else 'impossible')