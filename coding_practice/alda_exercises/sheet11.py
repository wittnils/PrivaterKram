# implementation of Rabin-Karp-Algorithm
# nicht nlo, das habe ich nicht hinbekommen :(

# das ist ein pattern finding algoirthmus

def karp_rabin(P,S,q):
    m = len(P)
    n = len(S)
    d = 256 # number of characters in input alphabet
    h = 1
    print(P)
    p = 0
    s = 0
    
    for i in range(m-1):
        h = (h * d) % q
    # calculate first hash values
    for i in range(m):
        p = (d * p + ord(P[i])) %q
        s = (d * s + ord(S[i])) %q
    print(p)
    print(s)
    for i in range(n-m+1):
        if p == s:
            for j in range(m):
                if P[j] != S[i+j]:
                    break
            j += 1
            if j==m:
                print("Pattern found at index", str(i))
        # calculate new hash value
        if i < n-m:
            s = (d*(s-ord(S[i])*h)+ord(S[i+m]))% q
            if s < 0:
                s = s+q
    
s = "matthis scholz ist matthis scholz"
p = "matthis"

karp_rabin(p,s,17)