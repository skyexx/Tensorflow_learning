from sys import argv

script,filename = argv

txt = open(filename,'w')

world = input("write something:\n")

txt.write(world)

txt.close()
