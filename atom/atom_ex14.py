#提示与传递
#这是一个互动感比较强的小程式
from sys import argv
#需要输入 一个名字作为usename
script, user_name = argv

prompt = 'so you think: '

print(f"hi {user_name},i'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
alright,so you said {likes} about liking me.
you live in {lives}. not sure where that is.
and you have a {computer} computer.nice.
""")
