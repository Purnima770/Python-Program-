s = "hello world"
v = 0
for c in s.lower():
    if c in "aeiou":
        v+=1
print("Vowels:", v, "Consonants:", len([c for c in s if c.isalpha()])-v)