import chars, sys

fn = sys.argv
fn.pop(0)
m = fn[2]
fn = " ".join(fn)
with open(fn, 'r') as f:
    text = f.read()
f.close()

cry = ""
uncry = ""
if m == "e":
    for x in text:
        if x in chars.chardict:
            print(chars.chardict[x])
            cry += str(chars.chardict[x])
    with open(f"{fn}.cry", 'w') as f:
        f.write(cry)
    f.close()
elif m == "d":
    for x in cry:
        if x in chars.unchar:
            print(chars.unchar[x])
            uncry += str(chars.unchar[x])
    with open(f"{fn}.uncry", 'w') as f:
        f.write(uncry)
    f.close()
