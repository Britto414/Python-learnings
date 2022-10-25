class birds:
    def __init__(self ,name,age):
        self.name=name
        self.age=age
        self.height=None

    def _property(self):
        if self.name=="parraot":
            return f"{self.name} speaks with humans"
        else:
            return f"{self.name} can touch the sky"
    
    def _printdetails(self):
        return f'hello my name is {self.name} and my age is{self.age} '
eagle=birds("eagle", 10)
print(eagle._property())