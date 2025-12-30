
import cv2
import struct

vidcap = cv2.VideoCapture('badapple.mp4')
success,image = vidcap.read()
count = 0

writetofile = "1x1.txt"
with open(writetofile, 'w') as f:
    pass 
file = open(writetofile,'ab');

height = len(image)
width = len(image[0])

#file.write(str(height) + ' ' + str(width))
#file.write('\n')
chunksize = 1
bytebuffer = ''
while success: 
  for y in range(height // chunksize**1):
    for x in range(width // chunksize**1):
        sume = 0;
        for xe in range(chunksize):
            for ye in range(chunksize):
                sume += int(image[y*chunksize**1+ye][x*chunksize**1+xe][0])

        if (sume/chunksize**2 > 128.0):
            bytebuffer+='1'
              
        else:
            bytebuffer+='0'
          
        if len(bytebuffer) >= 8:

            #print("appended " + str(int(bytebuffer,2)))
            #bytestowrite.append(int(bytebuffer,2))
            file.write(int(bytebuffer,2).to_bytes(1,'big'))
            bytebuffer = ''

  print('FRAME ' + str(count) + ' IS DONE')
  success,image = vidcap.read()
  count += 1
while len(bytebuffer)%8 != 0:
    bytebuffer+='0'
if len(bytebuffer) == 8:
    file.write(int(bytebuffer,2).to_bytes(1,byteorder='big'))

print("FINISHED")