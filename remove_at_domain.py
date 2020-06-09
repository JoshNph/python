# write your code here
email = "lisa@blackpink.com"
local = ""

#these 5 lines
for char in email:
    local += char
    if char == '@':
        break
print(local[:-1])

#are same as these 2 lines
index_of_at = email.index('@')
print(email[:index_of_at])

#and also these 2 lines
result = email.split('@')[0]
print(result)
# remember: the variable email is already defined
