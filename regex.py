import re
class reg():
    def __init__(self,regex,data):
        self.regex = regex
        self.data = data
    def find_all(self):
        r1 = re.findall(self.regex,self.data)
        out = ""
        for i in r1:
            out = out + "\n" + i
        return out