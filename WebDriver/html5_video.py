'''
越來越多的應用使用了HTML5的元素，如canvas、video等。HTML5定義了一個新的元素,<video>，指定了
一個標準的方式來嵌入電影片段。

JavaScript函數有個內置的對象叫做arguments,argument對象包含了函數調用的參數睥組，[0]表示取對象的第一個值。
currentSrc反回當前音步/視步的URL，如果未設置音頻/視頻，則返回空字串
load()、play()、pause()等控制著視頻的加載、播放和暫停。
'''
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://videojs.com/")

#定位播放文件地址
video=driver.find_element_by_xpath('//*[@id="preview-player_html5_api"]')
#返回放文件地址
url=driver.execute_script("return arguments[0].currentSrc;",video)
print(url)
#播放視頻
print("start")
driver.execute_script("return arguments[0].play()",video)
#播放15秒
sleep(15)
#暫停播放視頻
print("stop")
driver.execute_script("arguments[0].pause()",video)

driver.quit()