
import requests
import json
def login(mail, password):

s = requests.Session()

payload={

'email': mail,

'password': password

}

res = s.post('https://aternos.org/', json-payload)

s.headers.update({'authorization': json.loads(res.content)['token']})

print(res.content)

return s

session = login('Lagjavacrash', 'trewq12345')

r = session.patch('https://aternos.org/account/', json={'username'}) print(r.content)
from selenium import webdriver

from webdriver_manager.chrome import Chrome DriverManager
import time

browser = webdriver.Chrome (ChromeDriverManager().install())

browser.get('https://aternos.org/')

time.sleep(5)

button = browser.find_element_by_link_text('Start')

button.click()

time.sleep(3)