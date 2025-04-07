import re

url_pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'

text = "Visit our website at https://www.example.com/page"

match = re.search(url_pattern, text)

if match:
    print("Valid URL found:", match.group())
else:
    print("No valid URL found.")