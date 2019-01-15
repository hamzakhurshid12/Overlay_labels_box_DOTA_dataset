from PIL import Image, ImageDraw, ImageFont
import os

directory="C:\\Users\\Hamza Khurshid\\Desktop\\puzzledqs-BBox-Label-Tool-80b9b8d\\puzzledqs-BBox-Label-Tool-80b9b8d\\Images\\001\\"
images=os.listdir(directory)
directory_labels="D:\\University\\Semester-4\\Machine_Learning\\Datasets\\labelTxt"
labels=[]
for x in range(len(images)):
    labels.append(os.path.join(directory_labels,images[x][:-4]+".txt"))
    images[x]=os.path.join(directory,images[x])

for x in range(50):
    im=Image.open(images[x])
    file=open(labels[x])
    fileText=file.read()
    file.close()
    lines=fileText.split("\n")[2:-1]
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 30)
    for line in lines:
        points=line.split(" ")
        draw.line((int(points[0]),int(points[1]), int(points[2]),int(points[3])), fill=128, width=3)
        draw.line((int(points[2]),int(points[3]), int(points[4]),int(points[5])), fill=128, width=3)
        draw.line((int(points[4]),int(points[5]), int(points[6]),int(points[7])), fill=128, width=3)
        draw.line((int(points[6]),int(points[7]), int(points[0]),int(points[1])), fill=128, width=3)
        draw.text((int(points[4]),int(points[5]))," ".join(points[8:]),(255,255,255),font=font)
    im.save(images[x]+"_labelled.png")
