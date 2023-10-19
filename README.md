# hair-follicle-detection
This project is the construction of an AutoEncoder-based machine learning model for the detection and calculation of hair area in the photo of the patient's scalp. The result can be a quantifiable indicator for surgeon performing hair follicle transplantation. 
1. This project has three sessions: first, the images from patients are processed and they constitute the training dataset and validation dataset; second, the model based on CNN and AutoEncoder is constructed and trained; third, the test photo is processed and input into the model.
2. The three branches (except main branch) contain the program for the three sessions in this project respectively. And the branches have been merged to main branch.
3. 'dataset.zip' includes the training dataset and validation set.
4. 'se_seg_hairfollicle.h5' is the model after training.
5.  To predict a photo, you need to create a directory 'PUT PHOTO HERE' under the project directory and put the photo in this directory.
6.  The result of prediction will show up in the directory 'result'.
