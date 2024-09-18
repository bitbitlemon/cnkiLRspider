import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# 初始化WebDriver
driver = webdriver.Edge()
url = 'https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS'
driver.get(url)
time.sleep(5)

# 点击期刊
driver.find_element(By.XPATH, '//*[@id="ModuleSearch"]/div[2]/div/div/ul/li[1]/a/span').click()
time.sleep(3)
#点击主题
driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[1]/div/span').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[1]/ul/li[2]/a').click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[1]/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[1]/div[2]/ul[1]/li[2]/a').click()
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="gradetxt"]/dd[2]/div[2]/input').send_keys('情报教育')
time.sleep(2)
# #点击中国图书分类号
# driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/a').click()
# time.sleep(1)

#输入检索词
driver.find_element(By.XPATH,'//*[@id="gradetxt"]/dd[1]/div[2]/input').send_keys('情报学教育')
time.sleep(2)
# 进行检索
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/div/input').click()
time.sleep(3)
#换成相关度
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/ul/li[1]').click()
time.sleep(3)
# 每页显示条数改成50
driver.find_element(By.XPATH,'//*[@id="perPageDiv"]/div/i').click()
driver.find_element(By.XPATH,'//*[@id="perPageDiv"]/ul/li[3]/a').click()
time.sleep(5)

# 全选
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/label/input').click()
time.sleep(4)

click_count = 0

# 尝试点击下一页
try:
    while True:
        driver.find_element(By.ID, 'PageNext').click()
        time.sleep(3)  # 等待页面加载

        #全选操作
        driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/label/input').click()
        time.sleep(4)

        click_count += 1

        if click_count % 9 == 0:
            # 转到导出新窗口
            driver.find_element(By.XPATH, '//*[@id="batchOpsBox"]/li[2]/a').click()
            driver.find_element(By.XPATH, '//*[@id="batchOpsBox"]/li[2]/ul/li[1]/a').click()
            driver.find_element(By.XPATH, '//*[@id="batchOpsBox"]/li[2]/ul/li[1]/ul/li[13]/a').click()
            time.sleep(10)

            # 获取所有窗口句柄
            all_windows = driver.window_handles

            # 切换到新窗口
            for handle in all_windows:
                if handle != driver.current_window_handle:
                    driver.switch_to.window(handle)
                    break
            # 在新页面进行操作（下载操作）
            driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/ul/div/div/a[1]').click()
            time.sleep(5)

            driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/ul/li[5]/a').click()
            time.sleep(4)
            #返回原页面并执行新一轮上述操作
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(5)
            driver.find_element(By.XPATH,
                                '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/a').click()
            time.sleep(3)
except NoSuchElementException:
    print("没有更多页面")

# 关闭WebDriver
driver.quit()
