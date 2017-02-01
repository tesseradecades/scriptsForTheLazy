import argparse


siPrefixes = {
	"Y" : 10**24, "Z" : 10**21, "E": 10**18, "P" : 10**15, "T" : 10**12, 
	"G" : 10**9, "M" : 10**6, "k":10**3, "h" : 10**2, "da" : 10, "" : 10**0, 
	"d" : 10**-1, "c" : 10**-2, "m": 10**-3, "n" : 10**-9, "p" : 10**-12, 
	"f" : 10**-15, "a" : 10**-18, "z" : 10**-21, "y" : 10**-24
}

siUnitsToImperial = {
	#distance 0.00024710493
	"m"	 : {"th" : 39370.1, "in" : 39.3701, "ft" : 3.28084, "yd" : 1.09361, 
	"ch" : 0.0497097, "fur" : 0.00497096, "ml" : 0.000621371,
	"lea" : 0.000179986, "fthm" : 0.546807, "cable" : 0.005399568, 
	"nautical mile" : 0.000539957, "link" : 4.970969538, "rod" : 0.198839}, 
	#area
	"m^2" : {"in^2" : 1550, "ft^2" : 10.7639, "yd^2" : 1.19599, 
	"ml^2" : 3.861e-7, "perch" : 0.198839**2, "rood" : 0.198839 * 0.00497096, 
	"acre" : 0.00497096 * 0.0497097, "hectare" : 1e-4},
	#volume
	"l" : {"in^3" : 61.0237, "ft^3" : 0.0353147, "floz" : 33.814, 
	"tbsp" : 67.628, "cup" : 4.16667, "pt" : 2.11338, "qt" : 1.05669, 
	"gal" : 0.264172},
	#mass
	"g" : {"gr" : 15.4324, "dr" : 0.5643833912, "oz" : 0.035274, 
	"lb" : 0.00220462, "st" : 0.000157473, "qr" : 0.000078737, 
	"qtr" : 0.000078737, "cwt" : 1.9684e-5, "t" : 1.1023e-6, 
	"slug" : 6.85218e-5},
	#temperature
	"C" : ["F"],

}

def main():
	argparser = argparse.ArgumentParser()
	argparser.add_argument("inputAmount")
	argparser.add_argument("inputUnit")
	argparser.add_argument("outputUnit")
	args = argparser.parse_args()

	baseInput = getBaseUnit(args.inputUnit)
	baseOutput = getBaseUnit(args.outputUnit)
	if(baseInput[0] in siUnitsToImperial):
		#converting from metric to imperial
		if(args.outputUnit in siUnitsToImperial[baseInput[0]]):
			#ensure converting correct kind of measurement
			#ie. distance to distance
			noPrefix = ( ( float( args.inputAmount ) ) * siPrefixes[baseInput[1]] )
			finalVal = 0
			if(baseInput[0] == "C"):
				finalVal = (noPrefix * 1.8) + 32
			else:
				finalVal = noPrefix * siUnitsToImperial[baseInput[0]][args.outputUnit]
			print(str(finalVal)+args.outputUnit)
		else:
			print("Can't convert from "+baseInput[0]+" to "+args.outputUnit)
	elif( inValueLists(baseInput[0], siUnitsToImperial)):
		#converting from imperial to metric
		if(baseInput[0] in siUnitsToImperial[baseOutput[0]]):
			#ensure converting correct kind of measurement
			#ie. distance to distance
			finalVal = 0
			if(baseInput[0] == "F"):
				finalVal = (float(args.inputAmount) - 32 ) / 1.8
			else:
				finalVal = (float(args.inputAmount) / siUnitsToImperial[baseOutput[0]][baseInput[0]]) /siPrefixes[baseOutput[1]]
			print(str(finalVal)+args.outputUnit)
		else:
			#invalid outputUnit
			print("Can't convert from "+baseInput[0]+" to "+args.outputUnit)
	else:
		#invalid input unit
		print("Invalid input unit")


def getBaseUnit(iUnit=""):
	if(iUnit in siUnitsToImperial or inValueLists(iUnit, siUnitsToImperial)):
		return (iUnit, "")
	else:
		#get si prefix
		unitInfo = list(iUnit)
		base = ""
		prefix = ""
		if(unitInfo[0]+unitInfo[1] == "da"):
			prefix = "da"
			base = "".join(unitInfo[2:])
		else:
			base = "".join(unitInfo[1:])
			prefix = unitInfo[0]
		return (base, prefix)

def inValueLists(v, d):
	for val in d.values():
		if(v in val):
			return True
	return False

if __name__ == "__main__":
	main()
