import operator

text = open("Z:\script.sql","rt", encoding="utf-8").read()
dic = {}
for c in text:
    if(c in dic):
        dic[c]=dic[c]+1
    else:
        dic[c]=1

print(sorted(dic.items(), key=lambda kv: kv[1],reverse=True))


