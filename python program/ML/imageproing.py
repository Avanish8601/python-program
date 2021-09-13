import cv2
import matplotlib.pyplot as plt
####normal form show image####
"""pic=cv2.imread("apj.png")
cv2.imshow("avanish",pic)
cv2.waitKey(0)"""

"""class predictorimage :
    def __init__(self,pic,label):
        self.pic=pic
        self.label=label"""

##### using function #####

def readimg(path):
    pic=cv2.imread(path)
    return pic
def showimg(pic):
    cv2.imshow("avanish",pic)
    cv2.waitKey(0)
    return pic

#showimg(pic)
#print(type(pic))
#print(pic)

def picpdding(pic):
    mr,mc,mz=pic.shape
    for r in range(20):
        for c in range(mc):
            pic[r][c][0]=255
            pic[r][c][1]=255
            pic[r][c][2]=255

            pic[mr-r-1][c][0]=255
            pic[mr-r-1][c][1]=255
            pic[mr-r-1][c][2]=255
    for r in range(mr):
        for c in range(20):
            pic[r][c][0] = 255
            pic[r][c][1] = 255
            pic[r][c][2] = 255

            pic[r][mc-c-1][0] = 255    # b blue
            pic[r][mc-c-1][1] = 255    #g green
            pic[r][mc-c-1][2] = 255    #r red
    return pic

def reversepic(pic):
    mr,mc,mz= pic.shape
    pic2 = pic.copy()
    for r in range(mr):
        pic2[r]=pic[mr-1-r]
    return pic2

def threadsold(pic):
    mr,mc,mz= pic.shape
    sum=0
    for r in range(mr):
        for c in range(mc):
            blue=int(pic[r][c][0])
            green=int(pic[r][c][1])
            red=int(pic[r][c][2])
            avg=(blue+green+red)//3
            sum+=avg

    return int(sum//(mr*mc))
def blackwhite(pic):
    pic2=pic.copy()
    t=threadsold(pic)
    mr,mc,mz=pic2.shape
    for r in range(mr):
        for c in range(mc):
            b=int(pic2[r][c][0])
            g=int(pic2[r][c][1])
            red=int(pic2[r][c][2])
            avg=(b+g+red)//3
            if avg<t:
                pic2[r][c]=[0,0,0]
            else:
                pic2[r][c]=[255,255,255]
    return pic2

def grayscale(pic):
    pic2=pic.copy()
    mr,mc,mz=pic2.shape
    for r in range(mr):
        for c in range(mc):
            b=int(pic2[r][c][0])
            g=int(pic2[r][c][1])
            red=int(pic2[r][c][2])
            avg=(b+g+red)//3
            pic2[r][c]=[avg,avg,avg]
    return pic2

def onedarray(pic):
    mr,mc,mz=pic.shape
    l=[]
    for r in range(mr):
        for c in range(mc):
            if pic[r][c][1]==255:
                l.append(0)
            else:
                l.append(1 )
    return l
def f(x):
    sum=0
    for i in range(len(x)):
        if x[i]==1:
            sum+=(i+1)**2
    sum+=1
    return sum

def imgvalue(pic):
    bw=blackwhite(pic)
    od=onedarray(bw)
    return f(od)
#listofpics = predictorimage[(reversepic("apj.png"))]

pic=readimg("apj.png")
pic2=readimg("1.jpg")
pic3=readimg("eight.PNG")
pic4=readimg("five.PNG")

#pic2=picpdding(pic)

#pic3=reversepic(pic)
#pic3=blackwhite(pic)
#pic3=grayscale(pic)
#a=onedarray(pic3)
#print(a)
#showimg(pic4)
imgvalue(pic)
#print(pic3)
print("1",imgvalue(pic))
print("2",imgvalue(pic2))
print("3",imgvalue(pic3))
print("4",imgvalue(pic4))

x=[1,2,3,4]
y=[imgvalue(pic),imgvalue(pic2),imgvalue(pic3),imgvalue(pic4)]
plt.plot(x,y,color="red")
plt.scatter(x,y,color="green",marker="o")
plt.show()

