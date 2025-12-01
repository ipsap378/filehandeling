file_read = open('codengal.txt', 'r')
print("file is in read mode")
print(file_read.read())
file_read.close()

file_write = open('codengal.txt', 'w')
file_write.write("File in write mode")
file_write.write("hi i am a penguin i am 1 year old")
file_write.close()

file_append = open('codengal.txt', 'a')
file_append.write("\n file in append mode...")
file_append.write(" hi i am a penguin i am 1 year old")
file_append.close()