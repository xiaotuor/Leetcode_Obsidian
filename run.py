import os
import re
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def clean_folder_name(name):
    # 移除不允许的字符
    name = re.sub(r'[\/:*?"<>|]', '_', name)
    return name

# 设置文件存储路径
obsidian_folder_path = r"C:\D\ProgramFiles\Obsidian\Tools\highLeecode"

# 如果文件夹不存在则创建
if not os.path.exists(obsidian_folder_path):
    os.makedirs(obsidian_folder_path)

# 禁用日志输出
os.environ['WDM_LOG_LEVEL'] = '0'  # 适用于webdriver-manager
os.environ['webdriver.chrome.logfile'] = '/dev/null'  # 适用于Chromium

# 初始化浏览器
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(options=chrome_options)

# python3选择标志
first = True

# 打开LeetCode题目列表页面
driver.get("https://leetcode.cn/studyplan/premium-algo-100/")
time.sleep(3)

# 遍历每个题目类型
type_xpath = "/html/body/div[1]/div[1]/div/div[5]/div/div[2]/div/div[1]/div/div[2]/div"

type_elements = driver.find_elements(By.XPATH, type_xpath)

for type_index, type_element in enumerate(type_elements):
    try:
        # 获取题目类型名称
        type_name_elem = type_element.find_element(By.XPATH, "./div[1]")
        type_name = type_name_elem.text.strip()
        type_name = clean_folder_name(type_name)  # 清理文件夹名称
        
        # 创建题目类型文件夹
        type_folder_path = os.path.join(obsidian_folder_path, type_name)
        if not os.path.exists(type_folder_path):
            os.makedirs(type_folder_path)
        
        # 获取该类型下所有题目的元素
        problem_elements = type_element.find_elements(By.XPATH, "./div[position() > 1]")

        # 遍历每个题目元素
        for problem_element in problem_elements:
            try:
                # 点击题目元素打开题目详情页面
                problem_link_elem = problem_element.find_element(By.XPATH, ".//div//div[2]//div/div")
                problem_link_elem.click()                
                time.sleep(2)
                
                # 切换到新窗口
                driver.switch_to.window(driver.window_handles[1])
                
                # 获取题目和描述内容
                try:
                    # 获取题目
                    title_elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div/div/div[4]/div/div[1]/div[1]/div/div/a")
                    title = title_elem.text.strip()
                    
                    # 获取描述内容
                    description_elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div/div/div[4]/div/div[1]/div[3]")
                    description_html = description_elem.get_attribute('innerHTML')  # 提取HTML内容

                    # 使用BeautifulSoup移除<p>&nbsp;</p>标签
                    soup = BeautifulSoup(description_html, 'html.parser')
                    for tag in soup.find_all('p'):
                        if tag.text == '\xa0':  # \xa0表示&nbsp;
                            tag.decompose()
                    description_html = str(soup)

                    if first:
                        # 选择Python3代码模板
                        try:
                            button_elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div/div/div[7]/div/div[1]/div[1]/div[1]/div/div/div[1]/div/button")
                            button_elem.click()
                            time.sleep(1)
                            python3_option_elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div/div/div[7]/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div[4]/div/div")
                            python3_option_elem.click()
                            time.sleep(1)
                        except Exception as e:
                            print(f"Failed to select Python3 template: {e}")
                        
                        first = False
                    
                    # 获取代码实现部分
                    try:
                        code_elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[5]/div/div/div[7]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div[5]")
                        code_text = code_elem.text  # 直接提取文本内容
                    except Exception as e:
                        code_text = ""
                    
                    # 生成Markdown内容
                    # markdown_content = f"# {title}\n\n"
                    # markdown_content += f"## Description\n\n"
                    markdown_content = description_html  # 使用HTML内容
                    markdown_content += "\n\n### 代码实现\n\n```python\n" + code_text + "\n```\n"

                    # 保存到Markdown文件
                    file_path = os.path.join(type_folder_path, f"{title}.md")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)

                    print(f"Saved: {title}")
                except Exception as e:
                    print(f"Failed to save {url}: {e}")
                
                # 关闭新窗口
                driver.close()
                
                # 切换回原窗口
                driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                print(f"Failed to access {url}: {e}")
    except Exception as e:
        print(f"Failed to process type {type_index}: {e}")

# 关闭浏览器
driver.quit()
