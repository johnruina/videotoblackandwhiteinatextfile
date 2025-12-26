
import cv2
vidcap = cv2.VideoCapture('badapple.mp4')
success,image = vidcap.read()
count = 0

writetofile = "videostuff.txt"
with open(writetofile, 'w') as f:
    pass 
file = open(writetofile,'a');

height = len(image)
width = len(image[0])

file.write(str(height) + ' ' + str(width))
while success: 
  framedata = ''
  for y in range(height//4):
      for x in range(width//4):
          rgb0 = int(image[y*4][x*4][0]) + int(image[y*4][x*4][1]) + int(image[y*4][x*4][2])
          rgb1 = int(image[y*4][x*4+1][0]) + int(image[y*4][x*4+1][1]) + int(image[y*4][x*4+1][2])
          rgb2 = int(image[y*4+1][x*4][0]) + int(image[y*4+1][x*4][1]) + int(image[y*4+1][x*4][2])
          rgb3 = int(image[y*4+1][x*4+1][0]) + int(image[y*4+1][x*4+1][1]) + int(image[y*4+1][x*4+1][2])
          if ((rgb0+rgb1+rgb2+rgb3)/12.0 > 127.0):
              framedata+='1'
          else:
              framedata+='0'
  print('FRAME ' + str(count) + ' IS DONE')
  file.write('\n')
  file.write(framedata);
 
  success,image = vidcap.read()
  count += 1
print("FINISHED")