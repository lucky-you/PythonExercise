
def input_Password():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    print("主动抛出异常")
    ex = Exception("密码长度不够")
    raise ex


if __name__ == '__main__':
    try:
        print(input_Password())

    except Exception as result:
        print("错误 %s" % result)
