class strpar():
    def ver_str(self,str1):
        f=1
        for i in range(len(str1)):
                    if(str1[i]=='(' and str1[i+1]!=')'):
                       f=0
                       break
                    if(str1[i]=='{' and str1[i+1]!='}'):
                        f=0
                        break
                    if(str1[i]=='[' and str1[i+1]!=']'):
                        f=0
                        break
            
        if(f==1):
            print("Valid")
        if(f==0):
            print("Invalid")

str1=input("Enter the string of paranthesis:")
p=strpar()
p.ver_str(str1)                       
                               
                               
        
            
            
