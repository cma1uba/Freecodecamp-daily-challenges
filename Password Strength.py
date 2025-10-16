import re
#The `re` module supports regular expressions in python important for pattern matching.

def checkStrength():
	"""Checks how many  conditions are met then assign input password into:
		- weak
		- medium
		- strong """
	
	#Initialize 
	password = input("Enter your password: ")
	condition_met = 0
	
	#check for password length
	if len(password) >= 8:
		condition_met += 1
		
	#Check case (atleast one uppercase and lowercase)	
	if any(c.islower() for c in password) and any(c.isupper() for c in password):
		condition_met += 1
		
	#Check digits
	if any(c.isdigit() for c in password):
		condition_met += 1
		
	#Check special characters	
	special_char = r'[@#$&%^*!]'
	if re.search(special_char, password):
		condition_met += 1
	
	#Determine strength based on number of conditions met	
	if condition_met == 4:
		return "strong"
	elif condition_met >= 2:
		return "medium"
	else:
		return "weak"
	
print(checkStrength());
