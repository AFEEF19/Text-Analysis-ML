import re
import json

phone_pattern = r'(\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

with open("sample_resumes.txt", "r") as file:
    text = file.read()

phones = re.findall(phone_pattern, text)
emails = re.findall(email_pattern, text)

output = {
    "phone_numbers": list(set(phones)),
    "email_addresses": list(set(emails))
}

with open("output.json", "w") as json_file:
    json.dump(output, json_file, indent=4)

print("Extraction complete. Data saved to output.json")
