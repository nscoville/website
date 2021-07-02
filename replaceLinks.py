import glob

for origpath in ["http://webpages.ursinus.edu/nscoville/", "/nscoville/"]:
    for f in glob.glob("**/*.html", recursive=True):
        ndirs = len(f.split("/"))-1
        fin = open(f, encoding="utf8", errors='ignore')
        s = fin.read()
        fin.close()
        if origpath in s:
            print(f)
            s = s.replace(origpath, "../"*ndirs)
            fout = open(f, "w")
            fout.write(s)
            fout.close()