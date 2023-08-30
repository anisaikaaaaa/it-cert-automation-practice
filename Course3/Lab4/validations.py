#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
def validate_user(username, min_length):
    if len(username) < min_length:
        return False
    
    # Check if the first character is a letter
    if not re.match(r'^[a-zA-Z]', username):
        return False
    
    # Check if the remaining characters are alphanumeric or underscores
    if not re.match(r'^[a-zA-Z0-9_]*$', username[1:]):
        return False
    
    return True
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


