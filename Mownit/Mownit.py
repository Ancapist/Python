from PIL import Image



iterations = 50
E = 1e-4
maxf= 1e10
minf= 1e-10

xa=-1
xb= 1
ya=-1
yb= 1

def f(z):
    return z**4+1
def df(z):
    return 4*z**3

def checkifinres(res,ress):
    for i in ress:
        if abs(res-i)<1e-3:
            return False
    return True

def Newton_Results(z):
    for i in range(iterations):
        h = f(z)/df(z)
        if abs(f(z))<minf or abs(f(z))>maxf :return None
        if abs(h)<E:return z
        z = z - h
    return None

def printImage(img):
    results = []
    y=0
    while y<512:
            x=0
            zy = ya + y*(yb-ya)/(511)
            while x<512:
                zx = xa + x*(xb-xa)/(511)
                result = Newton_Results(complex(zx,zy))          
                if result and checkifinres(result,results):
                    results.append(result)                   
                if result:                
                    img.putpixel((x,y),(128,0,0))
            
                if not result:
                    img.putpixel((x,y),(124,252,0))  
                x+=1
            y+=1
    print (results)
    img.save("Image", "PNG")


image = Image.new("RGB",(512,512),(255,255,255))
printImage(image)


