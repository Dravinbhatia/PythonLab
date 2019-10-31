s1 = input("Enter the first string \n")
s2 = input("Enter the second string \n")

def CommonChar(s1,s2):
    s3=''
    for i in s1:
        if i in s2:
            s3+=i
            
    if len(s3)==0:
        print("No letters are common")
        
    else:
        print(s3)
        
commonChar(s1,s2)   
