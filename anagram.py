def check(s1, s2):

	s1=(s1.replace(" ",""))
	s2=(s2.replace(" ",""))
	s1=s1.lower()
	s2=s2.lower()
	print(s1)
	print(s2)

	if ( sorted(s1) == sorted(s2) ):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")
#calling function 
s1 ="listen"
s2 ="silent"
check(s1, s2)
check("natural","at lunar")
check("language","a age lung")
check("processing","princes go")
check("corona Virus","or via us corn")


