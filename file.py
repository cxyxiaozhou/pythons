class Username(object):
    def __init__(self,inputs,file):
        self.inputs=raw_input("please input name")
    def written(self):
        self.file=self.inputs
        with open(self.file,'w') as file_object:
            file_object.write("I love you 雷欣窈")
    def inputlv(self):
        print(file_object)
filename=Username()
filename.inputlv()                  
