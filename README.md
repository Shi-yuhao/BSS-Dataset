# BSS-Dataset
the dataset of BSS

We have provided two CSV data files. Through code processing, the original data of SDSS can be downloaded from the CSV files (we have provided an example, such as: BSS-Dataset/sdss_detect/1_301_6850_3_37) and processed into our two datasets. The following is the processing procedure:

1、Use detect_sdss.py and dataset-0.06.csv, dataset-0.1.csv to download the original data

2、Modify the configuration in fits_config.py. To_annotation.py will process the original data into a txt file and generate a black-and-white image. It also annotates the position of the target star with horizontal lines, vertical lines and boxes.

3、Divide the txt file into train_annotation.txt, valid_annotation.txt and test_annotation.txt according to the ratio of train:valid:test = 7:1:2.

4、According to the ratio of train:valid:test = 7:1:2, the txt file is split into train.txt, valid.txt and test.txt. Based on the modified configuration in fits_config.py and the txt file, the train_dataset_generator.py will generate the final data after random cropping and also create npy, xml and other files.

# Data
<pre>  ├── dataset 
  
  │ ├── VOCdevkit 
  
  │ │ ├── VOC2007 
  
  │ │ │ ├── Annotations 
  
  │ │ │ │ ├── annotation_1.xml 
  
  │ │ │ │ ├── annotation_2.xml 
  
  │ │ │ │ └── ... 
  
  │ │ │ ├── ImageSets 
  
  │ │ │ │ └── Main 
  
  │ │ │ │ ├── train.txt 
  
  │ │ │ │ ├── valid.txt 
  
  │ │ │ │ └── test.txt 
  
  │ │ │ ├── JPEGImages 
  
  │ │ │ │ ├── dataset_image_1.npy 
  
  │ │ │ │ ├── dataset_image_2.npy 
  
  │ │ │ │ └── ... 
  
  │ ├── train_annotation.txt 
  
  │ ├── valid_annotation.txt 
  
  │ └── test_annotation.txt  </pre>
