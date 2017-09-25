import json,sys, timeit, functools
import xml.etree.ElementTree as et
from flatten_json import flatten
from memory_profiler import memory_usage,profile
	
"""
Queries the xml for the child nodes at every level
"""
@profile
def queryXML(xmlData):
	root = xmlData.getroot()
	searchString = "."
	retList = root.findall(searchString)
	returnList=[retList]
	while len(retList) > 0:
		#compose new search string to query for next generation
		searchString+="/*"
		retList = root.findall(searchString)
		returnList.append(retList)
	return returnList

@profile
def queryJSON(jsonData):
	flat = flatten(jsonData)
	for x in flat.keys():
		#treating like a dictionary to query by key
		qResult = flat[x]
	return flat

@profile
def processXML(fName):
	return et.parse(fName)

@profile
def processJSON(fName):
	f = open(fName)
	data = json.load(f)
	f.close()
	return data

def getMethod(command, xorj):
	if(command=="process" and xorj=="xml"):
		return processXML
	elif(command=="process" and xorj=="json"):
		return processJSON
	elif(command=="query" and xorj=="xml"):
		return queryXML
	elif(command=="query" and xorj=="json"):
		return queryJSON
	
def execute(command, fileName, xorj,iterations):
	method = getMethod(command, xorj)
	trueFname=""
	if(xorj=="xml"):
		trueFname = "xmlData/"+fileName+".xml"
	elif(xorj=="json"):
		trueFname = "jsonData/"+fileName+".json"
	data = method(trueFname)
	t = timeit.Timer(functools.partial(method, trueFname))
	avgTime = t.timeit(iterations)/iterations
	print("Average ",command," time:\t",avgTime,"\tOver ",iterations," iterations.")

def main():
	command = sys.argv[1]
	baseFile = sys.argv[2]
	xOrJ = sys.argv[3]
	try:
		iterations = int(sys.argv[4])
	except:
		iterations = 5
	execute(command,baseFile,xOrJ,iterations)

	return None

if __name__ == "__main__":
	main()