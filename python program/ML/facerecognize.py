import cv2 as pp
pic=pp.imread("apj.png")
print()
if pic is None:
    print("picture not found")
else:
    print(type(pic))
    mx,my,mz=pic.shape
for x in range(mx):
    for y in range(my):
        b=int(pic[x][y][0]) #blue value
        g=int(pic[x][y][1]) #green value
        r=int(pic([x][y][2])) # red value
        bwvalue=int((r+g+b)//3) #average RGB

        pic[x][y][0]=bwvalue
        pic[x][y][1]=bwvalue
        pic[x][y][2]=bwvalue
        print(r,g,b)
    output=pp.imshow("show picture",pic)
    print(output)
    pp.imwrite("apj.png")    #save to disk
    output=pp.waitkey(0)
