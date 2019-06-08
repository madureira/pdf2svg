import json
from os import system, listdir, sep

config = {}

with open('config.json', encoding='utf-8') as data_file:
    config = json.loads(data_file.read())


class Explode:

    @staticmethod
    def explode_pages(pdf_dir):
        dir_path = pdf_dir + sep
        files_in_dir = listdir(pdf_dir)
        if len(files_in_dir) == 1:
            for pdf in files_in_dir:
                name_page = pdf.replace('.pdf', '')
                name_page = name_page + '_%02d.pdf'
                exec_command = config['pdftk'] + ' %s burst output %s ' % (dir_path + pdf, dir_path + name_page)
                system(exec_command)


class ConvertToSVG:

    @staticmethod
    def convert_pdf_to_svg(pdf_dir, svg_dir):
        pdf_path = pdf_dir + sep
        svg_path = svg_dir + sep
        pages = listdir(pdf_path)
        if len(listdir(svg_path)) != 0:
            return

        for page in pages:
            if '_' in page and page != 'doc_data.txt':
                svg_file = page.replace('.pdf', '.svg')
                exec_command = config['inkscape'] + ' %s --export-plain-svg=%s' % (
                    pdf_path + page, svg_path + svg_file)
                system(exec_command)
