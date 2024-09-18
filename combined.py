import os
import pandas as pd


def combine_excel_files(directory):
    all_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.xlsx') or f.endswith('.xls')]
    dataframes = []
    for file in all_files:
        df = pd.read_excel(file)
        dataframes.append(df)

    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)
        return combined_df
    else:
        return pd.DataFrame()  # 返回空的DataFrame，如果没有任何文件能成功读取


# 使用示例
directory_path = r'C:\Users\29918\Desktop\test1'  # 替换为您的目录路径
combined_df = combine_excel_files(directory_path)

if not combined_df.empty:
    # 保存合并后的文件
    combined_df.to_excel(r'C:\Users\29918\Desktop\test1\abstract.xlsx', index=False)
    print("Files combined successfully.")
else:
    print("No files were successfully combined.")
