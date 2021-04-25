a={"bir":[1,2,3,4],"iki":[[1,2],[3,4]]}
print(a["iki"])
print(a["iki"][1][1])
print(a["iki"][1][1]+5)

b={"sayilar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz meyvesi","portakal":"kis meyvesi"}}
print("b= ",b["sayilar"]["iki"])
print(b.items())
print(b.keys())
print(b.values())
