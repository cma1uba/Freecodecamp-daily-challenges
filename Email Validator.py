import re

def validate_email(email: str) -> bool:
    """
    Determines if a string is a valid email address based on the challenge constraints.
    """
    # Regex breakdown:
    # ^ : Start of the string.
    #
    # [a-zA-Z0-9_-]+ : Start of the local part. Must be one or more allowed chars (excluding dot).
    # (?: \. [a-zA-Z0-9_-]+ )* : Optional group for dots in the middle.
    #                            A dot must be followed by one or more allowed chars (excluding dot).
    #
    # @ : The required single '@' symbol.
    #
    # [a-zA-Z0-9-]+ : Start of the domain name. One or more allowed chars (excluding dot).
    #
    # \. : The first required dot in the domain.
    #
    # [a-zA-Z0-9-]+ : One or more chars before the TLD dot.
    # (?: \. [a-zA-Z0-9-]+ )* : Optional groups for subdomains (e.g., .co.uk).
    #
    # \. : The final required dot before the TLD.
    #
    # [a-zA-Z]{2,} : The TLD (Top-Level Domain). Must be at least two letters.
    #
    # $ : End of the string.
    
    # NOTE: The challenge specifies the local part can contain dots, but NOT start/end with one.
    # The regex below precisely implements the "local part" and "domain part" rules.
    
    # Local Part: [a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)*
    # Domain Part: [a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}
    
    # Combined regex to enforce all constraints:
    # 1. Local part doesn't start/end with a dot, but allows internal dots:
    #    [a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*
    # 2. Domain part has at least one dot and ends with .<2+ letters>:
    #    [a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}
    
    regex = r"^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$"

    # re.fullmatch ensures the ENTIRE string matches the pattern, 
    # automatically fulfilling the "exactly one @" constraint since it's required 
    # to be in that specific middle position of the pattern.
    if re.fullmatch(regex, email):
        return True
    return False

# Example Usage:
# print(validate_email("user.name123_@sub.domain-name.co")) # Valid: True
# print(validate_email("user.name123_@domain.com"))        # Valid: True
# print(validate_email("test@.com"))                       # Invalid (domain starts with dot): False
# print(validate_email(".test@domain.com"))               # Invalid (local starts with dot): False
# print(validate_email("test@domain.c"))                  # Invalid (TLD < 2 chars): False
# print(validate_email("test@domain..com"))               # Invalid (consecutive dots): False
# print(validate_email("user.name.@domain.com"))          # Invalid (local ends with dot): False