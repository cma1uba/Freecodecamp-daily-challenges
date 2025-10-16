import re

def strip_tags(html: str) -> str:
  """
  Removes all HTML tags and their attributes from a string,
  returning the plain text content.
  """
  # The regular expression r'<[^>]*>' matches:
  # <      : The opening angle bracket
  # [^>]   : Any character that is NOT a closing angle bracket
  # * : Zero or more of the preceding characters (the content of the tag)
  # >      : The closing angle bracket
  # The r'' prefix denotes a raw string, which is good practice for regex in Python.
  return re.sub(r'<[^>]*>', '', html)

# Example Usage:
html1 = '<a href="#">Click here</a>'
print(strip_tags(html1))

html2 = '<h1>Nested <b>Tags</b> are tricky!</h1>'
print(strip_tags(html2)) 

html3 = '<span>Text with <br> break tag</span>'
print(strip_tags(html3)) 