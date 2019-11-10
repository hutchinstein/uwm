class foo :
    def __init__(self, v):
        self.value = v
    def change(self,v):
        value = v
    def getValue(self):
        return self.value

def main() :

    x = foo(1)

    x.change(10)

    x.change(100)

    print(x.getValue())

main()