import maya.cmds as cmds

# Functions must be defined before they are called. Python reads the file from top to bottom so if you call a function before it is defined it will throw a Name Error


def create_car(tx,ty,tz):
    body = cmds.polyPlane(w=4, h=2)
    tire1 = create_tire(1.6,0,1.3)
    tire2 = create_tire(1.6,0,-1.3)
    tire3 = create_tire(-1.6,0,1.3)
    tire4 = create_tire(-1.6,0,-1.3)
    
    car_name = cmds.group(body, tire1, tire2, tire3, tire4, name = "car")
    cmds.select(clear=True)
    cmds.setAttr("{0}.translate".format(car_name), tx, ty, tz)
    
    return car_name
    
def create_tire(tx, ty, tz):
    tire = cmds.polyCylinder(ax = (0,0,1), sc=True)
    cmds.setAttr("{0}.translate".format(tire[0]), tx, ty, tz)
    cmds.setAttr("{0}.scale".format(tire[0]),0.7, 0.7, 0.275)
    
    return tire[0]

car1 = create_car(5,0,5)
car2 = create_car(5,0,-5)
car3 = create_car(-5,0,5)
car4 = create_car(-5,0,-5)
    
    