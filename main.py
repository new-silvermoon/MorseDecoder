import cv2
import numpy as np
from morselogic import MorseDecoder
import threading

path = "/Users/stephanie/PycharmProjects/MorseDecoder/data/morse_vid2.mp4"
def readFromFile():

    """

    :return:
    """

    #region Variables
    light_times = []
    dark_times = []
    dark_times_count = light_times_count = 0
    #threshold variable
    min_error_tol, med_error_tol, max_error_tol = 4,4,4
    light_min_thresh = 11
    light_max_thresh = light_min_thresh * 3
    dark_min_thresh = 1
    dark_med_thresh = 15 #(min_thresh * 3)
    dark_max_thresh = 51 #(min_thresh * 7
    symbol_list = []

    #endregion

    """Reading from video"""

    vid_cap = cv2.VideoCapture(path)
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    print("fps " + str(int(fps)))
    read_flag = True
    while (read_flag):
        #img = np.array(cv2.imread(path))
        read_flag,img = vid_cap.read()

        if not read_flag:
            break
        #print(img.shape)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        """Blurring image to reduce noise"""
        img_blur_gray = cv2.GaussianBlur(img_gray,(11,11),0)

        """Converting  to binary image"""
        ret,bin_img = cv2.threshold(img_blur_gray,200,255,cv2.THRESH_BINARY)

        """Performing dilation and erosion to enhance quality of image"""
        bin_img = cv2.erode(bin_img, None, iterations=2)
        bin_img = cv2.dilate(bin_img, None, iterations=4)

        bin_img_arr = np.array(bin_img)
        source_light_cord = []

        """Saving coordinates for light object"""
        for i,row in enumerate(bin_img_arr):
            for j,col in enumerate(row):
                if col ==255:
                    source_light_cord.append([i,j])



        """Finding the midpoint of the light source"""
        if len(source_light_cord) > 0:
            if dark_times_count > 0:
                #print("dark times" + str(dark_times_count))
                dark_times.append(dark_times_count)
                if dark_times_count in range(dark_med_thresh,dark_med_thresh+med_error_tol):
                    print("Medium")
                    threading.Thread(target=decodeMorse,args=(symbol_list,)).start()
                    symbol_list = []
                elif dark_times_count in range(dark_max_thresh,dark_max_thresh-max_error_tol):
                    print("Max")
                    threading.Thread(target=decodeMorse,args=(" ",)).start()
                    symbol_list = []
            dark_times_count=0
            light_times_count+=1
            top,left = source_light_cord[0][0],source_light_cord[0][1]
            bottom,right = source_light_cord[len(source_light_cord)-1][0],source_light_cord[len(source_light_cord)-1][1]

            arr2D = np.array([[11, 12],
                                 [14, 15],
                                 [17, 15],
                                 [12, 14]])
            max_y, max_x = np.amax(source_light_cord,axis=0)

            midx,midy = int((left + max_x) /2), int((top + max_y) / 2)

            cv2.circle(img, (source_light_cord[0][1],source_light_cord[0][0]), 5, (255, 0, 0))
            cv2.circle(img, (max_x,max_y), 5, (255, 0, 0))
            cv2.circle(img,(midx,midy),5,(0,255,0))
        else:
            if light_times_count > 0:
                #print("light time"+str(light_times_count))
                light_times.append(light_times_count)
                symbol = '.' if light_times_count in range(light_min_thresh,light_min_thresh+min_error_tol) else "_"
                symbol_list.append(symbol)
            light_times_count = 0
            dark_times_count += 1

        #displaying the frames

        # cv2.imshow("hello", img)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
    
    vid_cap.release()
    print("Light times")
    print(light_times)
    print("Dark times")
    #Excluding the dark time before the sequence begins
    dark_times.pop(0)
    print(dark_times)


def readFromLiveFeed():
    """

    :return:
    """

    # region Variables
    light_times = []
    dark_times = []
    dark_times_count = light_times_count = 0
    # threshold variable
    min_error_tol, med_error_tol, max_error_tol = 4, 4, 4
    light_min_thresh = 11
    light_max_thresh = light_min_thresh * 3
    dark_min_thresh = 1
    dark_med_thresh = 15  # (min_thresh * 3)
    dark_max_thresh = 51  # (min_thresh * 7
    symbol_list = []

    # endregion

    """Reading from video"""

    vid_cap = cv2.VideoCapture(path)
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    print("fps " + str(int(fps)))
    read_flag = True
    while (read_flag):
        # img = np.array(cv2.imread(path))
        read_flag, img = vid_cap.read()

        if not read_flag:
            # Looping the over video infinitely
            vid_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            print("loop")
            read_flag = True
            continue
        # print(img.shape)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        """Blurring image to reduce noise"""
        img_blur_gray = cv2.GaussianBlur(img_gray, (11, 11), 0)

        """Converting  to binary image"""
        ret, bin_img = cv2.threshold(img_blur_gray, 200, 255, cv2.THRESH_BINARY)

        """Performing dilation and erosion to enhance quality of image"""
        bin_img = cv2.erode(bin_img, None, iterations=2)
        bin_img = cv2.dilate(bin_img, None, iterations=4)

        bin_img_arr = np.array(bin_img)
        source_light_cord = []

        """Saving coordinates for light object"""
        for i, row in enumerate(bin_img_arr):
            for j, col in enumerate(row):
                if col == 255:
                    source_light_cord.append([i, j])

        """Finding the midpoint of the light source"""
        if len(source_light_cord) > 0:
            if dark_times_count > 0:
                # print("dark times" + str(dark_times_count))
                dark_times.append(dark_times_count)
                if dark_times_count in range(dark_med_thresh, dark_med_thresh + med_error_tol):
                    print("Medium")
                    threading.Thread(target=decodeMorse, args=(symbol_list,)).start()
                    symbol_list = []
                elif dark_times_count in range(dark_max_thresh, dark_max_thresh - max_error_tol):
                    print("Max")
                    threading.Thread(target=decodeMorse, args=(" ",)).start()
                    symbol_list = []
            dark_times_count = 0
            light_times_count += 1
            top, left = source_light_cord[0][0], source_light_cord[0][1]
            bottom, right = source_light_cord[len(source_light_cord) - 1][0], \
                            source_light_cord[len(source_light_cord) - 1][1]

            arr2D = np.array([[11, 12],
                              [14, 15],
                              [17, 15],
                              [12, 14]])
            max_y, max_x = np.amax(source_light_cord, axis=0)

            midx, midy = int((left + max_x) / 2), int((top + max_y) / 2)

            cv2.circle(img, (source_light_cord[0][1], source_light_cord[0][0]), 5, (255, 0, 0))
            cv2.circle(img, (max_x, max_y), 5, (255, 0, 0))
            cv2.circle(img, (midx, midy), 5, (0, 255, 0))
        else:
            if light_times_count > 0:
                # print("light time"+str(light_times_count))
                light_times.append(light_times_count)
                symbol = '.' if light_times_count in range(light_min_thresh, light_min_thresh + min_error_tol) else "_"
                symbol_list.append(symbol)
            light_times_count = 0
            dark_times_count += 1

        # displaying the frames

        # cv2.imshow("hello", img)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    vid_cap.release()
    print("Light times")
    print(light_times)
    print("Dark times")
    # Excluding the dark time before the sequence begins
    dark_times.pop(0)
    print(dark_times)




def decodeMorse(symbolList):
    morse = MorseDecoder()
    print(symbolList)
    val = " " if symbolList == " " else morse.decodeSymbol(symbolList)
    print(val,sep="")




readFromFile()