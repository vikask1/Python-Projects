import pickle
def CreateFile():
    bookno=int(input("Enter book number:"))
    bookname=input("Enter book name:")
    author=input("Enter author name:")
    price=int(input("Enter price:"))
    f=open("book.dat","wb")
    li=[bookno,bookname,author,price]
    pickle.dump(li,f)
    f.close()

def CountRec():
    c=0
    author=input("Enter author name to be searched")
    f=open("book.dat","rb")

    try:
        while True:
            data=pickle.load(f)
            for i in data:
                print(i)
    except EOFError:
        pass
            
    f.close()
    print(c)
CreateFile()
CountRec()
