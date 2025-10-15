def count(text, parameter):
	''' Counts occurance of "parameter" in "text" allowing overlap
	'''
	if not parameter:
		return 0
	
		#initialize	
	count = 0 
	parameter_length = len(parameter)
	text_length = len(text)
	
	#iterate the text until where a full pattern match is possible
	for i in range(text_length - parameter_length + 1):
		slice = text[i : i + parameter_length]
		
		if slice == parameter:
			count += 1
			
	return count
	
fruit_pattern =  count("banana", "ana")
print(fruit_pattern)