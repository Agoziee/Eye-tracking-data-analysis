import os
import cv2
import math


class Video:
    """Handles operations and processing of video files

    Parameters
    -----------
    filename: str
        Receives the path to the video file
    """

    def __init__(self, filename: str):
        self.filename = filename

    def __str__(self):
        return "Video: %s" % self.filename

    def __repr__(self):
        return "Video(filename='%s')" % self.filename

    def to_image(self, resources_folder: str, tag: str, verbose=True):
        """Converts the video to a sequence of images
        
        Parameters:
        ----------
        resources_folder: str
            The path to the resource folder
        
        tag: str
            The name of the folder to house the sequence of images
            
        verbose: bool
            Prints out additional message during execution. defaults to True
        """ ""
        count = 0
        storage_folder = resources_folder + "/" + tag

        if verbose:
            print("Ensuring the resources folder exists")
            if not os.path.exists(storage_folder):
                os.mkdir(storage_folder)

        capture = cv2.VideoCapture(self.filename)
        frame_rate = capture.get(5)

        if verbose:
            print("Processing videos to images")

        while capture.isOpened():
            frame_id = capture.get(1)
            ret, frame = capture.read()
            if ret != True:
                break
            if frame_id % math.floor(frame_rate) == 0:
                filename = storage_folder + "/" + f"frame_{count}.jpg"
                count += 1
                cv2.imwrite(filename, frame)
        capture.release()
        print("The images are now available in the resources folder")
