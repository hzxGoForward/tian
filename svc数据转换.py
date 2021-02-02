"""本程序完成sig文件转换为xlsx文件"""
"coding: utf-8"
import os
import openpyxl

# 将单个.sig文件转换为xlsx文件
def convertsigToXlsx(openFileDir, saveFileDir):
        if os.path.isdir(openFileDir):
            return
        f = open(openFileDir)
        lines = f.readlines()
        lines = lines[25:]
        workbook = openpyxl.Workbook()
        booksheet = workbook.active
        booksheet.title = "sheet1"
        # 存储
        row = 1
        for line in lines:
            line = line.replace("\n","")
            dataList = line.split(" ")
            col = 1
            for data in dataList:
                booksheet.cell(row, col, data)
                col += 1
            row += 1
        print("正在写入: ", saveFileDir)
        workbook.save(saveFileDir)

# 转换文件
if __name__ == "__main__":
    read_dir = "/Users/tianwenxin/Desktop/data/bochangdingbiao/HR1024i Data/"
    file_list = os.listdir(read_dir)
    save_dir = "/Users/tianwenxin/Desktop/result/bochangdingbiao/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for filename in file_list:
        newfilename = filename.replace(".sig",".xlsx")
        convertsigToXlsx(read_dir + filename, save_dir + newfilename)
    print("转换完毕!")