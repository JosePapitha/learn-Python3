#Definition of Anagram in which length are compared and sorted
#Sorted string is compared once again

def areAnagram(str1,str2):
	n1 = len(str1)
	n2 = len(str2)
	if n1!=n2:
		return 0

	str1 = sorted(str1)
	str2 = sorted(str2)
	for i in range(0,n1):
		if str1[i] != str2[i]:
			return 0
	return 1

#Main Program

str1 = "listen"
str2 = "silent"

if areAnagram(str1,str2):
	print ("Given two strings are Anagram of each other")
else:
	print ("Given two strings are not Anagram of each other")