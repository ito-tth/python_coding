N,K = map(int,input().split())
A = [0] * (N + 1)
for i in range(len(A)):
    if i < K:
        A[i] = 1
    else:
        b = 0
        k = i - K
        for j in range(N - K):
            b += A[k]
            k += 1
        A[i] = b
print(A[N] % (10 ** 9))
