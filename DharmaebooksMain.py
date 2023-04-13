import urllib.request
import requests
import urllib.parse
import json
from lxml import etree
import os
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

if __name__ == '__main__':
    # ar="https://dharmaebooks.org/authors/"
    # res = create_request(ar)
    # content = get_content(res)
    # htmlName="Authors • dharmaebooks.org • Library of Buddhist and Tibetan Ebooks"
    # down_load(htmlName,content,"html")
    # xpath解析本地文件
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse("D:\pythonProject\Dharmaebooks\Authors • dharmaebooks.org • Library of Buddhist and Tibetan Ebooks.html", parser=parser)
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
    print(list_link2)
    list_link2.remove("https://dharmaebooks.org/tag/tashi-norbu/")
    for link in list_link2:
        if str(link).startswith("https://dharmaebooks.org/tag"):
            OUTPUT_ROOT = "D:/pythonProject/Dharmaebooks/1aaa"
            folderName = str(link).split("https://dharmaebooks.org/tag/")[1].strip("/")
            print(folderName)
            output_dir = OUTPUT_ROOT + "/" + folderName + "/"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                rs1 = create_request(link)
                c1 = get_content(rs1)
                print("正在下载" + folderName)
                down_load(output_dir + folderName, c1, "html")
                # 解析html
                # output_dir="D:/pythonProject/Dharmaebooks/potowa" +"/"
                # htmlName="potowa"
                parser = etree.HTMLParser(encoding="utf-8")
                tree = etree.parse(output_dir + folderName + ".html", parser=parser)
                list_zip = tree.xpath('//body//a[@title="ད་དུང་བལྟ་ཀློག • READ MORE • 閱讀更多"]//@href')
                print(list_zip)
                for linkZi in list_zip:
                    ZIHtmlName = str(linkZi).split("https://dharmaebooks.org/")[1].strip("/")
                    rsZi = create_request(linkZi)
                    contentZi = get_content(rsZi)
                    print("正在下载 " + ZIHtmlName+".html")
                    down_load(output_dir + ZIHtmlName, contentZi, "html")
                    # 解析ZI html
                    treeZi = etree.parse(output_dir + ZIHtmlName + ".html", parser=parser)
                    list_books = treeZi.xpath('//body//a[@title="epub"]//@href')
                    list_books_Names = treeZi.xpath('//body//a[@title="epub"]//text()')
                    index = 0
                    if len(list_books):
                       for bookLink in list_books:
                           print("正在下载EPUB_BOOK " + list_books_Names[index])
                           down_loadEPUB(str(bookLink),output_dir + list_books_Names[index])
                           index += 1

                    else:
                        print("pdf")
                        list_booksPDF = treeZi.xpath('//body//a[@title="pdf"]//@href')
                        list_booksPDF_Names = treeZi.xpath('//body//a[@title="pdf"]//text()')
                        index2 = 0
                        if len(list_booksPDF):
                            for bookPDFLink in list_booksPDF:
                                print("正在下载PDF_BOOK " + list_booksPDF_Names[index2])
                                down_loadPDF(str(bookPDFLink), output_dir + list_booksPDF_Names[index2])
                                index2 += 1






