class parent:


    def __init__(self,name,age,dept):

        self.age = age
        self.name = name

        self.dept = "voda"+' '+str(dept)


    def produce_result(self):
        print("result has been produced by",self)



class department(parent):


    def __init__(self, dept):
        self.dept =dept
        super().__init__("varun",20,dept)


obj1 = department("analytics")

print(obj1.name)


