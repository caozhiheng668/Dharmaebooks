import urllib.request
import requests
import urllib.parse
import json
from lxml import etree
import os
import xlsxwriter
# ctrl + shift  + X   小黑窗口
def create_request(ar):
    base_url = "http://www.dharmadownload.net/"
    nurl = ar
    data = {}

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    request = urllib.request.Request(url=nurl, headers=headers, data=data)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(tdName, content,type):
    with open(tdName + '.'+type, 'w', encoding='utf-8')as fp:
        fp.write(content)

def down_loadEPUB(url,epubName):
    # 下载EPUB
    r = requests.get(url)
    # 写入EPUB
    with open(epubName+".epub", "wb") as f:
        f.write(r.content)

def down_loadPDF(url,pdfName):
    # 下载EPUB
    r = requests.get(url)
    # 写入EPUB
    with open(pdfName+".pdf", "wb") as f:
        f.write(r.content)

def down_xiangQing_html(row,mulu,jianJie,lianjie,count,worksheet):
    output_dir = mulu
    # rs22 = create_request(lianjie)
    # c22 = get_content(rs22)
    # down_load(output_dir+str(count) , c22, "html")
    # print("正在下载详情页面")

     # 解析HTML
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse(output_dir + str(count)+".html", parser=parser)

    list_tg = tree.xpath('//body//footer[@class="entry-footer cf"]//text()')
    tag = str(list_tg)
    list_tp = tree.xpath('//*[@id="x-section-1"]/div/div[1]//text()')
    title = str(list_tp)

    list_publish = tree.xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td[2]//text()')
    if len(list_publish) == 0 :
        list_publish = tree.xpath('//*[@id="x-legacy-panel-1"]/table/thead/tr[3]/td[2]//text()')
        if len(list_publish) ==0 :
            list_publish = tree.xpath('//*[@id="x-legacy-panel-1"]/table/thead/tr[1]/td[2]//text()')
            if len(list_publish) == 0:
                list_publish=[""]

    finalAuthor = ''
    list_author = tree.xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td[2]//text()')
    if len(list_author) == 0 :
        list_author = tree.xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[1]/td[2]/text()')
        if len(list_author) == 0 :
            list_author = tree.xpath( '//*[@id="x-legacy-panel-1"]/table/thead/tr[2]/td[2]//text()')
            if len(list_author) == 0:
                list_author = tree.xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td[2]/p//text()')
                if len(list_author) == 0:
                    list_author = tree.xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[2]/td[2]//text()')
                    if len(list_author) == 0:
                        list_author=[""]
    if len(list_author) !=0:
        for aname in list_author:
            finalAuthor +=aname +","
    finalAuthor = str(finalAuthor.split(","[0]))





    list_yuYan = tree.xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[3]/td[2]//text()')
    if len(list_yuYan) == 0 :
        list_yuYan = tree.xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[3]/td[2]/p//text()')
        if len(list_yuYan) == 0:
            list_yuYan = tree.xpath('//*[@id="x-legacy-panel-1"]/table/thead/tr[3]/td[2]//text()')
            if len(list_yuYan) == 0:
                list_yuYan = tree.xpath('//*[@id="x-legacy-panel-1"]/table/tbody/tr[3]/td[2]/text()')
                if len(list_yuYan) == 0:
                    list_yuYan = tree.xpath( '//*[@id="x-legacy-panel-1"]/table/thead/tr[3]/td[2]//text()')
                    if len(list_yuYan) == 0:
                        list_yuYan=[""]
    list_yuYan = str(list_yuYan)

    lujing = ''
    list_wenjian = tree.xpath('//*[@id="my-btn"]/a//text()')
    if len(list_wenjian)!=0:
        wenjianName = list_wenjian[0]
        lujing = mulu +wenjianName
    else:
        list_wenjian = tree.xpath('//*[@id="x-section-1"]/div/div[2]/div[3]//text()')
        if len(list_wenjian) == 0:
            list_wenjian = tree.xpath('//*[@id="x-section-1"]/div/div[2]/div[2]//text()')
            if len(list_wenjian) ==0:
                lujing=''
            else:
                wenjianName = list_wenjian[0]
                lujing = mulu + wenjianName




    worksheet.write(row, 0, row)
    worksheet.write(row, 1, title)
    worksheet.write(row, 2, list_yuYan)
    worksheet.write(row, 3, finalAuthor)
    worksheet.write(row, 4, str(list_publish))
    worksheet.write(row, 5, jianJie)
    worksheet.write(row, 6, lianjie)
    worksheet.write(row, 7, tag)
    worksheet.write(row, 8, lujing)


