class email():
    def __init__(self, val):
        self.val=val
        self.validate()
    def validate(self):
        errtype=''
        if "@" not in self.val:
            errtype='missing @'
        elif "." not in self.val.partition("@")[2]:
            errtype='incorrect domain'
        if errtype!='':
            raise ValueError("Invalid email address")
        return True
    def domain(self):
        return self.val.partition("@")[2]
    
em1=email('mkv102007@gmail.com')
print(em1.validate())
print(em1.domain())
try:
    em2=email('mkv102007gmail.com')
except ValueError:
    print(ValueError)