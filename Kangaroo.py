class Kangaroo:
    def __init__(self, name, contents=None):
        if contents==None:
            contents = []
        self.pouch_contents = contents
        self.name = name

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = ' ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)




j = Kangaroo('john')
j.put_in_pouch('candy')
j.put_in_pouch('button')
p = Kangaroo('pete')
j.put_in_pouch(p)
print(p)
print(j)