def handleData(output_dir,link):
    global parser, tree, row

    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)
    # rs1 = create_request(link)
    # c1 = get_content(rs1)
    # print("正在下载" + folderName)
    # down_load(output_dir + folderName, c1, "html")
    mulu2 = output_dir
    # 解析html
    # output_dir="D:/pythonProject/Dharmaebooks/potowa" +"/"
    # htmlName="potowa"
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse(output_dir + folderName + ".html", parser=parser)
    count = 1
    list_zip = tree.xpath('//a[@title="ད་དུང་བལྟ་ཀློག • READ MORE • 閱讀更多"]//@href')
    if len(list_zip) == 1:
        list_tp = tree.xpath('//*[@id="x-site"]/main/div[3]/div/div/div/div/div/div/article/a/div/div/h3')
        list_jianJie = tree.xpath(
            '//*[@id="x-site"]/main/div[3]/div/div/div/div/div/div/article/div//text()')

        if len(list_jianJie) == 0:
            list_jianJie = tree.xpath(
                '//*[@id="x-site"]/main/div[3]/div/div/div/div/div/div/article/div/p[2]/text()')
        oneAbstract = str(list_jianJie)
        oneLink = str(
            tree.xpath('//*[@id="x-site"]/main/div[3]/div/div/div/div/div/div/article/div/a/@href')[0])
        down_xiangQing_html(row, mulu2, oneAbstract, oneLink, count, worksheet)
        row += 1

    else:
        count = 1
        while count < 100:
            # 题目
            baseTopic = '//*[@id="x-site"]/main/div[3]/div/div/div/div/div/div['
            finalTopic = baseTopic + str(count) + ']/article/a/div/div/h3'
            list_Topic = tree.xpath(finalTopic)
            if len(list_Topic) == 0:
                break
            # 简介
            baseAbtract = '//*[@id="x-site"]/main/div[3]/div/div/div/div/div/div['
            finalAbstract = baseAbtract + str(count) + ']/article/div/p[3]/text()'
            list_Abstract = tree.xpath(finalAbstract)
            if len(list_Abstract) == 0:
                finalAbstract = baseAbtract + str(count) + ']/article/div/p[2]/text()'
                list_Abstract = tree.xpath(finalAbstract)
            if len(list_Abstract) == 0:
                abstractOne = ''
            else:
                abstractOne = str(list_Abstract[0])
            # 法本详情链接
            baseLink = '//*[@id="x-site"]/main/div[3]/div/div/div/div/div/div['
            finalLink = baseLink + str(count) + ']/article/div/a//@href'
            linkOne = str(tree.xpath(finalLink)[0])
            down_xiangQing_html(row, mulu2, abstractOne, linkOne, count, worksheet)

            count += 1
            row += 1




