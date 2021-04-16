# segment_tree----------------
def seg_func(x,y):
    return min(x,y)


first_ele = inf

class Seg_Tree:
    def __init__(self,init_array, seg_func, first_ene):
        # init変数
        n = len(init_array)
        self.seg_length = (1 << (n-1).bit_length()) - 1 # 葉以外のノード数
        self.seg_func = seg_func
        self.first_ele = first_ele
        self.seg_tree = [self.first_ele]*(2*self.seg_length+1)
        # seg_treeに値を入れる
        for i in range(n):
            self.seg_tree[self.seg_length+i] = init_array[i]
        # seg_treeを構築していく
        for i in range(self.seg_length-1,-1,-1):
            self.seg_tree[i] = self.seg_func(self.seg_tree[2*i+1],self.seg_tree[2*i+2])
    
    
    # index番目をxに更新する
    def updata(self, index, x):
        n = self.seg_length+index
        self.seg_tree[n] = x
        while n > 0:
            n = (n-1)//2
            self.seg_tree[n] = self.seg_func(self.seg_tree[2*n+1],self.seg_tree[2*n+2])
    
    
    # query(taken_left, taken_riht, 見るノード, 対応する葉_left, 対応する葉_right)
    def query(self, L, R):
        L += self.seg_length
        R += self.seg_length
        res = self.first_ele
        while L < R:
            if R & 1:
                res = self.seg_func(res, self.seg_tree[R])
                R -= 1  
            if 0 == (L & 1):
                res = self.seg_func(res, self.seg_tree[L])
                L += 1
            L >>= 1
            R = (R-1)>>1
        if L==R:
            res = self.seg_func(res,self.seg_tree[L])
        return res

        
# segment_tree---- 以下0-indexでセグ木を扱う 元の配列はseg.seg_lengthが0-index

N,M=map(int, input().split())
A=list(map(int, input().split()))
inf=10**7

seg = Seg_Tree([i for i in range(N+1)], seg_func, first_ele)
temp = [0]*(N+1)
for i in range(M):
    seg.updata(A[i],inf)
    temp[A[i]]+=1
ans = seg.query(0,N)
for i in range(N-M):
    temp[A[M+i]]+=1
    seg.updata(A[M+i],inf)
    temp[A[i]]-=1
    if temp[A[i]]==0:seg.updata(A[i],A[i])
    ans=min(ans,seg.query(0,N))

print(ans)
