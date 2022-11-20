import random

#Names = ["Maryeliz", "Zach", "Alex", "Elise", "Julianne","Kim","Maryeliz", "Zach", "Alex", "Elise", "Julianne","Kim"]

MaryelizNames = ["M", "Z"]
ZachNames = ["Z", "M"]
AlexNames = ["A", "E"]
EliseNames = ["E", "A"]
JulianneNames = ["J"]
KimNames = ["K"]

PulledName1 = ""
PulledName2 = ""

Valid = False 

while Valid==False:
	Names = ["M", "Z", "A", "E", "J","K","M", "Z", "A", "E", "J","K"]

	while len(MaryelizNames) < 4:
		MaryelizNames.append(random.choice(Names))
		MaryelizNames = list(dict.fromkeys(MaryelizNames))

	PulledName1 = MaryelizNames[2]
	PulledName2 = MaryelizNames[3]
	Names.remove(PulledName2)
	Names.remove(PulledName1)

	while len(ZachNames) < 4:
		ZachNames.append(random.choice(Names))
		ZachNames = list(dict.fromkeys(ZachNames))

	PulledName1 = ZachNames[2]
	PulledName2 = ZachNames[3]
	Names.remove(PulledName2)
	Names.remove(PulledName1)

	while len(AlexNames) < 4:
		AlexNames.append(random.choice(Names))
		AlexNames = list(dict.fromkeys(AlexNames))

	PulledName1 = AlexNames[2]
	PulledName2 = AlexNames[3]
	Names.remove(PulledName2)
	Names.remove(PulledName1)

	while len(EliseNames) < 4:
		EliseNames.append(random.choice(Names))
		EliseNames = list(dict.fromkeys(EliseNames))

	PulledName1 = EliseNames[2]
	PulledName2 = EliseNames[3]
	Names.remove(PulledName2)
	Names.remove(PulledName1)

	while len(JulianneNames) < 3:
		JulianneNames.append(random.choice(Names))
		JulianneNames = list(dict.fromkeys(JulianneNames))

	PulledName1 = JulianneNames[1]
	PulledName2 = JulianneNames[2]
	Names.remove(PulledName2)
	Names.remove(PulledName1)


	KimNames.append(Names[0])
	KimNames.append(Names[1])
	KimNames = list(dict.fromkeys(KimNames))
	MaryelizNames.remove(MaryelizNames[1])
	ZachNames.remove(ZachNames[1])
	AlexNames.remove(AlexNames[1])
	EliseNames.remove(EliseNames[1])

	if len(KimNames) == 3:
		Valid = True	
		

print("{'", "','".join(str(x) for x in MaryelizNames),"'},")
print("{'", "','".join(str(x) for x in ZachNames),"'},")
print("{'", "','".join(str(x) for x in AlexNames),"'},")
print("{'", "','".join(str(x) for x in EliseNames),"'},")
print("{'", "','".join(str(x) for x in JulianneNames),"'},")
print("{'", "','".join(str(x) for x in KimNames),"'},")

import random

#Names = ["Maryeliz", "Zach", "Alex", "Elise", "Julianne","Kim","Maryeliz", "Zach", "Alex", "Elise", "Julianne","Kim"]

MaryelizNames = ["M", "Z"]
ZachNames = ["Z", "M"]
AlexNames = ["A", "E"]
EliseNames = ["E", "A"]
JulianneNames = ["J"]
KimNames = ["K"]

PulledName1 = ""
PulledName2 = ""

Valid = False 

while Valid==False:
	Names = ["M", "Z", "A", "E", "J","K","M", "Z", "A", "E", "J","K"]

	while len(MaryelizNames) < 4:
		MaryelizNames.append(random.choice(Names))
		MaryelizNames = list(dict.fromkeys(MaryelizNames))

	PulledName1 = MaryelizNames[2]
	PulledName2 = MaryelizNames[3]
	Names.remove(PulledName2)
	Names.remove(PulledName1)

	while len(ZachNames) < 4:
		ZachNames.append(random.choice(Names))
		ZachNames = list(dict.fromkeys(ZachNames))

	PulledName1 = ZachNames[2]
	PulledName2 = ZachNames[3]
	Names.remove(PulledName2)
	Names.remove(PulledName1)

	while len(AlexNames) < 4:
		AlexNames.append(random.choice(Names))
		AlexNames = list(dict.fromkeys(AlexNames))

	PulledName1 = AlexNames[2]
	PulledName2 = AlexNames[3]
	Names.remove(PulledName2)
	Names.remove(PulledName1)

	while len(EliseNames) < 4:
		EliseNames.append(random.choice(Names))
		EliseNames = list(dict.fromkeys(EliseNames))

	PulledName1 = EliseNames[2]
	PulledName2 = EliseNames[3]
	Names.remove(PulledName2)
	Names.remove(PulledName1)

	while len(JulianneNames) < 3:
		JulianneNames.append(random.choice(Names))
		JulianneNames = list(dict.fromkeys(JulianneNames))

	PulledName1 = JulianneNames[1]
	PulledName2 = JulianneNames[2]
	Names.remove(PulledName2)
	Names.remove(PulledName1)


	KimNames.append(Names[0])
	KimNames.append(Names[1])
	KimNames = list(dict.fromkeys(KimNames))
	MaryelizNames.remove(MaryelizNames[1])
	ZachNames.remove(ZachNames[1])
	AlexNames.remove(AlexNames[1])
	EliseNames.remove(EliseNames[1])

	if len(KimNames) == 3:
		Valid = True	
		

print("{'", "','".join(str(x) for x in MaryelizNames),"'},")
print("{'", "','".join(str(x) for x in ZachNames),"'},")
print("{'", "','".join(str(x) for x in AlexNames),"'},")
print("{'", "','".join(str(x) for x in EliseNames),"'},")
print("{'", "','".join(str(x) for x in JulianneNames),"'},")
print("{'", "','".join(str(x) for x in KimNames),"'},")

