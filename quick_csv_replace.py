old_new = [i.strip().split(',') for i in open('Replace_def.csv')]

with open('new.txt', 'w') as outfile, open('GCHC.txt') as infile:
    txt = infile.read()
    for oldword, newword in old_new:
        txt = txt.replace(oldword, newword)
    outfile.write(txt)