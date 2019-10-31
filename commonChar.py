s1 = input("Enter first string \n")
s2 = input("Enter second string \n")

def common(s1,s2):
    s3=''
    for i in s1:
        if i in s2:
            s3+=i
            
    if len(s3)==0:
        print("No letters common")
        
    else:
        print(s3)
        
common(s1,s2)   