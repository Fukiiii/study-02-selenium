(base) Cacao-no-MacBook-Air:desktop cacao$ python3 selenium_sample.py
Traceback (most recent call last):
  File "/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/common/service.py", line 76, in start
    stdin=PIPE)
  File "/opt/anaconda3/lib/python3.7/subprocess.py", line 775, in __init__
    restore_signals, start_new_session)
  File "/opt/anaconda3/lib/python3.7/subprocess.py", line 1522, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: '/Users/cacao/Desktop\\chromedriver': '/Users/cacao/Desktop\\chromedriver'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "selenium_sample.py", line 35, in <module>
    main()
  File "selenium_sample.py", line 25, in main
    driver = set_driver("chromedriver", False)
  File "selenium_sample.py", line 22, in set_driver
    return Chrome(executable_path=os.getcwd() + "\\" + driver_path,options=options)
  File "/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/webdriver.py", line 73, in __init__
    self.service.start()
  File "/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/common/service.py", line 83, in start
    os.path.basename(self.path), self.start_error_message)
selenium.common.exceptions.WebDriverException: Message: 'Desktop\chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home