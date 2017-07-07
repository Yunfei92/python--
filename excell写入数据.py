import requests
import xlwt
from bs4 import BeautifulSoup

url = 'http://news.people.com.cn/GB/124658/index.html'
res = requests.get(url)
# 使用UTF-8编码
res.encoding = 'GB2312'

# 使用剖析器为html.parser
soup = BeautifulSoup(res.text, 'html.parser')

indexs=soup.select('td.fblack')
titles=soup.select('a.anavy')
#遍历
for index,title in zip(indexs,titles):
    data={'index':index.get_text(),'title':title.get_text()}
    # print(data)
    # f = open(r'D:\人民网0324.txt','a',encoding='utf-8')
    # f.write(index.get_text()+' '+title.get_text()+'\n')
    # f.close()
    # 添加后缀，指定文件的名称
    # fileName = file_title + time.strftime("_%Y%m%d%H%M%S", time.localtime()) + '.xls'
    savePath='D'
    # 创建workbook对象
    curBook = xlwt.Workbook()
    # 设定编码
    curBook.encoding = 'gbk'
    # 添加Sheet表；其中cell_overwrite_ok，表示是否可以覆盖单元格
    sheet1 = curBook.add_sheet(u'sheet1', cell_overwrite_ok=True)

    # 行数
    rowNum = len(data)
    # 列数
    colNum = len(data)
    # 第二行，设定列标题
    for k in range(0, colNum):
        sheet1.write(1, k, data[k][1])

    # 第三行起，开始写入数据
    for i in range(0, rowNum):
        for j in range(0, colNum):
            sheet1.write(i + 2, j, data[i][data[j][0]])

    # 如保存xls到路径
    full_filename = os.path.join(savePath, fileName)
    # 执行保存
    curBook.save(full_filename)
  # def writeExcel(dataList , file_title , col_list , isSave = False , savePath = ''):
  #     # 添加后缀，指定文件的名称
  #     fileName = file_title + time.strftime("_%Y%m%d%H%M%S", time.localtime()) + '.xls'
  #         # 创建workbook对象
  #     curBook = xlwt.Workbook()
  #         # 设定编码
  #     curBook.encoding='gbk'
  #         # 添加Sheet表；其中cell_overwrite_ok，表示是否可以覆盖单元格
  #     sheet1 = curBook.add_sheet(u'sheet1',cell_overwrite_ok = True)
  #
  #         # 行数
  #         rowNum = len(dataList)
  #         # 列数
  #         colNum = len(col_list)
  #
  #         # 第一行，合并单元格，设定文件标题
  #         # write_merge(x, x + h, y, y + w, string, style)，x表示行，y表示列，h表示跨行个数，w表示跨列个数
  #        sheet1.write_merge(0 , 0 , 0 , colNum-1 , file_title , set_style('华文中宋',320))
  #
  #        # 第二行，设定列标题
  #        colTitleStyle = set_style('华文宋体',240)
  #        for k in range(0,colNum):
  #            sheet1.write(1 , k , col_list[k][1] , colTitleStyle)
  #
  #        # 第三行起，开始写入数据
  #        for i in range(0,rowNum):
  #           for j in range(0,colNum):
  #   sheet1.write(i+2 , j , dataList[i][col_list[j][0]])
  #
  #
  #        if isSave:
  #            # 如保存xls到路径
  #            full_filename = os.path.join(savePath , fileName)
  #            # 执行保存
  #            curBook.save(full_filename)
  #            return returnInfo()
  #        else:
  #            # 否则输出到浏览器
  #            response = HttpResponse(content_type='application/vnd.ms-excel;charset=utf-8;name="' + file_title + '.xls"')
  #            response['Content-Disposition'] = 'attachment; filename=' + fileName
  #            # 保存返回
  #            curBook.save(response)
  #          return response