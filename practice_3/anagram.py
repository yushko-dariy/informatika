def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
        
    s2_list = list(s2)
    for c in s1:
        if c in s2_list:
            s2_list.remove(c)
        else:
            return False
    return True

print(is_anagram("heart", "earth"))   
print(is_anagram("python", "typhon"))  
print(is_anagram("hello", "world"))   
print(is_anagram("ab", "abc"))     
print(is_anagram("rat", "cat"))