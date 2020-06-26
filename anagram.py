s1,s2=input("enter two string separated by space").split()
s1=s1.lower()
s2=s2.lower()
def anagram_check(s1,s2):
   print(bool(sorted(s1)==sorted(s2)))
anagram_check(s1,s2)
