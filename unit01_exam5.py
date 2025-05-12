# Get user email address
email = input("Please enter your email:").strip()

# Slice out the user name
user_name = email[0:email.index('@')]
#print(user_name)
# Slice out the domain name
domain_name = email[email.index('@')+1:len(email)]
#print(domain_name)
# Format message
output = "Your user name is '{}' and your domain name is '{}' ".format(user_name, domain_name)
print(output)
#print("Your user name is '%s' and your domain name is '%s' "%(user_name, domain_name))

# Which company does the domain belong to?
domain = {'gmail.com':'Google', 'yahoo.com.tw':'Yahoo', 'hotmail.com':'Microsoft', 'coretronic.com':'Coretronic'}
if domain_name in domain:
  output = "The domain name of email belongs to '{}'. ".format(domain[domain_name])
  print(output)