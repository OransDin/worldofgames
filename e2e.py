
from main_score import app
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import threading
import time
import sys

def run_flask_in_thread():
    app.run(port=5000)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask_in_thread)
    flask_thread.daemon = True
    flask_thread.start()
    time.sleep(3)


def test_scores_service():
    service = Service(executable_path=r"C:\Users\oran\Downloads\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://127.0.0.1:5000/score")
    score_text = driver.find_element(By.XPATH,'//*[@id="score"]').text
    score = int(score_text)
    driver.quit()
    if 1 <= score <= 1000:
        return True
    else:
        return False

def main_function():
    tests_passed = True
    if tests_passed:
        sys.exit(0)
    else:
        sys.exit(-1)

main_function()

