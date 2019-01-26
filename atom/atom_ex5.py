#更多的变量和打印
my_name = 'Zed A. Shaw'# variable名要以字母开头，不能以数字开头
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
my_height_m = my_height*0.0254
my_weight_kg = my_weight*0.4535

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_height_m} meters tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"He's {my_weight_kg} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
