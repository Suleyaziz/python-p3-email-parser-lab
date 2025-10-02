import re

class EmailAddressParser:
    '''Parses email addresses from a string with various separators'''
    
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        '''Extracts and returns sorted list of valid email addresses'''
        # Split by both commas and spaces, then filter out empty strings
        potential_emails = re.split(r'[,\s]+', self.email_string)
        
        # Filter valid email addresses using regex
        valid_emails = []
        email_pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        
        for item in potential_emails:
            if item and email_pattern.match(item):
                valid_emails.append(item)
        
        # Return sorted list (alphabetically)
        return sorted(valid_emails)