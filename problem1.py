"""new program to check validity of email"""

def validemail(email):
    i=0
    for char in email:
        if char == "@":
            return print("found @ at index {}",i)
        i+=1
    return print("did not find @")
test1="testgmail.com"
test2="charliebrown@gmail.com"
test3="testgmail.com"
validemail(test1)
    
        
    
 