if __name__ == '__main__':
    # xpath解析本地文件
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse("D:\pythonProject\Dharmaebooks\Authors • dharmaebooks.org • Library of Buddhist and Tibetan Ebooks.html", parser=parser)
    # list_link = tree.xpath('//body//a//@href')
    # list_link2 = list(set(list_link))

    list_link = tree.xpath('//*[@id="cs-content"]/div[2]//a//@href')
    list_link2 = list(set(list_link))

    # list_link2.remove("https://dharmaebooks.org/tag/tashi-norbu/")
    # #list_link2.remove("/cdn-cgi/l/email-protection#714e0204131b1412054c300405191e030257101c014a131e15084c3914085d5105191e0416190551081e04511c1816190551141f1b1e0851051918025051321914121a511805511e0405510619141f51081e0451191007145110511219101f12144b5119050501024b5e5e151910031c1014131e1e1a025f1e03165e100405191e03025e', 'https://dharmaebooks.org/tag/langri-thangpa/")
    # list_link2.remove("/cdn-cgi/l/email-protection#48773b3d2a222d2b3c75093d3c20273a3b6e292538732a272c3175002d3164683c20273d2f203c6831273d6825212f203c682d26222731683c20213b69680b202d2b2368213c68273d3c683f202d266831273d6820293e2d6829682b2029262b2d7268203c3c383b7267672c20293a25292d2a2727233b66273a2f67293d3c20273a3b67")
    # list_link2.remove("https://dharmaebooks.org/authors/")
    # list_link2.remove("https://dharmaebooks.org/category/dharma-practice/")
    # list_link2.remove("https://dharmaebooks.org/tag/english/")
    # list_link2.remove("https://www.facebook.com/dharmaebooks.org/?ref=bookmarks")
    # list_link2.remove("https://wildlotusart.com/privacy-policy/")
    # list_link2.remove("https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en")
    # list_link2.remove("https://creativecommons.org/licenses/by-nc-nd/4.0/")
    # list_link2.remove("https://dharmaebooks.org/wp-content/plugins/newsletter-facebook/login.php")
    # list_link2.remove("http://dharma-treasure.org")
    # list_link2.remove("https://dharmaebooks.org")
    # list_link2.remove("#share")
    # list_link2.remove("https://www.youtube.com/channel/UCLyaZ8oBGAg7syeQvEpyb7g")
    # list_link2.remove("https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh_TW")
    # list_link2.remove("https://twitter.com/DharmaEbooks")
    # list_link2.remove("https://dharmaebooks.org/")
    # list_link2.remove("https://dharmaebooks.org/tag/chinese/")
    # list_link2.remove("https://dharmaebooks.org/category/lamrim/")
    # list_link2.remove("https://dharmaebooks.org/newsletter-subscription/")
    # list_link2.remove("https://dharmaebooks.org/dharma-ebooks-introduction/")
    # list_link2.remove("https://dharmaebooks.org/category/philosophy/")
    # list_link2.remove("https://dharmaebooks.org/category/prayer-books/")
    # list_link2.remove("https://dharmaebooks.org/category/poetics/")
    # list_link2.remove("https://dharmaebooks.org/category/canon/")
    # list_link2.remove("https://dharmaebooks.org/ebooks/")
    # list_link2.remove("https://dharmaebooks.org/videos/")
    # list_link2.remove("https://dharmaebooks.org/category/108-translations-ebooks/")
    # list_link2.remove("https://dharmaebooks.org/epub-guide/videos/")
    # list_link2.remove("https://dharmaebooks.org/privacy-policy/")
    # list_link2.remove("https://dharmaebooks.org/publishers/")
    # list_link2.remove("https://dharmaebooks.org/category/advice/")
    # list_link2.remove("https://dharmaebooks.org/category/history/")
    # list_link2.remove("https://dharmaebooks.org/category/mahamudra/")
    # list_link2.remove("https://dharmaebooks.org/category/collected-works/")
    # list_link2.remove("https://dharmaebooks.org/category/kagyu-guncho/")
    # list_link2.remove("https://dharmaebooks.org/contact/")
    # list_link2.remove("https://dharmaebooks.org/epub-guide/")
    # list_link2.remove("/cdn-cgi/l/email-protection#714e0204131b1412054c300405191e030257101c014a131e15084c3914085d5105191e0416190551081e04511c1816190551141f1b1e0851051918025051321914121a511805511e0405510619141f51081e0451191007145110511219101f12144b5119050501024b5e5e151910031c1014131e1e1a025f1e03165e100405191e03025e")
    # list_link2.remove("https://dharmaebooks.org/category/teachings/")

    list_link2.remove("https://dharmaebooks.org/tag/tashi-norbu/")
    print(list_link2)

    # 写入excel
    workbook = xlsxwriter.Workbook('dharmaebooks.xlsx')  # 创建一个excel文件
    worksheet = workbook.add_worksheet('目录')  # 在文件中创建一个名为目录的sheet,不加名字默认为sheet1
    worksheet.write(0, 0, "ID")
    worksheet.write(0, 1, "title")
    worksheet.write(0, 2, "languages")
    worksheet.write(0, 3, "author")
    worksheet.write(0, 4, "publisher")
    worksheet.write(0, 5, "abstract")
    worksheet.write(0, 6, "url")
    worksheet.write(0, 7, "tag")
    worksheet.write(0, 8, "location")
    row = 1
    rock = 0
    for link in list_link2:
        if str(link).startswith("https://dharmaebooks.org/tag"):
            OUTPUT_ROOT = "D:/pythonProject/Dharmaebooks/1aaa"
            folderName = str(link).split("https://dharmaebooks.org/tag/")[1].strip("/")
            print(folderName)
            output_dir = OUTPUT_ROOT + "/" + folderName + "/"
            handleData(output_dir,link)
            for i in range(2,11):
                link2 = link +'page/'+str(i)+"/"

                try:
                    rs2 = create_request(link2)
                    c2 = get_content(rs2)
                    print("下载第"+str(i)+"页")
                    output_dir2 = output_dir+ "/" + str(i) + "/"
                    handleData(output_dir2, link2)
                except urllib.error.HTTPError as e:
                    print(e.code)
                    break

        #     rock += 1
        # if rock == 3:
        #     break



workbook.close()

