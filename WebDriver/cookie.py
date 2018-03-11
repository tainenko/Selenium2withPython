'''
Cookie
驗証瀏覽器中cookie是否正確，webdriver提供了操作Cookie的相關方法，可以讀取、添加和刪除cookie信息
get_cookies()                                   獲得所有cookie信息
get_cookie(name)                             返回字典的key為'name'的cookie信息
add)cookie(cookie_dict)                    添加cookie。'cookie_dict'為字典對象
delete_cookie(name,optionsString)     刪除cookie信息，name是要刪除的cookie的名稱，optionString是該cookie的選項。
dele_all_cookies()                            刪除所有的cookie信息
'''
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.youdao.com")
#獲得cookie信息並打印。
cookie=driver.get_cookies()
print(cookie)

#向cookie的name和value中添加信息
driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbbbb'})
#遍歷cookies中的name和value信息並打印
for cookie in driver.get_cookies():
    print(cookie['name'],'->',cookie['value'])

driver.quit()