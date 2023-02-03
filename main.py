from src.video import Video

# reference to the video file to test
filename = "./videos/Participant_8_2021-06-01_13-10-42-741.avi"

# a variable to house the video taken by participant
participant_8 = Video(filename)

# convert the video to images
participant_8.to_image("./resources", "Participant 8")
