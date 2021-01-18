string = "abcd  efgh"



#print(string[4].isspace())

i = 0

while i < len(string):
        if i % 2 == 0:
            u = string[i].upper()
            print(u, end="")
        elif i % 2 != 0:
            l = string[i].lower()
            print(l, end="")

        i = i + 1

