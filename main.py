import os
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def run_opencat_bot():
    # ブラウザの設定（画面なしモード）
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # 1. LINEのログイン画面またはWeb版へアクセス
    # (注: Web版LINEは現在サービスが限定的なため、特定のWebフック等を経由させるのが一般的)
    # ここでは概念的な「入力→送信」のループを示します
    
    message_base = "テスト投稿"
    count = 5
    interval = 2

    for i in range(count):
        # 乱数生成
        rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        full_message = f"{message_base} [{rand_str}]"
        
        # 実際にはここでLINEの入力欄を特定して送信
        print(f"送信中: {full_message}")
        
        # 例: driver.find_element(By.ID, "input_field").send_keys(full_message + Keys.ENTER)
        
        time.sleep(interval)

    driver.quit()

if __name__ == "__main__":
    run_opencat_bot()
