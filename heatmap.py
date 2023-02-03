import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


filename = "./data/Participant_17.csv"
eye_data = pd.read_csv(filename)

# Selecting specific columns needed for analysis
eye_data_imp_col = eye_data[
    ["gaze_projected_to_left_view_x", "gaze_projected_to_left_view_y"]
]
eye_data_imp_col.insert(0, "No.", range(0, 0 + len(eye_data_imp_col)))

eye_data_imp_col["No."] = eye_data_imp_col.loc[:, "No."].astype(str)


# selecting the 100th datapoint for drawing in image
eyeTrackingData = eye_data_imp_col.loc[
    eye_data_imp_col["No."].str.contains("\d00+$"),
    ("gaze_projected_to_left_view_x", "gaze_projected_to_left_view_y"),
].values.tolist()


# create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 14))


im = plt.imread("./resources/Participant 17/frame_0.jpg")
ax1.imshow(im)

heatmap, xedges, yedges = np.histogram2d(
    [i[0] for i in eyeTrackingData], [i[1] for i in eyeTrackingData], bins=50
)
implot = plt.imshow(im, origin="upper")
extent = [xedges[0], xedges[-1], yedges[-1], yedges[0]]
ax2.imshow(heatmap, extent=extent, alpha=0.4, origin="upper", interpolation="none")
fig.tight_layout()

fig.savefig("heatmap1.png", dpi=300)
