from PyPDF2 import PdfFileReader


def generate(arr,i,s,len_arr):
    
   
    if(i==0):
        s1=len(s)
        if(s1==5):
            reader = PdfFileReader("secret.pdf")
           
            
            try:
                if reader.decrypt(s) == 1:
                    print("{} is the right one".format(s))
                else:
                    print("{} is not correct password".format(s))
                
            except:
                print("nothing")
           
                
            
            
        return
    
    for j in range(0,len_arr):
        
        appended=s+arr[j]
        generate(arr,i-1,appended,len_arr)
    return


def cracking(arr,len_arr):
    for i in range(1,len_arr+1):
        generate(arr,i,"",len_arr)
       


arr=['x','y','z','Z','1']
len_arr=len(arr)
cracking(arr,len_arr)
