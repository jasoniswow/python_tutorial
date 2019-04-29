
file_list = open("file_list.txt")

for line in file_list:
  size = line[29:31]
  fileName = line[47:92]
  if size[1] == "M":
    size = size[0]
    fileName = line[46:91]
  if int(size) < 40 or int(size) > 50:
    print "file "+fileName+" has abnormal size: "+size+"MB"

