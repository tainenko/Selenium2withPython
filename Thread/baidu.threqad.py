from threading import Thread
from selenium import webdriver
from time import ctime,sleep

def test_baidu(browser,serch):
    print('start:',ctime())
    print('browser:',browser)
    if browser=='edge':
        driver=webdriver.Edge()
    elif browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    else:
        print("borwser 參數有誤，只能為ie, chrome 或是firefox")

    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.quit()

if __name__=='__main__':
    lists={'chrome':'threading','edge':'webdriver','firefox':'python'}
    threads=[]
    files=range(len(lists))

    for browser, search in lists.items():
        t=Thread(target=test_baidu,args=(browser,search))
        threads.append(t)

    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:',ctime())