#因為沒有要輸入成績的環節
#所以我就偷懶了一下嘻嘻

import math

#學生的成績為: 10, 30, 40, 90, 100, 62
x = (10 + 30 + 40 + 90 + 100 + 62)/ 6
y = math.sqrt(((10-x)**2+(30-x)**2+(40-x)**2+(90-x)**2+(100-x)**2+(62-x)**2)/6)

a = input()
if a == "1a":
    print(round(x))
elif a == "1b":
    print(math.ceil(x))
elif a == "1c":
    print(math.floor(x))
elif a == "2":
    print(round(y,2))
else:
    pass
