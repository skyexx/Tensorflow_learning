#字符串和文本
types_of_people = 10
#there are all string between the "" and the ''
#if you want to add some variable into the string you should print "f"
#at title and use the"{}"between the variable
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said:{x}")
print(f"I also said:'{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"
# .format()是另一种格式化的字符串
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
