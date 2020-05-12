import json

class People():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
    def inputs(self,numbers,files):
        self.numbers=input("please input you like num:")
        self.files=files
        with open(files,'w') as f_obj:
            json.dump(self.numbers,f_obj)
    def represent(self,file):
        self.file=file
        # with open(file,'w') as f_obj:
            # json.dump(self.numbers,f_obj)
            # json.dump(self.first_name,f_obj)
            # json.dump,f_obj)
        
    def printsz(self):
        with open('bts.txt') as f_obj:
            
            contents=json.load(f_obj)
        print("I KNOW YOUR favorite number !" +contents)
user_people=People('cheng','xuyuan')
# user_people.represent('bts.txt')
user_people.inputs('','bts.txt')
user_people.printsz()