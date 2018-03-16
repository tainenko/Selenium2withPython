from threading import Thread
from selenium import webdriver
from time import sleep, ctime

def test_baidu(host,browser):
    print('start:',ctime())
    print(host,browser)
    dc={'borwserName':browser}
    driver=webdriver.Remote(command_executor=host,desired_capabilities=dc)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    driver.close()

if __name__=='__main__':
    lists={'http://127.0.0.1:4444/wd/hub':'chrome',
           'http://127.0.0.1:5555/wd/hub':'edge',
           'http://172.16.10.34:6666/wd/hub':'firefox'}
    threads=[]
    files=range(len(lists))

    for host,browser in lists.items():
        t=Thread(target=test_baidu, args=(host,browser))
        threads.append(t)

    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    print('end:',ctime())