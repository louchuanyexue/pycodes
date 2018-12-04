from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter

def get_reader(filename,password=None):
    try:
        old_file = open(filename, 'rb')
    except IOError as err:
        print('文件打开失败！' + str(err))
        return None

    # 创建读实例
    pdf_reader = PdfFileReader(old_file, strict=False)

    # 解密操作
    if pdf_reader.isEncrypted:
        if password is None:
            print('%s文件被加密，需要密码！' % filename)
            return None
        else:
            if pdf_reader.decrypt(password) != 1:
                print('%s密码不正确！' % filename)
                return None
    if old_file in locals():
        old_file.close()
    return pdf_reader
def split_by_pages(filename, pages, password=None):
    """
    将文件按照页数进行平均分割
    :param filename: 所要分割的文件名
    :param pages: 分割之后每个文件对应的页数
    :param password: 如果文件加密，需要进行解密操作
    :return:
    """
    # 得到Reader
    pdf_reader = get_reader(filename, password)
    if pdf_reader is None:
        return
    # 得到总的页数
    pages_nums = pdf_reader.numPages

    if pages <= 1:
        print('每份文件必须大于1页！')
        return

    # 得到切分之后每个pdf文件的页数
    pdf_num = pages_nums // pages + 1 if pages_nums % pages else int(pages_nums / pages)

    print('pdf文件被分为%d份，每份有%d页！' % (pdf_num, pages))

    # 依次生成pdf文件
    for cur_pdf_num in range(1, pdf_num + 1):
        # 创建一个新的写实例
        pdf_writer = PdfFileWriter()
        # 生成对应的文件名称
        split_pdf_name = "".join(filename)[:-1] + '_' + str(cur_pdf_num) + '.pdf'
        # 计算出当前开始的位置
        start = pages * (cur_pdf_num - 1)
        # 计算出结束的位置，如果是最后一份就直接返回最后的页数，否则用每份页数*已经分好的文件数
        end = pages * cur_pdf_num if cur_pdf_num != pdf_num else pages_nums
        # print(str(start) + ',' + str(end))
        # 依次读取对应的页数
        for i in range(start, end):
            pdf_writer.addPage(pdf_reader.getPage(i))
        # 写入文件
        pdf_writer.write(open(split_pdf_name, 'wb'))


get_reader(r"C:\Users\15203\Desktop\3.pdf")
split_by_pages(r"C:\Users\15203\Desktop\3.pdf", 5)
