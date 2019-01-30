import os

os.chdir('c://Users/dlb/Desktop/小结/0x4')

# print(os.getcwd())

num_words = 0

files = os.listdir()
for f in files:
	with open(f,encoding='utf8') as file:
		contents = file.read()
		words = contents.rstrip()
		num_words += len(words)
		print(num_words)
print(num_words)