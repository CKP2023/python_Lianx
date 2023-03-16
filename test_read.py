# import csv
#
#
path2 = "C:\\Users\\chenkp\\Desktop\\out.txt"
with open(path2,"r") as f:
    for read in f:
        read = read.replace("\n","")
        # print(read)

        path1 = "out.txt"
        with open(path1,'r') as f:
            for txt in f:
                reads = (txt.replace('\n',"")).split(",")

                if read == reads[1]:
                    print(reads)




# 测试而已
#
# path = 'C:\\Users\\chenkp\\Desktop\\out.CSV'
# with open(path,'r') as csvfile:
#     reader = csv.reader(csvfile)
#     print(type(reader))
#     for row in reader:
#         if read == row[1]:
#             print(type(row[1]),row[1])
#
# # print(read==row[1])
