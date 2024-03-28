'''
Created on 2024年2月27日

@author: ericluo
'''

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import csv
import time
import method
from method import PyConfigParser



def RunSelenium(config, driver, config_data, **kwargs):
    
    timeout = kwargs.get('timeout', '5')
    freq = kwargs.get('freq', '0.5')
    xpath = kwargs.get('xpath', '')
    item = kwargs.get('item', '') 
    data = kwargs.get('data', '') 
    section = kwargs.get('section', 'section')
    option = kwargs.get('option', 'option')
    source = kwargs.get('source', '')
    target = kwargs.get('target', '')
    xoffset = kwargs.get('xoffset', '')
    yoffset = kwargs.get('yoffset', '')
    element = kwargs.get('yoffset', '')
    id = kwargs.get('id', '')  # @ReservedAssignment
    result = False
    
    try:
        for i in range(1):  # @UnusedVariable
            if item == 'sleep':
                time.sleep(float(data)) #等待(秒)。
            elif item == 'get': #開啟網址。
                driver.get(data)
            elif item == 'refresh':
                driver.refresh() #網頁重整。
            elif item == 'back':   
                driver.back()#前往上一項瀏覽紀錄。
            elif item == 'forward':   
                driver.forward()#前往下一項瀏覽紀錄。
            elif item == 'execute_script':
                driver.execute_script(data)#執行JavaScript語法
                #window.scrollTo(0,500) # 瀏覽器視窗捲動到 500px 位置
                #window.open("https://192.168.127.253/asqc.asp") #瀏覽器視窗開啟分頁。
            elif item == 'switch_to.frame':
                driver.switch_to.frame(data)#切換frame。
            elif item == 'switch_to.default_content':   
                driver.switch_to.default_content()#切換frame到預設值。
            elif item == 'switch_to.parent_frame':   
                driver.switch_to.parent_frame()#切換frame到前一個。
            elif item == 'switch_to.window':          
                driver.switch_to.window(driver.window_handles[int(data)])#切換分頁。             
            elif item == 'switch_to.alert.accept':
                driver.switch_to.alert.accept()#點擊警告視窗確定鍵。
            elif item == 'switch_to.alert.dismiss':
                driver.switch_to.alert.dismiss()#點擊警告視窗取消鍵。
            elif item == 'close': 
                try:  
                    driver.close()# 關閉瀏覽器視窗。
                except Exception as e:
                    raise e
            elif item == 'close': 
                try:  
                    driver.quit()# 離開瀏覽器
                except Exception as e:
                    raise e                 
            elif item == 'WebDriverWait':   
                if xpath: WebDriverWait(driver, float(timeout), float(freq)).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)), '找不到指定的元素')
                elif id: WebDriverWait(driver, float(timeout), float(freq)).until(expected_conditions.presence_of_element_located((By.ID, id)), '找不到指定的元素')
            elif item == 'quit':
                try:  
                    driver.quit()
                except Exception as e:
                    print(e)
            elif item == 'maximize_window':
                driver.maximize_window()#瀏覽器視窗最大化
            elif item == 'minimize_window':
                driver.minimize_window()#瀏覽器視窗最小化
            elif item == 'fullscreen_window':
                driver.fullscreen_window()#瀏覽器視窗全屏
            elif item == 'frame':
                
                driver.switch_to.frame('contents')
                control = driver.find_element(By.XPATH, '//*[@id="folder62"]/tbody/tr/td[2]/a/font')
                control.click()
                control = driver.find_element(By.XPATH, '//*[@id="item65"]/tbody/tr/td[2]/a/font')
                control.click()
                driver.switch_to.default_content()
                driver.switch_to.frame('main')
                control = driver.find_element(By.XPATH, '//*[@id="file_upload"]/table[1]/tbody/tr[1]/td[2]/input')
                control.send_keys('D:\\Ericluo Documents\\Desktop\\MultipleStationV2\\MW-AWK1132C\\MOXA\\Moxa 產測資料\\FW\\出貨\\AWK1137C_1.8_Build_23010916.rom')
                
            else:
                
                if item == 'select_by_index':
                    if xpath:
                        control = Select(driver.find_element(By.XPATH, xpath))
                    elif id:
                        control = Select(driver.find_element(By.ID, id))
                else:
                    if xpath:
                        control = driver.find_element(By.XPATH, xpath)
                    elif id:
                        control = driver.find_element(By.ID, id).send_keys(data)
                        
                if element :
                    if item == 'select_by_index':
                        if xpath:
                            control = Select(driver.find_element(By.XPATH, element))
                    else:
                        if xpath:
                            control = driver.find_element(By.XPATH, element)

               
                if item == 'click':
                    control.click()#按下滑鼠左鍵。
                elif item == 'click_and_hold':
                    control.click_and_hold()#滑鼠左鍵按著不放。
                elif item == 'double_click':
                    control.double_click()#連續按兩下滑鼠左鍵。
                elif item == 'context_click':
                    control.context_click()#按下滑鼠右鍵 ( 需搭配指定元素定位 )。
                elif item == 'drag_and_drop':
                    control.drag_and_drop(source, target)#點擊 source 元素後，移動到 target 元素放開。
                elif item == 'drag_and_drop_by_offset':
                    control.drag_and_drop_by_offset(source, int(xoffset), int(yoffset))#點擊 source 元素後，移動到指定的座標位置放開。
                elif item == 'release':
                    control.release(data)#放開滑鼠。
                elif item == 'send_keys':
                    control.send_keys(data)#送出某個鍵盤按鍵值。
                elif item == 'send_keys_to_element':
                    control.send_keys_to_element(element, data)#向某個元素發送鍵盤按鍵值。
                elif item == 'key_down':
                    control.key_down(data)#按著鍵盤某個鍵。
                elif item == 'key_up':
                    control.key_up(data)#按著鍵盤某個鍵。
                elif item == 'pause':
                    control.pause(int(data))#暫停動作(秒seconds)。
                elif item == 'perform':
                    control.perform()#執行儲存的動作。
                elif item == 'text':
                    method.Logging(config, 'INFO', '{} = {}'.format(option, control.text))
                    method.ConfigAdd(config_data, section, option, control.text)#元素的內容文字。
                elif item == 'get_attr_name':
                    method.ConfigAdd(config_data, 'Selenium', 'get_attr_name', control.get_attr_name(data))#元素的某個 HTML 屬性值。
                elif item == 'id':
                    method.ConfigAdd(config_data, 'Selenium', 'id', control.id())#元素的 id。
                elif item == 'tag_name':
                    method.ConfigAdd(config_data, 'Selenium', 'tag_name', control.tag_name())#元素的 tag 名稱。
                elif item == 'size':
                    method.ConfigAdd(config_data, 'Selenium', 'size', control.size())#元素的 tag 名稱。
                elif item == 'screenshot':
                    control.screenshot()#將某個元素截圖並儲存為 png。
                elif item == 'select_by_index':
                    control.select_by_index(int(data))#下拉式選單選取
                elif item == 'clear':
                    control.clear() #清除文字       
                elif item == 'current_url':
                    method.ConfigAdd(config_data, 'Selenium', 'current_url', control.current_url())# 取得當前瀏覽器網址
                elif item == 'current_window_handle':
                    method.ConfigAdd(config_data, 'Selenium', 'current_window_handle', control.current_window_handle())# 取得當前瀏覽器handle
                elif item == 'title':
                    method.ConfigAdd(config_data, 'Selenium', 'title', control.title())# 取得當前瀏覽器title
                elif item == 'is_selected':
                    result = control.is_selected()# 元素是否被選取。
                    continue
                elif item == 'is_enabled':
                    result = control.is_enabled()# 元素是否可用。
                    continue
                elif item == 'is_displayed':
                    result = control.is_displayed()# 元素是否顯示在網頁上。
                    continue
                elif item == 'parent':
                    result = control.parent()# 元素的父元素。
                    continue
                
            result = True
        
    except Exception as e:
        method.Logging(config, 'ERROR', '{}'.format(e))    
    finally:
        if method.PathIsExist(method.PathGetCurrent('STOP')) == True: result = False
        return result
    
