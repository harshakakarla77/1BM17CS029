class admission:
    def __init__(self,i):
        self.id=None
        self.age=None
        self.marks=None

    def get_val(self):
        self.id=int(input("ID:"))
        self.age=int(input("Age:"))
        self.marks=int(input("Marks:"))

    def validate_age(self):
        if(self.age>20 and self.age<=100):
            return True
        return False

    def validate_marks(self):
        if(self.marks>=0 and self.marks<=100):
            return True
        return False

    def check_qualification(self,ag,mar):
        if(ag and mar):
            if(self.marks>=60):
                return True
            return False
        return False

li=[]
for i in range(3):
    li.append(admission(i))    
for i in range(3):
    print("Student ",i+1) 
    li[i].get_val()
    ag=li[i].validate_age()
    mar=li[i].validate_marks()
    val=li[i].check_qualification(ag,mar)
    if(val):
        print("You are selected\n")
    else:
        print("Better luck next time\n")

    
