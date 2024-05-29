from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

def initialize_driver(type: str = None):
  if type == "f":
    options = webdriver.FirefoxOptions()
    return webdriver.Firefox(options=options)

  chrome_app_path = "./chromedriver/chromedriver"
# user_data_dir = ""
  options = webdriver.ChromeOptions()
  options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
  # options.add_argument(f"--user-data-dir={user_data_dir}")
  
  service = webdriver.ChromeService(executable_path=chrome_app_path, service_args=["--user-profile=Default", "--profile-directory=Default"])

  return webdriver.Chrome(options=options, service=service, keep_alive=True)

def find_element(driver: WebDriver, selector, timeout = 1.5):
  try:
    current_url = driver.current_url
    if current_url.startswith("https://www.google.com/sorry/index"):
      print("Dem don nab us. Sleeping for 30")
      sleep(30)
      return WebDriverWait(driver, timeout).until(lambda x: x.find_element(By.CSS_SELECTOR, selector))

    return WebDriverWait(driver, timeout).until(lambda x: x.find_element(By.CSS_SELECTOR, selector))
  except:
    return None
  

def install_captcha_solver(driver):
  driver.get("https://chromewebstore.google.com/detail/captcha-solver-auto-hcapt/hlifkpholllijblknnmbfagnkjneagid?hl=en")

  sleep(30)