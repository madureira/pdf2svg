from os import sep, listdir, mkdir, makedirs, rename
from shutil import copyfile


class Build:

    def normalize_pdf_names(self, pdf_names, location):
        for name in pdf_names:
            if '.pdf' in name:
                new_file_name = name.replace('.pdf', '')
                new_file_name = self.remove_special_chars(new_file_name)
                new_file_name = new_file_name.upper() + '.pdf'
                self.rename_file(name, new_file_name, location)

    @staticmethod
    def ensure_dir(dir_name, target_dir):
        files_and_dirs = listdir(target_dir)
        if dir_name not in files_and_dirs:
            try:
                mkdir(target_dir + sep + dir_name)
            except(ValueError, KeyError):
                print(ValueError)

    @staticmethod
    def remove_special_chars(text):
        special_chars = ['_', '-', '$', '.', ' ', '*', '']
        for char in special_chars:
            text = text.replace(char, '')
        return text

    @staticmethod
    def rename_file(current_name, new_name, dir_name):
        dir_name = dir_name + sep
        if current_name != new_name:
            try:
                rename(dir_name + current_name, dir_name + new_name)
            except(ValueError, KeyError):
                print(ValueError)

    @staticmethod
    def cut_files(current_path, target_path):
        current_files = listdir(current_path)
        for pdf in current_files:
            if pdf != '.keep':
                new_pdf_dir = pdf.replace('.pdf', '')
                old_location = current_path + sep
                new_location = target_path + sep + new_pdf_dir + sep
                copyfile(old_location + pdf, new_location + pdf)

    @staticmethod
    def create_dir_structure(dir_structure):
        try:
            makedirs(dir_structure)
        except(ValueError, KeyError):
            print(ValueError)
