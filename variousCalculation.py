class calculation():
    
    def subfieldsInAI():
        print("Sub Fields in AI are:")
        subfields=["machine_learning","neural_networking", "vision", "robotices", "speach_processing", "NLP"]
        for i in subfields:
            print(i)
    
    
    def oddeven():
        Num=int(input("Enter the number:"))
        if(Num%2==0):
            print(Num,"is even number")
            meassage="even number"
        else:
            print(Num,"is odd number")
            meassage="odd number"
        return meassage
   
    
    def eligible():
        genter=input("your genter:")
        age=int(input("your age:"))
        if(genter=="male"):
            if(age==23):
                print("Eligibel for marriage")
            else:
                print("Not Eligibel for marriage")
        else:
            if(age==18):
                print("Eligibel for marriage")
            else:
                print("Not Eligibel for marriage")
   
        
    def percentage():
        s1=int(input("subject 1="))
        s2=int(input("subject 2="))
        s3=int(input("subject 3="))
        s4=int(input("subject 4="))
        s5=int(input("subject 5="))
        total=s1+s2+s3+s4+s5
        print("total: ",total)
        percentage=(total/5)
        print("percentage: ",percentage)
    
        
    def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula: ((Height*Breadth)/2)")
        area=(Height*Breadth)/2
        print("area of triangle: ",area)  
        Height1=int(input("Height:"))
        Height2=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=Height1+Height2+Breadth
        print("perimeter of triangle",perimeter)
    