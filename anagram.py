s1,s2=str(input().split())
def anagram_check(s1,s2):
   print(bool(sorted(s1)==sorted(s2)))
anagram_check(s1,s2)
