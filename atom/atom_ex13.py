from sys import argv
# read the wyss section for how to run this
#script就是这个文件的名字
#在终端运行的时候就需要输入除了script以外的三个参数
script, first, second, third = argv

print("the script is called:",script)
print("your first variable is:",first)
print("your second variable is:",second)
print("your third variable is:",third)
