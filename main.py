# for i in range(1,40):
#     print("\"",i,".\",",end="",sep="")
a=["1.","2.","3.","4.","5.","6.","7.","8.","9.","10.","11.","12.","13.","14.","15.","16.","17.","18.","19.","20.","21.","22.","23.","24.","25.","26.","27.","28.","29.","30.","31.","32.","33.","34.","35.","36.","37.","38.","39."]
f2=open("out.md","w")
with open("in.txt","r") as f:
    for lines in f.readlines():
        if (lines.strip() in a):
            print(lines.strip())
            print("```\n\n### ["+lines.strip()+"]("+"../programs/chapter6/6."+lines.strip()+"c"+")\n\n```c",file=f2)
            f1=open("6."+lines.strip()+"c","w")
        else:
            print(lines.strip("\n"),file=f1)
            print(lines.strip("\n"),file=f2)
print("```",file=f2)
