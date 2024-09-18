import os

def batch_rename_extension(directory, old_extension, new_extension):
    for filename in os.listdir(directory):
        if filename.endswith(old_extension):
            base = os.path.splitext(filename)[0]
            new_name = base + new_extension
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    print(f"Renamed all {old_extension} files to {new_extension} in {directory}")

# 使用示例
directory_path = r'C:\Users\29918\Desktop\R'
# 替换为您的目录路径
batch_rename_extension(directory_path, '.xlsx', '.xls')
