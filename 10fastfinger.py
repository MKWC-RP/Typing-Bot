"""Welcome to my typing bot. Please install the Selenium Module through "python -m pip install selenium"
   in Command Prompt or in your interpreter settings in Pycharm. Install the chromedriver present in the repositry
   or download the required version from the link in the chromedriver_install file.
   To adjust typing speed on the site, you can adjust the sleep time present on line 67 where sleep time is in seconds.
   Adjust it however you want or remove it completely and see the magic.
   Enjoy
   """


from selenium import webdriver
import time

path = "D:\Python\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://10fastfingers.com/advanced-typing-test/english")
driver.maximize_window()

Cookie_button = driver.find_element_by_id("CybotCookiebotDialogBodyButtonDecline")
Cookie_button.click()
time.sleep(3)
while True:
    count = 0
    keys = 0
    while True:
        try:
            first_word = driver.find_element_by_class_name('highlight')
        except Exception:
            timer = driver.find_element_by_id('timer')
            t1 = timer.text.split(':')
            t = int(t1[1]) 
            t_time = 60 - t
            print(f'You wrote {count} words in {t_time} seconds.')
            print(f'Your WPM was {keys/(5*(t_time/60))}')
            play = input('Do you want to test again?(y/n): ')
            if play == 'y':
                while True:
                    reload = driver.find_element_by_id('reload-btn')
                    reload.click()
                    time.sleep(3)
                    break
            else:
                driver.quit()
                print('Thank you!')
                exit()
            break
        else:
            words = driver.find_element_by_xpath('//*[@id="words"]')
            first = first_word.text
            a = words.text
            index = a.index(first)
            a = a[index:len(a)]
            a1 = a.split()
            for i in a1:
                keys += len(i)
            count += len(a1)
            timer = driver.find_element_by_id('timer')
            if timer.text == '0:00':
                print('The race has ended!!!')
                exit()
            else:
                input_field = driver.find_element_by_xpath('//*[@id="inputfield"]')
                #time.sleep(1)
                #print(f'{a}, ')
                #input_field.send_keys(a + ' ')
                for i in a1:
                    input_field.send_keys(i + ' ')
                    print(end=f'{i} ')
                    time.sleep(0.1)
                print()
                #time.sleep(1)
    time.sleep(2)
