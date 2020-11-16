import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd

### Chromeを起動する関数
def set_driver(driver_path,headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg==True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    #options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(executable_path=os.getcwd() + "/" + driver_path,options=options)

### main処理
def main():
    # search_keyword="高収入"
    search_keyword= input()
    # driverを起動
    driver=set_driver("chromedriver", False)
    # Webサイトを開く
    driver.get("https://tenshoku.mynavi.jp/")
    time.sleep(5)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')
    time.sleep(2)
    # ポップアップを閉じる
    driver.execute_script('document.querySelector(".karte-close").click()')
    
    # 検索窓に入力
    driver.find_element_by_class_name("topSearch__text").send_keys(search_keyword)
    # 検索ボタンクリック
    driver.find_element_by_class_name("topSearch__button").click()
    

    # 検索結果の一番上の会社名を取得
    name_list=driver.find_elements_by_class_name("cassetteRecruit__name")
    copy_list=driver.find_elements_by_class_name("cassetteRecruit__copy")
    status_list=driver.find_elements_by_class_name("labelEmploymentStatus")
    salary_list=driver.find_elements_by_class_name("tableCondition__body")
    container_list=driver.find_elements_by_class_name("container__inner")

    # 1ページ分繰り返し
    print("{},{},{}".format(len(copy_list),len(status_list),len(name_list),len(salary_list), len(container_list)))
    for name,copy,status,salary,container in zip(name_list,copy_list,status_list,salary_list,container_list):
        print(name.text)
        print(copy.text)
        print(status.text)
        print(salary.text)
        print(container.text)
    
        name = name.text
        copy = copy.text
        status = status.text
        salary = salary.text
        container = container.text

        df = pd.DataFrame([name, copy, status, salary, container])
        df.to_csv("abcd.csv")


## 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()