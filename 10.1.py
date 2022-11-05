import os

path = "e:\\text1\\"

filenames = os.listdir (path)
a = 0
for i in filenames:
    o_name = path +filenames[a]
    n_name = path + "N-" + filenames[a]
    os.rename (o_name,n_name)
    print("文件{}重命名成功，改为{}".format (o_name,n_name))
    a = a+1
    
