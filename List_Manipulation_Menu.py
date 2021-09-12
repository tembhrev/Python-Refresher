ch = 0
list = []
while True:
    print("List Manipulation Menu")
    print("1. Add Elements(s)")
    print("2. Modify Element")
    print("3. Delete Element")
    print("4. Sort list")
    print("5. Display list")
    print("6. Exit")
    ch = int(input("Enter your choice (1..6) :"))
    if ch == 1:
        print("1. Add one element")
        print("2. Add a list")
        ch1 = int(input("Enter your choice (1..2) :"))
        if ch1 == 1:
            item = int(input("Enter element :"))
            pos = int(input("Enter position where to add :"))
            list.insert(pos, item)
        elif ch1 == 2:
            lst2 = eval(input("Enter list to be added:"))
            list.extend(lst2)
        else:
            print("Valid choices are 1 and 2 ...Returning..")
        print("Successfully added.")
    elif ch == 2:
        pos = int(input("enter position where to modify :"))
        item = int(input("Enter new value for element :"))
        old = list[pos]
        list[pos] = item
        print("{} modified with value {}".format(old, item))
    elif ch == 3:
        print("1. Delete element by position")
        print("2. Delete element by value")
        ch1 = int(input("Enter your choice (1..2) :"))
        if ch1 == 1:
            pos = int(input("Enter position where to delete :"))
            item = list.pop(pos)
            print("{} deleted".format(item))
        elif ch1 == 2:
            item = int(input("Enter element to be deleted :"))
            pos = list.remove(item)
            print("Successfully deleted")
        else:
            print("Valid choices are 1 and 2 ... Returning..")
    elif ch == 4:
        print("1. Ascending")
        print("2. Descending")
        ch1 = int(input("Enter your choice (1..2) :"))
        if ch1 == 1:
            list.sort()
        elif ch1 == 2:
            list.sort(reverse=True)
        else:
            print("Valid choices are 1 and 2 ... Returning..")
    elif ch == 5:
        print(list)
    elif ch == 6:
        break
    else:
        print("Valid choices are 1 to 6...")