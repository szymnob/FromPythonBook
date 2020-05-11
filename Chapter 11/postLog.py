from selenium import webdriver
import time, sys

#conf
login = 'login'
password = 'password'


chromedriver = 'C:\\Users\\Szymon\\Documents\\Python file\\pythonAttemptTwo\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)

def logging():
    browser.get('https://gmail.com')
    
    url = browser.current_url
    print('Podawanie adresu...', end=' ')
    log = browser.find_element_by_id('identifierId')
    log.send_keys(login)
    button = browser.find_element_by_id('identifierNext')
    button.click()
    print('Pomyślne')

    while url == browser.current_url:
        time.sleep(1)

    print('Podawanie hasła...', end=' ')
    try:
        passw = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
        passw.send_keys(password)
        button = browser.find_element_by_xpath("//span[@class='RveJvd snByac']")
        button.click()
    except:
        return 0
    print('Pomyślne')
    #waiting for page reload
    x = 0
    while not browser.current_url.endswith('inbox'):
        time.sleep(1)
        x += 1
        if x == 8:
            return 0

    return 1

def creatingNew(destination, topic, message):
    button = browser.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']")
    button.click()

    while not browser.current_url.endswith('compose=new'):
        time.sleep(1)
    print('Podawanie wiadomości')

    adress = browser.find_element_by_xpath("//textarea[@class='vO']")
    adress.send_keys(destination)
    adress = browser.find_element_by_xpath("//input[@class='aoT']")
    adress.send_keys(topic)
    adress = browser.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']")
    adress.send_keys(message)
    print('Podano wiadomość, czy chcesz wysłać wiadowmość do: %s? Tak lub nie' % messAdress)
    if input().lower() == 'nie':
        return 0
    button = browser.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
    button.click()
    print('Wiadomość wysłano pomyślnie!')
    return 1


#for testing purposes
if len(sys.argv) != 4:
    print('Wymagany adresat, temat oraz treść')
    messAdress = 'adress@gmai.com'
    messTopic = 'Wiadomość testowa'
    messText = '1/n2'
else:
    messAdress = sys.argv[2]
    messTopic = sys.argv[3]
    messText = sys.argv[4]


while logging() == 0:
    print('Błąd logowania')
    browser.get('https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/')
    logging()
    if browser.current_url.endswith('inbox'):
        break
print('Logowanie pomyślne')

creatingNew(messAdress, messTopic, messText)




