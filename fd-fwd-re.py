import re

def email_chain_count(subject):
    # Define the pattern to look for fw:, fwd:, or re:
    # re.IGNORECASE ensures we catch "RE:", "Fw:", etc.
    pattern = r"(fw:|fwd:|re:)"
    
    # findall returns a list of all matches found in the string
    matches = re.findall(pattern, subject, re.IGNORECASE)
    
    return len(matches)

# --- Test Cases ---
print(email_chain_count("Re: Fwd: Fw: Count"))  # Output: 3
print(email_chain_count("RE: Meeting tomorrow")) # Output: 1
print(email_chain_count("Just a regular email")) # Output: 0