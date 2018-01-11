import os 
os.chdir("/Users/name/Desktop/")

#read a file
with open("read.txt", "rt", encoding="utf-8") as in_file:
	keys1 = []
	values1= []
	for counter, line in enumerate(in_file): #line counter
		if counter <= 10: #limit for loop for first 11 lines
			newline = line.rstrip('\n') #remove \n character
			var = newline.split(" ")
			keys1.append(var[0])
			values1.append(var[1])
	dictionary = dict(zip(keys1,values1))
	
#write to file
if not os.path.exists('write.txt'):
	with open('write.txt', 'wt') as out_file:
		#out_file.write('text\n') #takes only one argument
		
		#redirect print output to file
		print("text1", file=out_file)
		print("text2", file=out_file, sep=",", end="\n")
		
		list1 = ["apple", "banana","carrot"]
		print(",".join(list1)) #
		#convert int to str
		print(",", .join(str(x) for x in list1))
		#or 
		#works for both str and int
		print(*list1, sep=",", end="\n", file=out_file)


		print(*keys1, sep=",", end="\n", file=out_file) #prints text
		print(*values1, sep=",", end="\n", file=out_file)

		print(keys1, sep=",", end="\n", file=out_file) #prints in list format
		print(values1, sep=",", end="\n", file=out_file)

		print(dictionary, sep=",", end="\n", file=out_file) #prints in dic format
		
else:
	print('File already exists!')

 
