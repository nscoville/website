import glob

#origpath = "http://webpages.ursinus.edu/nscoville/\""
origpath = "http://webpages.ursinus.edu/nscoville/"
for f in glob.glob("**/*.html", recursive=True):
    ndirs = len(f.split("/"))-1
    fin = open(f, encoding="utf8", errors='ignore')
    s = fin.read()
    fin.close()
    if origpath in s:
        replace = "../"*ndirs
        print(f, replace)
        s = s.replace(origpath, replace)
        fout = open(f, "w")
        fout.write(s)
        fout.close()
