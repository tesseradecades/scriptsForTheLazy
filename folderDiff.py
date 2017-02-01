import argparse, os

def main():
	argparser = argparse.ArgumentParser()
	argparser.add_argument("folder1", help="enter the first folder for comparison")
	argparser.add_argument("folder2", help="enter the second folder for comparison")
	args = argparser.parse_args()
	folder1 = args.folder1
	folder2 = args.folder2
	f = []
	for fileList in os.walk(folder1):
		if(len(fileList) > 1):
			for x in fileList[1:]:
				f+=x
		else:
			print(folder1+" is empty")
		break
	f2 =[]
	for fileList in os.walk(folder2):
		if(len(fileList) > 1):
			for x in fileList[1:]:
				f2+=x
		else:
			print(folder2+" is empty")
		break
	fOnly = []
	for fName in f:
		if(fName not in f2):
			fOnly.append(fName)
	f2Only = []
	for fName in f2:
		if(fName not in f):
			f2Only.append(fName)
	print(folder1)
	print(fOnly)
	print("\n*****************************************************************\n"+folder2)
	print(f2Only)


if __name__ == "__main__":
	main()
