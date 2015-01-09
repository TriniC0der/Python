
varA = 'x'
varB = 'x'

if isinstance(varA, basestring) or isinstance(varB, basestring):
    print("string involved")
elif varA > varB:
	print("bigger")
elif varA == varB:
	print("equal")
elif varA < varB:
	print("smaller")