The motion_capture is the detector of motion infont yor web camera. 

Motion Detector use computer vision technology, via python library CV2. 
In the first moment of program run, the original frame is saved as a background for motion, therefore the first appearance will be considered
as stable background and motion will be detected outside of this frame. 

The motion calculator: The times of motion are calculated and saved to dataframe via Pandas library, as start + end time and saved to the csv file. 
