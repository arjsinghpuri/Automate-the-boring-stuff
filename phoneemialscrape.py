#! usr/bin/env python3

import re, pyperclip

#Create regex for phone number
# could be 111-111-1111, 111-1111, (111) 111-1111, 111-1111 ext 1111, 
# ext. 12345, x12345
phoneRegex =re.compile(r'''
(
(\d\d\d | \(\d\d\d\))?       #area code (optional)
(- | \s)                    
\d\d\d                          #next 3 digits  
(- | \s)
\d\d\d\d                        #last 4 digits  
(ext(\.)?\s\d{2, 5} | x\d+)?    #extension (optional)  
)                
''', re.VERBOSE)

#Create regex for email addresses
#could be some._+thing@something.com

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+       #character class for name part of email
@
[a-zA-Z0-9_.+]+       #character class for the domain of email
''', re.VERBOSE)

#Get the text off the clipboard
alltext = pyperclip.paste()

#Extract the email/phone from the text
extractedphone = phoneRegex.findall(alltext)
extractedemail = emailRegex.findall(alltext)

phonenos = []
for tup in extractedphone:
    phonenos.append(tup[0])

#Copy the extracted email/phone to clipboard
result = '\n'.join(phonenos) + '\n' + '\n'.join(extractedemail)
pyperclip.copy(result)