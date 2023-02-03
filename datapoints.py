import pandas as pd
eye_data = pd.read_csv("Participant_17_data 22-06-21.csv")

# Selecting specific columns needed for analysis
eye_data_imp_col = eye_data[['gaze_projected_to_left_view_x', 'gaze_projected_to_left_view_y']]
eye_data_imp_col.insert(0, 'No.', range(0, 0 + len(eye_data_imp_col)))

eye_data_imp_col['No.'] = eye_data_imp_col.loc[:, "No."].astype(str)

# mg_eye_data["Pupil Diameter Left (mm)"] = mg_eye_data.loc[:, "Pupil Diameter Left (mm)"]*10
eyeTrackingData = eye_data_imp_col.loc[eye_data_imp_col['No.'].str.contains("\d00+$"), ('gaze_projected_to_left_view_x', 'gaze_projected_to_left_view_y')].values.tolist()
