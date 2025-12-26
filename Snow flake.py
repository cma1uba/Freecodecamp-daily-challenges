def generate_snowflake(crystals):
    # 1. Split the string into individual lines
    lines = crystals.split('\n')
    
    mirrored_lines = []
    
    for line in lines:
        # 2. Reverse the line using slicing
        mirror = line[::-1]
        
        # 3. Attach the mirror to the end of the original line
        mirrored_lines.append(line + mirror)
    
    # 4. Join the lines back together with newline characters
    return '\n'.join(mirrored_lines)

# --- Test Case ---
input_str = "* \n * \n* "
# Original looks like:
# * #  * # * 
result = generate_snowflake(input_str)
print(result)

# Expected Output:
# * *
#  ** # **