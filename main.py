#!/usr/bin/python
from os import getcwd, listdir, sep
from tools.directories import Build
from tools.pdf import Explode, ConvertToSVG
import time


# Directories names
current_path = getcwd()
tmp_dir = 'tmp'
pdf_dir = 'pdf'
svg_dir = 'svg'
dirs = [tmp_dir, pdf_dir, svg_dir]


def log(new_text):
    print(new_text)


log(time.ctime())
log('\nBegin the conversion\n\n')


build = Build()


# Creates a directory structure.
for new_dir in dirs:
    log('Create a directory structure to: %s.' % new_dir)
    build.ensure_dir(new_dir, current_path)


# Normalize pdf names, cut and paste pdf in respective dir.
log('\nNormalize PDF\'s names.\n')
build.normalize_pdf_names(listdir(tmp_dir), tmp_dir)


# Build the dir structure for pdf and svg.
for pdf_dir_name in listdir(tmp_dir):
    if pdf_dir_name != '.keep':
        pdf_dir_name = pdf_dir_name.replace('.pdf', '')
        log('Create a directory structure to: %s.' % (pdf_dir + sep + pdf_dir_name))
        build.create_dir_structure(pdf_dir + sep + pdf_dir_name)
        log('Create a directory structure to: %s.' % (svg_dir + sep + pdf_dir_name))
        build.create_dir_structure(svg_dir + sep + pdf_dir_name)


# Cut the pdf on tmp dir from pdf name dir.
log('\nCut the pdf files from %s to %s.\n' % (tmp_dir + '/', pdf_dir + '/'))
build.cut_files(tmp_dir, pdf_dir)


# Performs the separate pages process.
action = Explode()
for current_dir in listdir(pdf_dir):
    log('Performs the separate pdf pages on %s.' % (pdf_dir + sep + current_dir))
    action.explode_pages(pdf_dir + sep + current_dir)


# Convert each pdf page to svg file
action = ConvertToSVG()
log('\n')
for current_dir in listdir(pdf_dir):
    log('Converting each pdf page of %s to svg' % (pdf_dir + sep + current_dir))
    action.convert_pdf_to_svg(pdf_dir + sep + current_dir, svg_dir + sep + current_dir)


log('\n\nConversion finish!')
