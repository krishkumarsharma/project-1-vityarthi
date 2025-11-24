items=[]
def a():
    d=input("Date (YYYY-MM-DD): ")
    c=input("Category: ")
    try:
        x=float(input("Amount: "))
    except:
        print("Invalid amount")
        return
    s=input("Note: ")
    items.append({"d":d,"c":c,"x":x,"s":s})
    print("Added")

def b():
    if not items:
        print("No data")
        return
    n=1
    for i in items:
        print(n,"|",i["d"],"|",i["c"],"|",i["x"],"|",i["s"])
        n+=1

def c():
    k=input("Category to search: ")
    z=[i for i in items if i["c"].lower()==k.lower()]
    if not z:
        print("None found")
        return
    for i in z:
        print(i["d"],i["x"],i["s"])

def d():
    print("Total =",sum(i["x"] for i in items))

while True:
    print("\n1 Add\n2 View\n3 Search Category\n4 Total\n0 Exit")
    u=input("> ")
    if u=="1":
        a()
    elif u=="2":
        b()
    elif u=="3":
        c()
    elif u=="4":
        d()
    elif u=="0":
        print("Bye")
        break
    else:
        print("Invalid")