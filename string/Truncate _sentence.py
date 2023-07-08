def truncateSentence(s: str, k: int) -> str:
        num = []
        s = s.split()
        i = 0
        while i < k:
            num.append(s[i])
            i = i + 1
        x = " ".join(num)
        return x

s = "Hello how are you Contestant" 
k = 4
print(truncateSentence(s, k))