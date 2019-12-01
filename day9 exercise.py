# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:10:56 2019

@author: AbeerJaafreh
"""
import  statistics  as st
import random
import math
from PIL import Image,ImageFilter,ImageDraw


#Question 1 -----------------------------------------------
x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
    
print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))
"""Solution
3.7142857142857144
2.8769027134348115
3
3
3
3.0
2.25
1.8391990270833904
3.38265306122449
1.9865619978819116
3.9464285714285716
"""
print('-----------------------------------------------')
#Question 2 -----------------------------------------------
print(random.random())
print(random.randrange(10))
print(random.choice(['Ali','Khaled','Hussam']))
print ( random.sample(range(100), 10) ) 
print(random.choice('OrangeAcademy'))
Number = [1,5,8,9,2,4]
random.shuffle(Number) 
print( Number ) 
print ( random.randint(20, 30) ) 
print ( random.randrange(1000, 2111, 5) ) 
print  ( random.uniform(10000, 11000))
"""Solution
0.26730221862635606
0
Ali
[66, 21, 37, 74, 90, 68, 65, 88, 12, 44]
e
[5, 1, 8, 9, 4, 2]
25
1025
10643.749418675492
"""
print('-----------------------------------------------')

#Question 3 -----------------------------------------------
c=200
s=30
t=180
print ('pi: %.40f' % math.pi)
print ('arcsine(%.1f)    = %5.2f' % (s, math.sin(s))) 
print ('arccosine(%.1f)  = %5.2f' % (c, math.cos(c))) 
print ('arctangent(%.1f) = %5.2f' % (t, math.tan(t)))
n=10.8
print("floor ",n,": ",math.floor(n)) 
print("ceil ",n,":",math.ceil(n))
"""Solution
pi: 3.1415926535897931159979634685441851615906
arcsine(30.0)    = -0.99
arccosine(200.0)  =  0.49
arctangent(180.0) =  1.34
floor  10.8 :  10
ceil  10.8 : 11
"""
print('-----------------------------------------------')

#Question 4 -----------------------------------------------
image1=Image.open("bbb.jpeg")
img=image1.copy()
image2=Image.open("home.jpg").resize(image1.size)
img2=image2.copy().resize(img.size)

print(image1.format,",",image1.size,",",image1.mode)

image1_flip=image1.transpose(Image.FLIP_TOP_BOTTOM)
image2_flip=image2.transpose(Image.FLIP_TOP_BOTTOM)
image1_flip.show()
image2_flip.show()

gray=image1.convert('L') #convert to grayscale 
gray1=image2.convert('L') #convert to grayscale 
gray.show()
gray1.show()

copped=image1.crop((0,0,50,50))
copped.show()

draw=ImageDraw.Draw(image1)
draw.line((0,0)+image1.size,fill=(255,255,255))
draw.line((0,image1.size[1],image1.size[0],0),fill=(255,255,255))
draw.text((image1.size[0]/2 - image1.size[0]/2,image1.size[1]/2-60),"Abeer Jaafreh",fill=(255,255,0))

enhanced=image2.filter(ImageFilter.EDGE_ENHANCE)
find_enhanced=image2.filter(ImageFilter.FIND_EDGES)
smooth=image2.filter(ImageFilter.SMOOTH)
sharpen=image2.filter(ImageFilter.SHARPEN)
enhanced.show()
find_enhanced.show()
smooth.show()
sharpen.show()

alpha=0.5
Image.blend(image1,image2,alpha).save("new.jpeg".format(alpha))
newImage=Image.open("new.jpeg")
newImage.show()

blurred=image2.filter(ImageFilter.BLUR)
blurred.show()

size=(128,128)

image2.thumbnail(size) #thumbnail
image2.show()

image1_rotate_90=image2.rotate(90)
image1_rotate_90.show()


maskImage=Image.open("mask_circle.jpg")
maskImage=maskImage.resize(image1.size)
Image.composite(img,img2,maskImage).save("newMaskImage.jpg")
newMaskImage=Image.open("newMaskImage.jpg")
newMaskImage.show()
image1.show()
