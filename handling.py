try:
    a=121
    b=456
    f = open("ab.txt")
    p=b/0

    for line in f:
        print(line)
except FileNotFoundError as e:
    print("Anything at all",e.filename)
#except (FileNotFoundError , ZeroDivisionError):
#    print("File not found  0xFFwegergnid0KJKH")
#i=0/0
#except ZeroDivisionError:
#    print("Divided By Zero")
# lol
