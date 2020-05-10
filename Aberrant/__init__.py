# 异常的学习和使用

try:
    num = int(input("请输入一个数字："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入一个正确的正整数")
except ZeroDivisionError:
    print("除0错误")
except Exception as result:
    print("未知错误 %s " % result)
finally:
    print("无论是否出现异常，最终我都会被执行")
