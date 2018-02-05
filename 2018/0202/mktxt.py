lines = []
with open("texts.txt", "r") as r:
  for row in r:
    lines.append(row)

for i in range(len(lines)):
  line = lines[i]
  if (i < 10):
    s = "0" + str(i)
  else:
    s = str(i)
  with open(s + ".txt", "w") as w:
    w.write(line)