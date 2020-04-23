from selenium import webdriver
import time

time.sleep(1)


def brow():
    global browser
    browser = webdriver.Firefox()
    browser.get('https://www.instagram.com')


def login(user, password):
    element = browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    Pass = browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    clicks = browser.find_element_by_xpath(
        "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button")
    time.sleep(0.5)
    element.send_keys(user)
    Pass.send_keys(password)
    clicks.click()
    time.sleep(6)

    try:
        element = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
        element.click()

    except :
        return 0


def search(value):
    search = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    search.send_keys(value)
    time.sleep(3)
    enter = browser.find_element_by_xpath(
        "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]")
    enter.click()
    time.sleep(1.5)


def home_click():
    try:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div")
        button.click()
    except:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[1]/div")
        button.click()
    return 0


def profile_click():
    try:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]")
        button.click()
        time.sleep(2)
    except:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[5]")
        button.click()
    return 0


def dm_click():
    try:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]")
        button.click()
    except:
        None
    return 0


def explore_click():
    try:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]")
        button.click()
    except:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[3]")
        button.click()
    return 0


def activity_click():
    try:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]")
        button.click()
    except:
        button = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[4]")
        button.click()
    return 0


def settings_click():
    try:
        profile_click()
        time.sleep(2)

    except:
        activity_click()

    finally:
        profile_click()

    button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button")
    button.click()
    return 0


def logout():
    try:
        settings_click()
        time.sleep(3)
        button = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/button[9]")
        button.click()
    except:
        print("there is a problem")


def first_five_not():
    activity_click()
    time.sleep(4)
    b = []
    for i in range(1, 6):
        a = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[{}]/div[2]".format(
            i)
        st = browser.find_element_by_xpath(a)
        c = st.text
        b.append(c)
    activity_click()
    return b


def pic_open():
    time.sleep(2)
    button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]")
    button.click()
    return 0


def like():
    time.sleep(1)
    button = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button")
    button.click()
    return 0


def save():
    time.sleep(1)
    button = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[3]/button")
    button.click()

    return 0


def cross_click():
    time.sleep(1)
    button = browser.find_element_by_xpath("/html/body/div[4]/div[3]/button")
    button.click()
    return 0
