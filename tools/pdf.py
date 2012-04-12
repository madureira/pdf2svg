from os import system, listdir, sep

class Explode:

	def explodePages(self, pdfdir):
		dirpath = pdfdir + sep
		filesindir = listdir(pdfdir)
		if len(filesindir) == 1:
			for pdf in filesindir:
				namePage = pdf.replace('.pdf', '')
				namePage = namePage + '_%02d.pdf'
				preparecommand = '/usr/bin/pdftk %s burst output %s ' %(dirpath + pdf, dirpath + namePage)
				system(preparecommand)


class ConvertToSVG:
	
	def converPdfToSvg(self, pdfdir, svgdir):
		pdfpath = pdfdir + sep
		svgpath = svgdir + sep
		pages = listdir(pdfpath)
		if len(listdir(svgpath)) == 0:
			for page in pages:
				if '_' in page:
					svgfile = page.replace('.pdf', '.svg')
					preparecommand = '/usr/local/bin/inkscape %s --export-plain-svg=%s' %(pdfpath + page, svgpath + svgfile)
					system(preparecommand)