class HashMap:
    def __init__(self):
        self.l = []        
        for _ in range(10):
            self.l.append([])
        print self.l
    
    def add(self,key,value):
        hash_key = reduce(lambda x,y:x+y,[ord(c) for c in str(key)])
        self.l[hash_key%(len(self.l)-1)].append((key,value))
        print self.l

    def get(self,key):
        hash_key = reduce(lambda x,y:x+y,[ord(c) for c in str(key)])
        l = self.l[hash_key%(len(self.l)-1)]
        for tup in l:
            if tup[0] == key:
                return tup[1]
        raise KeyError

hm = HashMap()
hm.add("ab",5)
print(hm.get("ab"))