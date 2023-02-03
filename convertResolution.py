from PIL import Image, ImageDraw
import os as os
import pandas as pd


filename = ("Participant_17_data 22-06-21.csv")
eye_data = pd.read_csv(filename)

# Selecting specific columns needed for analysis
eye_data_imp_col = eye_data[['gaze_projected_to_left_view_x', 'gaze_projected_to_left_view_y']]
eye_data_imp_col.insert(0, 'No.', range(0, 0 + len(eye_data_imp_col)))

eye_data_imp_col['No.'] = eye_data_imp_col.loc[:, "No."].astype(str)


# selecting the 100th datapoint for drawing in image
eyeTrackingData = eye_data_imp_col.loc[eye_data_imp_col['No.'].str.contains("\d00+$"), ('gaze_projected_to_left_view_x', 'gaze_projected_to_left_view_y')].values.tolist()

# eyeTrackingData = [
#     [0,0],
#     [0.8,0.2],
#     [0.14209,0.023498],
#     [0.170687,0.033833],
#     [0.549907,0.06477],
#     [0.168999,0.018419],
#     [0.066252,0.310836]
# ]

'''

0.14209,0.023498],
0.170687,0.033833],
0.549907,0.06477],
0.168999,0.018419],
0.066252,0.310836]

'''

xResLeft = 0
xResRight = 1391
yResTop = 0
yResBottom = 1600

xNormLeft = -1
xNormRight = 1
yNormTop = 1
yNormBottom = -1

imgNumber = 0

def convertFromNormToRes(xVal, yVal):
    # what is one pixel in normalized space?
    width = xNormRight + (0 - xNormLeft)
    height= yNormTop + (0 - yNormBottom)

    xPixel = width / (xResRight + (0-xResLeft))
    yPixel = height / (yResBottom + (0-yResTop))
    
    xResult = ((xVal + (0 - xNormLeft)) / xPixel) 
    yResult = yResBottom / (yNormTop - yNormBottom) - (yVal / yPixel) 
    print("%f , %f" % (xResult, yResult))
    return [xResult - 10, yResult - 10, xResult+ 10, yResult+10]


def drawInImage(filename, xVal, yVal):
    #global imgNumber
    try: 
         img  = Image.open('C:\\Users\\igbud\\thesis\\Scripts\\input_images\\'+filename) 
         draw = ImageDraw.Draw(img)
         #draw.line((0, 0) + img.size, fill=128)
         #draw.line((0, img.size[1], img.size[0], 0), fill=128)
         res = convertFromNormToRes(xVal, yVal)
         #draw.point(res, fill=128)
         draw.ellipse(res, outline = 128, width = 2)
         #convertFromNormToRes(xVal, yVal)
        #  img.save('C:\\Users\\igbud\\thesis\\Scripts\\out_images\\%4i.jpg' % (imgNumber))
         img.save('C:\\Users\\igbud\\thesis\\Scripts\\out_images\\new'+filename)
         #imgNumber += 1
    except IOError:
         print('IO Error')
         pass

def navigateThroughFiles():
    s = os.listdir('C:\\Users\\igbud\\thesis\\Scripts\\input_images')
    counter = 0
    for f in s: # go through each entry
        print(f)
        drawInImage(f, eyeTrackingData[counter][0], eyeTrackingData[counter][1])
        counter += 1


navigateThroughFiles()

# dummy output
'''
convertFromNormToRes(0.8, 0.2) # 556,4+1391/2 ; 800-160
convertFromNormToRes(1, 1) # 1391, 0
convertFromNormToRes(0, 0) # 1391/2, 800
convertFromNormToRes(-1, -1) # 0, 1600
convertFromNormToRes(1, -1) # 1391, 1600
convertFromNormToRes(-1, 1) # 0, 0
'''

# test images 
#drawInImage('C:\Users\igbud\thesis\Scripts\\frame_31.jpg', 0, 0)
# print (eyeTrackingData[0])
# convertFromNormToRes(0.8, 0.2)
# counter = 0
