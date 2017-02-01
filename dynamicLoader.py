__author__ = "Nathan Evans"

"""
This script takes in a .c file and creates a .so file, allowing the code from the 
original .c file to be accessed in python
"""
import argparse, os, subprocess

argparser = argparse.ArgumentParser()
argparser.add_argument('moduleName', help='enter the name that you would like to assign to the completed module')
argparser.add_argument('--majorVersion', help='enter the major version of the module to be built', default='1')
argparser.add_argument('--minorVersion', help='enter the minor version of the module to be built', default='0')
argparser.add_argument('source', help='enter the name of the .c file to be built')
argparser.add_argument('--description', help='enter a short description of the package to be built', default='')
argparser.add_argument('--author', help='enter the name of the author of C code to be built', default='anonymous')
argparser.add_argument('--authorEmail', help='enter the email address of the author of the C code to be built', default='')
argparser.add_argument('--url', help='enter the url of the website that documents the C code to be built', default='')
argparser.add_argument('--longDescription', help='enter a longer description of the C code to be built', default='')
args = argparser.parse_args()

print("Preparing to generate setup file")
fileName = "setupSpam.py"
subprocess.run(["rm", "-rf", fileName])
print("Writing setup file")
target = open(fileName, 'w')
target.write("from distutils.core import setup, Extension\n"+
	"module1 = Extension('"+args.moduleName+"',\n"+
	"\tdefine_macros = [('MAJOR_VERSION', '"+args.majorVersion+"'),\n"+
	"\t\t\t('MINOR_VERSION', '"+args.minorVersion+"')],\n"+
	"\tsources = ['"+args.source+"'])\n"+
	"setup(name = 'PackageName',\n"+
	"\tversion = '"+args.majorVersion+"."+args.minorVersion+"',\n"+
	"\tdescription = '"+args.description+"',\n"+
	"\tauthor = '"+args.author+"',\n"+
	"\tauthor_email = '"+args.authorEmail+"',\n"+
	"\turl = '"+args.url+"',\n"+
	"\tlong_description = ''' "+args.longDescription+" ''',\n"+
	"\text_modules = [module1])")

target.close()
print("Finished writing setup file\nBuilding module")
subprocess.run(["python", "setupSpam.py", "build"])
print("moving .so file")
for fileList in os.walk("build"):
	if(fileList[0][:len("build"+os.sep+"lib.")] == "build"+os.sep+"lib."):
		moduleFileName = fileList[2][0]
		fullFileName = fileList[0]+os.sep+moduleFileName
		print(fullFileName)
		subprocess.run(["cp", fullFileName, moduleFileName])
		break
print("Cleaning up")
subprocess.run(["rm", "-rf", "build"])
subprocess.run(["rm", "-rf", fileName])
print("DONE!")
print("If your .so file doesn't exist in this directory, the original .c code probably threw an error in the debugger")
