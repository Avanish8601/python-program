train={101:{'rajdhani exp':{1:{'vns':0},2:{'lko':20},3:{'knp':45},4:{'ndls':60}}},102:{'shivganga exp':{1:{'vns':0},2:{'prj':20},3:{'knp':45},4:{'ndls':60}}},103:{'mahamana exp':{1:{'vns':0},2:{'jnp':5},3:{'lko':20},4:{'knp':40},5:{'ndls':65}}},104:'mahanagri exp'}
print(train)
t=train.get(103)
print(t)
print(t.get('mahamana exp'))
print(t.get('mahamana exp').get(3))

