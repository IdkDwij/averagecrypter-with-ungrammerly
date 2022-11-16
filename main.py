import chars, sys

with open(sys.argv[2], 'r') as f:
    text = f.read()
f.close()

cry = ""
uncry = ""
if sys.argv[1] == "e":
    for x in text:
        if str(x) in chars.chardict:
            cry += str(chars.chardict[x])
    with open(f"{sys.argv[2]}.cry", 'w') as e:
        e.write(cry)
    e.close()
elif sys.argv[1] == "d":
    for x in text:
        if str(x) in chars.unchar:
            uncry += str(chars.unchar[x])
    with open(f"{sys.argv[2]}.uncry", 'w') as g:
        g.write(uncry)
    g.close()
