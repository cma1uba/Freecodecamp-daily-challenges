def mask(card):
    """
    Masks a credit card number string according to the challenge constraints.
    Replaces all digits, except the last four, with an asterisk (*),
    while leaving separators (space or hyphen) unchanged.
    """
    start_of_preserved_section = len(card) - 4

    masked_card = []
    for i, char in enumerate(card):
        # Check if we are in the section that needs masking
        if i < start_of_preserved_section:
            # If the character is a digit, mask it
            if char.isdigit():
                masked_card.append('*')
            # Otherwise (it's a separator), keep it unchanged
            else:
                masked_card.append(char)
        # We are in the last four characters (including the last separator),
        # keep them unchanged
        else:
            masked_card.append(char)

    return "".join(masked_card)
    
my_card = mask("8678-4560-2455-2976")

print(my_card)