f = open("yesterday.txt",'r')
yesterday_lyrec=""
while 1:
    line - f.readline()
    if not line : break
    yesterday_lyric - yesterday_lyric+line.strip()+"\n"
    f.close()
    n_of_yesterday = yesterday_lyric.upper().count("yesterday")
print "number of a word "Yesterday",n_of_yesterday

