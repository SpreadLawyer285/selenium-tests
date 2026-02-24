from selenium.webdriver.common.by import By

def room_one(driver):
    driver.implicitly_wait(5)
    regenerate_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button[1]')
    check_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button[2]')

    while(True):
        try:
            regenerate_btn.click()
        except:
            break

    check_btn.click()