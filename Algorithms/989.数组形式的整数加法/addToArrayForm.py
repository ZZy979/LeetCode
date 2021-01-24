class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A.reverse()
        K = list(map(int, reversed(str(K))))
        if len(A) < len(K):
            A, K = K, A
        carry = 0
        for i in range(len(K)):
            carry, A[i] = divmod(A[i] + K[i] + carry, 10)
        i = len(K)
        while carry and i < len(A):
            carry, A[i] = divmod(A[i] + carry, 10)
            i += 1
        if carry:
            A.append(carry)
        A.reverse()
        return A
