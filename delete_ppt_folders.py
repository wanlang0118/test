import os
import shutil
from pathlib import Path

def delete_ppt_folders(root_path):
    """
    递归删除指定路径下所有名为'PPT'的文件夹
    
    Args:
        root_path (str): 要搜索的根目录路径
    """
    root = Path(root_path)
    
    if not root.exists():
        print(f"错误：路径 {root_path} 不存在")
        return
    
    deleted_folders = []
    
    # 使用Path.walk()遍历所有子目录（Python 3.12+）
    try:
        for current_dir, dirs, files in root.walk():
            # 检查当前目录下是否有名为'PPT'的文件夹
            for dir_name in dirs[:]:  # 使用切片复制避免修改时出错
                if dir_name == 'PPT':
                    ppt_path = current_dir / dir_name
                    try:
                        shutil.rmtree(ppt_path)
                        deleted_folders.append(str(ppt_path))
                        print(f"已删除: {ppt_path}")
                        dirs.remove(dir_name)  # 从列表中移除已删除的目录
                    except Exception as e:
                        print(f"删除失败 {ppt_path}: {e}")
    except AttributeError:
        # 如果Python版本低于3.12，使用os.walk()
        for current_dir, dirs, files in os.walk(root_path):
            for dir_name in dirs[:]:
                if dir_name == 'PPT':
                    ppt_path = os.path.join(current_dir, dir_name)
                    try:
                        shutil.rmtree(ppt_path)
                        deleted_folders.append(ppt_path)
                        print(f"已删除: {ppt_path}")
                        dirs.remove(dir_name)
                    except Exception as e:
                        print(f"删除失败 {ppt_path}: {e}")
    
    if deleted_folders:
        print(f"\n总共删除了 {len(deleted_folders)} 个PPT文件夹:")
        for folder in deleted_folders:
            print(f"  - {folder}")
    else:
        print("未找到任何名为'PPT'的文件夹")

if __name__ == "__main__":
    # 示例用法
    target_path = r"D:\桌面\2025最新版JavaWeb+AI"
    
    # 确认操作
    print(f"即将在以下路径中删除所有名为'PPT'的文件夹:")
    print(f"路径: {target_path}")
    
    confirm = input("确认执行删除操作吗？(输入 'yes' 确认): ")
    
    if confirm.lower() == 'yes':
        delete_ppt_folders(target_path)
    else:
        print("操作已取消")