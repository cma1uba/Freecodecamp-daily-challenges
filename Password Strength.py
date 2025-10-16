import re

def check_strength(password):
    """
    Evaluates the strength of a password based on four rules.
    Returns 'weak', 'medium', or 'strong'.
    """
    
    # Initialize a counter for rules met
    rules_met = 0
    
    # 1. Check Length (at least 8 characters)
    if len(password) >= 8:
        rules_met += 1
        
    # 2. Check Case (contains both uppercase and lowercase letters)
    # Checks if there is at least one lowercase letter AND at least one uppercase letter
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        rules_met += 1
        
    # 3. Check Number (contains at least one number)
    if any(c.isdigit() for c in password):
        rules_met += 1
        
    # 4. Check Special Character 
    # The required set is: !, @, #, $, %, ^, &, *
    special_chars = r'[!@#$%^&*]'
    if re.search(special_chars, password):
        rules_met += 1
        
    # Determine strength based on the number of rules met
    if rules_met == 4:
        return "strong"
    elif rules_met >= 2: # This covers 2 and 3
        return "medium"
    else: # This covers 0 and 1
        return "weak"
