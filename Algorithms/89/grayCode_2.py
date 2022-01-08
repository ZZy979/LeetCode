# 假设n位二进制数b末尾有k个1，则b可以写成以下形式：
#        b = b[n-1]    b[n-2]     ...    b[k+1]        0   1 1 ... 1
#     b>>1 =   0       b[n-1]     ...    b[k+2]     b[k+1] 0 1 ... 1
# b^(b>>1) = b[n-1] b[n-1]^b[n-2] ... b[k+2]^b[k+1] b[k+1] 1 0 ... 0
# 同理
#              b+1 = b[n-1]    b[n-2]     ...    b[k+1]         1   0 0 ... 0
#         (b+1)>>1 =   0       b[n-1]     ...    b[k+2]      b[k+1] 1 0 ... 0
# (b+1)^((b+1)>>1) = b[n-1] b[n-1]^b[n-2] ... b[k+2]^b[k+1] ~b[k+1] 1 0 ... 0
# 因此如果定义g(b)=b^(b>>1)，则g(b)和g(b+1)只有一位不同（b[k+1]和~b[k+1]）
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ i >> 1 for i in range(2 ** n)]
