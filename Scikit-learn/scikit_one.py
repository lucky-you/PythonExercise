from sklearn.datasets import load_iris, fetch_20newsgroups
from sklearn.model_selection import train_test_split


li = load_iris()

# print("获取特征值")
# print(li.data)
# print("获取目标值")
# print(li.target)
# print(li.DESCR)


# 注意返回值  训练集 train  x_train  y_train  测试集   text  x_text y_text
x_train, x_text, y_train, y_text = train_test_split(li.data, li.target, test_size=0.25)
print("训练集特征值和目标值：", x_train, y_train)
print("测试集特征值和目标值：", x_text, y_text)

fetch_20newsgroups()
