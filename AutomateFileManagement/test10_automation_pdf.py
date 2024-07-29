# @time     ：2024/7/26 14:57
# @author   : 莉光哈哈哈
# @file     : test10_automation_pdf.py
# @software : PyCharm
'''
1.从pdf中提取文本
'''
import PyPDF2


def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    return text


'''
2.合并多个pdf
'''
import PyPDF2


def merge_pdfs(input_paths, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    for path in input_paths:
        with open(path, 'rb') as f:
            pdf_merger.append(f)

    with open(output_path, 'wb') as f:
        pdf_merger.write(f)


'''
3.添加密码保护
'''
import PyPDF2


def add_password_protection(input_path, output_path, password):
    with open(input_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)
        pdf_writer.encrypt(password)
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
