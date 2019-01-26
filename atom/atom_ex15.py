from sys import argv
#调用参数
script,filename = argv
#打开filname这个文件（文件名自己定）
txt = open(filename)

print(f"here's your file {filename}:")
#读取这个文件用read.()这个函数
print(txt.read())

print("type the filename again:")
#在">"后让用户再次输入文件名
file_again = input("> ")
#再次打开这个文件
txt_again = open(file_again)
#再次读取这个文件
print(txt_again.read())
