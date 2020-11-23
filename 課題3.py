import os
from selenium.webdriver import Chrome, ChromeOptions
import time
# import pandas as pd

# Chromeを起動する関数
def set_driver(driver_path, headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)

# main処理
def main():
    search_keyword = "高収入"
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')

    # 検索窓に入力
    driver.find_element_by_class_name(
        "topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()

    # ページ終了まで繰り返し取得
    exp_name_list = []

    while True:
  # ここに情報取得処理を書く
  # 検索結果の一番上の会社名を取得
        name_list=driver.find_elements_by_class_name("cassetteRecruit__name")
        title_list = driver.find_elements_by_class_name("cassetteRecruit__copy")
        label_list = driver.find_elements_by_class_name("cassetteRecruit__attribute")

        # for name in name_list:
        #     print(name.text)

        for name, title, label in zip(name_list, title_list, label_list):
            print(name.text)
            print(title.text)
            print(label.text)

  # ここにページ切り替え処理を書く
        try:
            icon = driver.find_element_by_class_name("iconFont--arrowLeft")
            #次ページを開く
            driver.get(icon.get_attribute("href"))
            time.sleep(5)
        except:
            break

    # 1ページ分繰り返し
    print(len(name_list))
    for name in name_list:
        print(name.text)

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
