from selenium import webdriver
import json
import time

# browser = webdriver.Chrome(executable_path="./chromedriver")
def write_shimo_cookies():
    try:
        browser = webdriver.Chrome(executable_path="./chromedriver")
        browser.get("https://shimo.im")
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="homepage-header"]/nav/div[3]/a[2]/button').click()
        time.sleep(1)
        browser.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[3]/div[1]').click()
        time.sleep(5)
        cookies = browser.get_cookies()
        # print(cookies)
        if len(cookies) > 3:
            with open("cookies.txt", "w") as fp:
                json.dump(cookies, fp)
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        browser.close()

def read_shimo_cookies():
    browser = webdriver.Chrome(executable_path="./chromedriver")
    browser.get("https://shimo.im")
    with open("cookies.txt", "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            browser.add_cookie(cookie)

    browser.get("https://shimo.im")
    time.sleep(10)
    browser.close()

def login_shimo():
    try:
        read_shimo_cookies()
    except Exception as e:
        print(e)
        write_shimo_cookies()

if __name__ == "__main__":
    login_shimo()
