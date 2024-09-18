import os
import re

def remove_chinese_characters(directory):
    for filename in os.listdir(directory):
        # 使用正则表达式去除文件名中的中文字符
        new_name = re.sub(r'[\u4e00-\u9fff]+', '', filename)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    print(f"Renamed all files in {directory} by removing Chinese characters.")

# 使用示例
directory_path = r'C:\Users\29918\Desktop\test1'  # 替换为您的目录路径
remove_chinese_characters(directory_path)
