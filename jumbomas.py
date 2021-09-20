from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
#---------------------------------------------------------------------------------------------------
debug = True                                           # False si no queres ver el progreso ni debug
usuario_jumbomas = ''                                  # Tu usuario
pass_jumbomas = ''                                     # Tu Contraseña
pagina_inicio = 'https://www.jumbomas.com.ar/login'    # La pagina de inicio
DRIVER_PATH = 'C:\chromedriver_win32\chromedriver.exe' # Driver de Chrome
#---------------------------------------------------------------------------------------------------
chrome_options = Options()
if debug == False:
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)

driver.get(pagina_inicio)
if debug: print('Pedi la pagina de Login y espero 4 segundos')
time.sleep(4)
if debug: print('Intentando Login')
search_box = driver.find_element_by_id('Email')
search_box.send_keys(usuario_jumbomas)
search_box = driver.find_element_by_id('Password')
search_box.send_keys(pass_jumbomas)
search_box = driver.find_element_by_id('submitloginform')
search_box.click()
if debug: print('Login OK, Espero 2 segundos')
time.sleep(2)
html = driver.page_source
driver.quit()
if debug: print('Cierro el navegador')

soup = BeautifulSoup(html, features="lxml")

busqueda = soup.findAll('li'),('class'=="infoPuntos")
start = 'tenés'     # inicio de la busqueda 
end = 'puntos'      # final de la busqueda
s = str(busqueda)   # a donde voy a buscar

resultado = s[s.find(start)+len(start)+3:s.find(end)-1] # Aca esta el resultado (hay 3 espacios adelante y 1 atras)
resultado = int(resultado.replace('.', '')) # Elimino el .
print('Hay', resultado, 'puntos')
