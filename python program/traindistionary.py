train={101:{'rajdhani exp':{1:{'vns':0},2:{'lko':20},3:{'knp':45},4:{'ndls':60}}},102:{'shivganga exp':{1:{'vns':0},2:{'prj':20},3:{'knp':45},4:{'ndls':60}}},103:{'mahamana exp':{1:{'vns':0},2:{'jnp':5},3:{'lko':20},4:{'knp':40},5:{'ndls':65}}}2,104:'mahanagri exp'}
print(train)
while (True):
    print("0-exit, 1-add,2-search")
    option=int(input("enter the option:"))
    if option==0:
        break
    if option==1:
        print("add element:")
        key=int(input("enter the key:"))
        ch= input("enter train :")
        train[key]=ch
    if option==2:
        print("search train:")
        key=int(input("enter the key"))
        x=train.get(key)
        print(x)