ZH_CN = {
    "greeting": "你好",
    "farewell": "再见",
    "menu_file": "文件",
    "menu_edit": "编辑",
    "menu_help": "帮助"
}

def t(key, **kwargs):
    return ZH_CN.get(key, key)
