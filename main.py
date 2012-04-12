#!/usr/bin/python
from os import getcwd, listdir, sep, remove, error, path
from tools.directories import Build
from tools.pdf import Explode, ConvertToSVG
import time

# Directories names
currentpath = getcwd()
tmpdir = 'tmp'
pdfdir = 'pdf'
svgdir = 'svg'
logfile = 'execution.log'

try:
	if path.isfile(logfile):
		remove(logfile)
	out = open(logfile, 'w')
	out.close()
except error, value:
	print value[1]


dirs = [tmpdir, pdfdir, svgdir]

def logthis(newtext):
	log = currentpath + sep + logfile
	input = open(log, 'r')
	text = input.read()
	input.close()
	output = open(log, 'w')
	output.write(text + newtext +'\n')
	output.close()

logthis(time.ctime())
logthis('\nBegin the convertion\n\n')

# Creates a directory structure.
now = Build()
for newdir in dirs:
	logthis('Create a directory structure to: %s.' % newdir)
	now.createDirIfNotExist(newdir, currentpath)


# Normalize name of the pdfs and cut and paste pdf in respective dir.
logthis('\nNormalize name of the pdfs.\n')
now.normalizeNameOfPdfs(listdir(tmpdir), tmpdir)


# Buid the dir structure for pdf and svg.
for pdfnamedir in listdir(tmpdir):
	pdfnamedir = pdfnamedir.replace('.pdf', '')
	
	logthis('Create a directory structure to: %s.' % (pdfdir + sep + pdfnamedir))
	now.createDirStructure(pdfdir + sep + pdfnamedir)
	logthis('Create a directory structure to: %s.' % (svgdir + sep + pdfnamedir))
	now.createDirStructure(svgdir + sep + pdfnamedir)


# Cut the pdf of tmp dir to pdf name dir.
logthis('\nCut the pdf files of %s to %s.\n' %(tmpdir + '/', pdfdir + '/'))
now.cutFiles(tmpdir, pdfdir)


# Performs the separate pages process
action = Explode()
for currentdir in listdir(pdfdir):
	logthis('Performs the separate pdf pages on %s.' %(pdfdir + sep + currentdir))
	action.explodePages(pdfdir + sep + currentdir)


# Convert each pdf page to svg file
action = ConvertToSVG()
logthis('\n')
for currentdir in listdir(pdfdir):
	logthis('Converting each pdf page of %s to svg' %(pdfdir + sep + currentdir))
	action.converPdfToSvg(pdfdir + sep + currentdir, svgdir + sep + currentdir)


logthis('Finish conversions.')