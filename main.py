import os

for i in range(14,15):
    dir = r"C:\Users\mista\CLionProjects\npuccppans\cpp\programs\chapter{}".format(i)
    pb_num = []
    for path, dir_list, file_list in os.walk(dir):
        for file_name in file_list:
            pb_num.append(int(file_name.strip().split()[-1].split('.')[1]))
        pb_num.sort()
    # print(pb_num)
    pb_path = []
    flag = True
    for j in pb_num:
        if (i == 8 and j == 14):
            if flag:
                pb_path.append(os.path.join(dir, "{}.{}.1.cpp".format(i, j)))
                flag = False
            else:
                pb_path.append(os.path.join(dir, "{}.{}.2.cpp".format(i, j)))
                flag = True
        elif (i == 7 and j == 17):
            if flag:
                pb_path.append(os.path.join(dir, "{}.{}.1.cpp".format(i, j)))
                flag = False
            else:
                pb_path.append(os.path.join(dir, "{}.{}.2.cpp".format(i, j)))
                flag = True
        else:
            pb_path.append(os.path.join(dir, "{}.{}.cpp".format(i, j)))
    # for pt in pb_path:
    #     print(pt)

    with open("chapter{}.md".format(i), "w") as fout:
        for path in pb_path:
            with open(path, "r") as fin:
                pb_name = path[len(r"C:\Users\mista\CLionProjects\npuccppans\cpp\programs\chapter3\3."):-4]
                # print(pb_name)
                print("### [{}.](../programs/chapter{}/{}.{}.cpp)\n\n```c++".format(
                    pb_name, i, i,pb_name), file=fout)
                if (not(i==3 and pb_name=="6")):
                    for line in fin.readlines():
                        print(line, file=fout,end="")
                print("```\n", file=fout)

exit()

# g = os.walk(r"C:\Users\mista\CLionProjects\npuccppans\cpp\programs")
#
# for path, dir_list, file_list in g:

# for i in range(1,40):
#     print("\"",i,".\",",end="",sep="")
#
# for i in range (12,19):
#     print("### ["+str(i)+".](../programs/chapter6/6."+str(i)+".cpp)\n\n```c++\n\n```\n")
#     with open("8."+str(i)+".cpp","w") as f:
#         print("",file=f,end="")

# exit()
# a=["1.","2.","3.","4.","5.","6.","7.","8.","9.","10.","11.","12.","13.","14.","15.","16.","17.","18.","19.","20.","21.","22.","23.","24.","25.","26.","27.","28.","29.","30.","31.","32.","33.","34.","35.","36.","37.","38.","39."]
# f2=open("out.md","w")
# with open("in.txt","r") as f:
#     for lines in f.readlines():
#         if (lines.strip() in a):
#             print(lines.strip())
#             print("```\n\n### ["+lines.strip()+"]("+"../programs/chapter6/6."+lines.strip()+"c"+")\n\n```c",file=f2)
#             f1=open("6."+lines.strip()+"c","w")
#         else:
#             print(lines.strip("\n"),file=f1)
#             print(lines.strip("\n"),file=f2)
# print("```",file=f2)
