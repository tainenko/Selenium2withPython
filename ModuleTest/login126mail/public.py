class Login():
    #登錄
    def user_login(selfself,driver):
        driver.switch_to.frame("x-URS-iframe")
        # 定位到idInput，輸入帳號username
        driver.find_element_by_name('email').clear()
        driver.find_element_by_name('email').send_keys('username')
        # 定位到passwardInput，輸入密碼passward
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]').clear()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[3]/div[2]/input[2]').send_keys(
            'passward')

    #退出
    def user_logout(selfself,driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()