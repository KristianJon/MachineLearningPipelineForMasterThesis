# Overview of folder and its structure
This folder contains four subfolders:

1. DataPreprocessing
	- Contains one Python script ("FetchTilesAndConvertFromGeoJSONToYOLO") that fetches all the patches from a WSI that contains annotations and converts from .geoJSON-formet to YOLO-format for the annotations

2. ResultsFromYOLOModels
	- This folder further consists of three new folders ("YOLOv10", "YOLOv11", "YOLOv12") that contains the results obtained from model training through Ultralytics. 
	- Each of the previously mentioned folders contains results from the different patch sizes (320x320, 640x640, 1280x1280)
	- The model weights can be found in the folder called "weights", both .pt and .torchscript models are available (.torchscript models are required for the developed QuPath-extension)

3. StatisticalBootstrappingAndTTest
	- Contains in total 8 files and 1 folder:
		- "Dataset" -> "labels" -> "test"
			- This folder contains all the ground truth annotation labels and is included so that the bootstrapping code can be executed properly 

		- "bootstrapResults.json"
			- All metrics for every bootstrap iteration is saved to this json-file and grouped under the three models ("YOLOv10nData", "YOLOv11nData", "YOLOv12nData")
			- This file is used when performing the t-test

		- "PathsFromANON7TDVLK188_1_6.csv"
			- Contains file paths to the annotation labels

		- "PathsFromANONAVDVLK13R_1_4.csv"
			- Contains file paths to the annotation labels

		- "PerformStatisticalBoostrap.ipynb"
			- Jupyter Source file used to perform bootstrapping and calculate metrics such as precision, recall, ap50-95 etc for each bootstrap iteration
			- The results, i.e. collection of all metrics for all iterations, are stored in the .json-file called "bootstrapResults.json"

		- "predictions_YOLOv10n.json"
			- A .json-file that contains all predictions made by the YOLOv10-model on the static dataset
			- This file is used during bootstrapping

		- "predictions_YOLOv11n.json"
			- A .json-file that contains all predictions made by the YOLOv11-model on the static dataset 
			- This file is used during bootstrapping

		- "predictions_YOLOv12n.json"
			- A .json-file that contains all predictions made by the YOLOv12-model on the static dataset
			- This file is used during bootstrapping

		- "TTestOnBootstrappedData.ipynb"
			- Python code used to perform t-test based on the bootstrapped data saved in the file "bootstrapResults.json"


5. TrainingYOLOModel
	- This folder contains only one file ("trainModelOnAnnotations.py") and it has been used to load a .pt-file and then perform training based on the parameters defined
	- After training the model, the output and results will be saved and can be viewed for each model under the folders described in "2. ResultsFromYOLOModels"

# How to run the files

1. The files ".ipynb" should be opened With jupyter notebook and the cells should be executed sequentially
   
2. The Python scripts are best executed by creating a special anaconda environment, activating it and then calling "python filename.py"
