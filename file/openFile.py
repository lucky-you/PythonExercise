# 1.打开文件

file = open("text", "r", encoding="utf-8")

# 2.读取文件
text = file.read()
print(text)

# 3.关闭文件
file.close()
