import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def init_driver():
    driver = webdriver.Edge()
    url = 'https://kns.cnki.net/kns8/AdvSearch?dbcode=CFLS'
    driver.get(url)
    time.sleep(5)
    return driver

def click_journal(driver):
    driver.find_element(By.XPATH, '//*[@id="ModuleSearch"]/div[2]/div/div/ul/li[1]/a/span').click()
    time.sleep(3)

def click_subject(driver):
    driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[1]/div[2]/div[1]/div[1]/span').click()
    time.sleep(3)

def click_classification(driver):
    driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[1]/div[2]/div[1]/div[2]/ul[1]/li[11]/a').click()
    time.sleep(1)

def fuzzy_search(driver):
    driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[1]/div[2]/div[2]/div/span').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="gradetxt"]/dd[1]/div[2]/div[2]/ul/li[2]/a').click()
    time.sleep(1)

def set_start_year(driver):
    driver.find_element(By.XPATH, '//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/ul/li[45]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/input').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/ul/li[2]/a').click()
    time.sleep(2)

def select_cscd(driver):
    driver.find_element(By.XPATH,'//*[@id="ModuleSearch"]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[3]/div/label[6]/input').click()
    time.sleep(2)

def input_search_term(driver, term):
    driver.find_element(By.XPATH,'//*[@id="gradetxt"]/dd[1]/div[2]/input').send_keys(term)
    time.sleep(2)

def start_search(driver):
    driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/div/input').click()
    time.sleep(3)

def sort_by_relevance(driver):
    driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/ul/li[1]').click()
    time.sleep(3)

def set_items_per_page(driver):
    driver.find_element(By.XPATH,'//*[@id="perPageDiv"]/div/i').click()
    driver.find_element(By.XPATH,'//*[@id="perPageDiv"]/ul/li[3]/a').click()
    time.sleep(5)

def select_all(driver):
    driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/label/input').click()
    time.sleep(4)

def go_to_next_page(driver):
    try:
        driver.find_element(By.ID, 'PageNext').click()
        time.sleep(3)  # 等待页面加载
    except NoSuchElementException:
        print("没有更多页面")
        return False
    return True

def export_data(driver):
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
    # 返回原页面并执行新一轮上述操作
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/a').click()
    time.sleep(3)

def automate_search(driver, term):
    click_journal(driver)
    click_subject(driver)
    click_classification(driver)
    fuzzy_search(driver)
    set_start_year(driver)
    select_cscd(driver)
    input_search_term(driver, term)
    start_search(driver)
    sort_by_relevance(driver)
    set_items_per_page(driver)
    select_all(driver)

    click_count = 0
    while go_to_next_page(driver):
        select_all(driver)
        click_count += 1

        if click_count % 9 == 0:
            export_data(driver)

# 主程序执行示例
driver = init_driver()
automate_search(driver, 'R96')

# 关闭WebDriver
driver.quit()
