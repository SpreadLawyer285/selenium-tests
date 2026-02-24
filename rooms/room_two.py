from selenium.webdriver.common.by import By

def room_two(driver):
    driver.implicitly_wait(5)
    guess = driver.find_element(By.XPATH,'//*[@id="root"]/main/div/input')
    guess_btn = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/button')
    click = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/a')
    for i in range(0, 101):
        guess.send_keys(i)
        guess_btn.click()
        driver.implicitly_wait(5)
        title = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/h2')
        if "Eltaláltad" in title.get_attribute("textContent"):
            break
        guess.clear()
    
    driver.implicitly_wait(5)
    click.click()