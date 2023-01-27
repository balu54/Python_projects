def Writer(file,linenumber,content):
    a = open(file, "r")
    li = a.readlines()
    my = len(li)
    a.close()
    linenumber = linenumber - 1

    if len(li) == linenumber:
        last = li[-1]
        li.pop()
        last = last + "\n"
        li.append(last)
        li.append(content)
    else:
        first = li[:linenumber]
        second = li[linenumber + 1:]
        first.append(content + "\n")
        first.extend(second)
        li = first
    b = open(file, "w")
    for i in li:
        b.write(i)
    b.close()


def Read(file,linenumber):
    l = open(file,"r")
    li = l.readlines()
    l.close()
    print(li[linenumber-1])
    return li[linenumber-1]






if __name__ == "__main__":
    file = input("enter the file name >> ")
    linenumber = int(input("Enter line number >> "))
    content = input(f"Enter the content to replace in the line {linenumber}")
    Writer(file, linenumber, content)
    Read(file, linenumber)