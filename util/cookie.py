# 读取 cookie 文件
import json


def load_cookies(cookie_file: str):
    with open(cookie_file, 'r', encoding='utf-8') as f:
        return json.load(f)