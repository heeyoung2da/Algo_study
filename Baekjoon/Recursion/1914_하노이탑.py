def hanoi(N,s,t,d):
    if N==1:
        print(s, d, sep = " ")
        return
        
    hanoi(N-1, s, d, t)
    hanoi(1, s, t, d)
    hanoi(N-1, t, s, d)    

N = int(input())

print(2**N-1)
if N<= 20:
    hanoi(N,1,2,3)
