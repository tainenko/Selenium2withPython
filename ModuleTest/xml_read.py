'''
info.xml
<?xml version="1.0" encoding="utf-8"?>
<info>
    <base>
      <platform>Windows</platform>
      <browser>Firefox</browser>
      <url>http://www.baidu.com</url>
        <login username="admin" password="123456"/>
        <login username="guest" password="654321"/>
    </base>
    <test>
        <province>北京</province>
        <province>广东</province>
          <city>深圳</city>
          <city>珠海</city>
        <province>浙江</province>
          <city>杭州</city>
    </test>
</info>
'''

#獲得標簽信息
#首先導入xml的minidom模塊，用來處理XML文件，parse()用於打開一個XML文件，
#documentElement用於得到XML文件的唯一元素
#每一個節點都有它的nodeName、nodeValue、nodeType等屬性。nodeName為節點名稱，nodeValue為節點的值
#只對本文節點有效，nodeType為節點的類型
from xml.dom import minidom
#打開xml文檔
dom=minidom.parse('info.xml')

#得到文檔元素對象
root=dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
'''
執行結果
info
None
1
1
'''

#獲得任意標簽名
#getElementByTagName()可以通過標簽名獲取標簽，它所獲取的對象是以數組形式存放。假如'login'和'province'
#標簽在info.xml文件中有多個，則可以通過指定數組的下標的方式獲取某個具體標簽。
#getElementsByTagName('province') 獲得的是標簽名為"province"的一組標簽
#getElementsByTagName('province').tagname[0] 表示一組標簽中的第一個
#getElementsByTagName('province').tagname[2] 表示一組標簽中的第三個
tagname=root.getElementsByTagName('browser')
print(tagname[0].tagName)

tagname=root.getElementsByTagName('login')
print(tagname[1].tagName)

tagname=root.getElementsByTagName('province')
print(tagname[2].tagName)
'''
執行結果
browser
login
province
'''

#獲得標簽的屬性值
#getAttribute()方法用於獲取元素的屬性值。它和webdriver中所提供的get_attribute()方法相似
logins=root.getElementsByTagName('login')

username=logins[0].getAttribute("username")
print(username)

password=logins[0].getAttribute("password")
print(password)

username=logins[1].getAttribute("username")
print(username)

password=logins[1].getAttribute("password")
print(password)
'''
執行結果
admin
123456
guest
654321
'''

#獲得標簽對之間的數據
#firstChild屬性返回被選節點的第一個子節點。data表示獲緊該節點的數據，它和webdriver中提供的text方法類似
provinces=dom.getElementsByTagName('province')
citys=dom.getElementsByTagName('city')

p2=provinces[1].firstChild.data
print(p2)

c1=citys[0].firstChild.data
print(c1)

c2=citys[1].firstChild.data
print(c2)
'''
執行結果
广东
深圳
珠海
'''