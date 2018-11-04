import re
import urllib

def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  return html

def getImg(html):
#  reg = r'src="(.*?\.jpg)"'
  reg = r'"(.*?\.html)"'
  imgre = re.compile(reg)
  imglist = re.findall(imgre,html)
  print imglist
  txt='result.txt'  
  f = open(txt,"w+")  
  f.write(repr(imglist))
  f.close() 
  
#  x = 0
#  for imgurl in imglist:
#    urllib.urlretrieve(imgurl,'%s.jpg' % x)
#    x+=1
    
html = getHtml("https://www.baidu.com/")
getImg(html)