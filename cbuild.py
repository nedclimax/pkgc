import os
import sys
import getopt
import subprocess

def clean(dir):
	test = os.listdir(dir)
	for item in test:
		if os.name == "nt":
			if item.endswith(".exe"):
				os.remove(os.path.join(dir, item))
			if item.endswith(".obj"):
				os.remove(os.path.join(dir, item))
		else:
			if item.endswith(".out"):
				os.remove(os.path.join(dir, item))
			if item.endswith(".o"):
				os.remove(os.path.join(dir, item))
		if item.endswith(".pdb"):
			os.remove(os.path.join(dir, item))
		if item.endswith(".ilk"):
			os.remove(os.path.join(dir, item))

try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:o:c",["help","idir=","odir=","clean"])
except getopt.GetoptError:
	print('[Usage]: cgen.py -i <inputdir> -o <outputdir>')
	sys.exit(2)

inputdir = ""
outputdir = ""

for opt, arg in opts:
	if opt == "-h" or opt == "--help":
		print("[Usage]: cgen.py -i <inputdir> -o <outputdir>")
		sys.exit()
	elif opt in ("-i", "--idir"):
		inputdir = arg
	elif opt in ("-o", "--odir"):
		outputdir = arg
	elif opt  == "-c" or opt == "--clean":
		clean(outputdir if outputdir != "" else ".")

if inputdir != "":
	subprocess.call(["cl", "/Zi", "/FC", f"{inputdir}\*.c"])