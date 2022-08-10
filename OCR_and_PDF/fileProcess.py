import cv2
import numpy as np
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

OCR_reader = None


def txt_Processor(file_path):
    # print('begin txt process')
    text = ''
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            text = text + line.replace('\n', '')
    return text


def parse(path):
    output_string = StringIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    text = output_string.getvalue()
    text = text.replace('\n', '')
    return text


def pdf_Processor(file_path):
    # print('begin pdf process')
    text = parse(file_path)
    '''
    也许这里需要再对读取出来的文本有些处理，这个具体要与前端沟通好
    '''
    return text


def img_Processor(file_path, bi_thresh):
    # print('begin image process')
    img = cv2.imread(file_path)
    if get_file_type(file_path) == 'png':
        imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换成灰度图像
    img_ready = pretreatment(imgray, bi_thresh)
    result = OCR_reader.readtext(img_ready, detail=0)
    post_line = ''
    for s in result:
        post_line = post_line + s
    return post_line


def pretreatment(img, bi_thresh):
    kernel1 = np.ones((2, 2), np.uint8)
    kernel2 = np.ones((1, 1), np.uint8)
    '''
    这两步腐蚀和膨胀不一定需要，因为图片相对简单，直接使用二值化那一行也是可以的
    '''
    img = cv2.erode(img, kernel=kernel1, iterations=1)  # 腐蚀（黑色腐蚀白色），连接字幕边框
    img = cv2.dilate(img, kernel=kernel1, iterations=1)  # 膨胀（白色膨胀），恢复字母体积

    ret, img = cv2.threshold(img, bi_thresh, 255, cv2.THRESH_BINARY)  # 二值化
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    img = cv2.dilate(img, kernel=kernel2, iterations=1)  # 膨胀，滤除黑色噪点
    img = cv2.erode(img, kernel=kernel2, iterations=1)  # 膨胀，滤除黑色噪点
    return img


def get_file_type(file_path):
    suffix = file_path.split('.')[-1]
    return suffix


def getContent(file_path):
    bi_thresh = 150  # 图片二值化时候的阈值，范围为0-255

    # OCR_reader = easyocr.Reader(['ch_sim', 'en'])  # only need to run once，代表easyOCR可以使用简体中文和英文

    suffix = get_file_type(file_path)
    # print('suffix: ', suffix)
    if suffix == 'pdf':
        text = pdf_Processor(file_path)
    elif suffix == 'jpg' or suffix == 'jpeg' or suffix == 'png':
        text = img_Processor(file_path, bi_thresh)
    elif suffix == 'txt':
        text = txt_Processor(file_path)
    else:
        text = '错误的文件格式！'
    return text


if __name__ == '__main__':
    file_path = './1.txt'
    getContent(file_path)