if __name__ == '__main__':
    pass

    try:       

        driver = None
        
        method.FileDelete(method.PathGetCurrent('PASS'))
        method.FileDelete(method.PathGetCurrent('FAIL'))
        method.FileDelete(method.PathGetCurrent('STOP'))
        
        config_data = PyConfigParser()
        config = PyConfigParser()
        config.read(method.PathGetCurrent('selenium.ini'))
        #[env]
        output_file_name = method.ConfigGet(config, 'env', 'output_file_name', 'selenium_output.txt')
        method.FileDelete(method.PathGetCurrent(output_file_name))
        #[logger]
        # loggers = method.ConfigGet(config, 'logger', 'loggers', 'all')
        logger_file_name = method.ConfigGet(config, 'logger', 'file_name', 'selenium.log')
        # logger_level = method.ConfigGet(config, 'logger', 'level', 'INFO')
        method.FileDelete(method.PathGetCurrent(logger_file_name))
        # logger = method.LoggerLoad(loggers, logger_file_name, logger_level)
        # if logger == None: raise RuntimeError("LoggerLoad Fail.")
        
        #[chrome_options]
        disable_notifications = method.ConfigGet(config, 'chrome_options', 'disable_notifications', 'False')#禁用彈跳視窗
        headless = method.ConfigGet(config, 'chrome_options', 'headless', 'False')#隱藏瀏覽器視窗
        maximized = method.ConfigGet(config, 'chrome_options', 'maximized', 'False')#瀏覽器視窗最大化
        minimized = method.ConfigGet(config, 'chrome_options', 'minimized', 'False')#瀏覽器視窗最小化
        ChromeDriverManager = method.ConfigGet(config, 'chrome_options', 'ChromeDriverManager', 'False')#啟用Chrome更新
        
        chrome_options = webdriver.ChromeOptions()
        if disable_notifications == 'True': chrome_options.add_argument("--disable-notifications")
        if headless == 'True': chrome_options.add_argument('--headless')
        if maximized == 'True': chrome_options.add_argument('--start-maximized')
        if minimized == 'True': chrome_options.add_argument('--start-minimized')
        chrome_options.add_argument('--ignore-certificate-errors')
        if ChromeDriverManager == 'False':
            driver = webdriver.Chrome(options=chrome_options)
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        result = True
        output = False
        with open('selenium_script.txt', newline='') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                if method.PathIsExist(method.PathGetCurrent('STOP')) == True: 
                    result = False
                    break
                data = ', '.join(row)
                if not data or data[0] == '#': continue
                if "item' : 'text'" in data:
                    output = True
                res = eval(data)
                method.Logging(config, 'INFO', '{}'.format(res))
                if RunSelenium(config, driver, config_data, **res) == False:
                    result = False
                    break
        
        if method.PathIsExist(method.PathGetCurrent('STOP')) == True:
            method.Logging(config, 'ERROR', 'User Stop.')
             
        if result == True:
            method.FileCreate(method.PathGetCurrent('PASS'))
            method.Logging(config, 'INFO', 'Result : PASS')
        else:
            method.FileCreate(method.PathGetCurrent('FAIL'))
            method.Logging(config, 'INFO', 'Result : FAIL')
            
        if output == True: method.ConfigWrite(config_data, method.PathGetCurrent(output_file_name))
        
    except Exception as e:
        method.Logging(config, 'ERROR', '{}'.format(e))
        pass
    
    finally:
        try:
            if driver != None:
                driver.close()# 關閉瀏覽器視窗
                driver.quit() # 離開瀏覽器
        except Exception as e:
            method.Logging(config, 'ERROR', '{}'.format(e))
            
        method.Logging(config, 'INFO', 'Finish.')
    
        
    #ERROR
    #unterminated string literal (detected at line 1) (<string>, line 1) //scritp 字串(string)無法轉換成字典(dict)
        