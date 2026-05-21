# Information
In order to train a model, you need to have a .pt-file for the model weights in the same folder as the script

This can be downloaded from: [Ultralytics](https://docs.ultralytics.com/models/yolo11) or any of the weights folders found in this [repository](https://github.com/KristianJon/MachineLearningPipelineForMasterThesis/tree/main/ResultsFromYOLOModels)

# How to run
It is advised to have Anaconda downloaded and then use load a custom environment provided by either of the two .yml-files found in this folder. A custom environment can be loaded by the command

	conda env create -f your_file_name.yml

Insert either the file "modelTrainingForCPU" or "modelTrainingForGPU" based on your preferance. Training can then be started with the following command after you activated the custom environment:

	python trainModelOnAnnotations.py
