# Starting Code Kit for the EPIC-KITCHENS TREK-150 Object Tracking Challenge
This repository shows how to run the LTMU-H tracker to obtain results that can be submitted to the Object Tracking [CodaLab challenge]().

The code presented here can be taken as baseline to implement and run your solution. The results to submit are obtained through the [TREK-150-toolkit](https://github.com/matteo-dunnhofer/TREK-150-toolkit/). To exploit the toolkit to obtain the results, all you need to do is to make your tracker inherit the class [```Tracker```](https://github.com/matteo-dunnhofer/TREK-150-toolkit/blob/main/toolkit/trackers/__init__.py) and override the [```init(self, image, box):```](https://github.com/matteo-dunnhofer/TREK-150-toolkit/blob/d774b5842471c103d9b3e04b38d4f31b5c4150ec/toolkit/trackers/__init__.py#L16) and [```update(self, image):```](https://github.com/matteo-dunnhofer/TREK-150-toolkit/blob/d774b5842471c103d9b3e04b38d4f31b5c4150ec/toolkit/trackers/__init__.py#L19) methods.


## Challenge Organizers
Matteo Dunnhofer (1)
Antonino Furnari (2)
Giovanni Maria Farinella (2)
Christian Micheloni (1)

* (1) Machine Learning and Perception Lab, University of Udine, Italy
* (2) Image Processing Laboratory, University of Catania, Italy

**Contact:** [matteo.dunnhofer@uniud.it](mailto:matteo.dunnhofer@uniud.it)


## Instructions to run the LTMU-H tracker

The following instructions demonstrate how to run the LTMU-H tracker defined in our IJCV paper.


### Download and install LTMU-H

1. Download this [repository](https://github.com/matteo-dunnhofer/fpv-tracking-baselines)
   
    ```
    git clone https://github.com/matteo-dunnhofer/fpv-tracking-baselines
    cd fpv-tracking-baselines/LTMU-H
    ```

2. Create the Conda environment and install the dependecies
   
    ```
    conda env create -f environment.yml
    pip install -f requirements.txt
    conda activate ltmuh
    ```

3. Download the [Hands-in-Contact repository](https://github.com/ddshan/hand_object_detector)
   
    ```
    git clone https://github.com/ddshan/hand_object_detector.git
    ```
    Download the [pretrained model for egocentric data](https://drive.google.com/open?id=1H2tWsZkS7tDF8q1-jdjx6V9XrK25EDbE) an put into a ```hand_object_detector/models/res101_handobj_100K/pascal_voc``` folder.

4. Download the [LTMU repository](https://github.com/Daikenan/LTMU)
    ```
    git clone https://github.com/Daikenan/LTMU.git
    ```
    Set ```base_path = './LTMU' ``` in the ```LTMU/DiMP_LTMU``` folder.

5. Download the [STARK repository](https://github.com/researchmm/Stark)

    ```
    git clone https://github.com/researchmm/Stark.git
    ```
    Then run 
    ```
    python Stark/tracking/create_default_local_file.py --workspace_dir Stark/ --data_dir Stark/data --save_dir Stark/
    ```
    Download the [baseline pretrained model](https://drive.google.com/drive/folders/1fSgll53ZnVKeUn22W37Nijk-b9LGhMdN?usp=sharing) an put into a ```Stark/checkpoints/train/stark_st2``` folder.


### Download the TREK-150 dataset

1. Install the TREK-150 toolkit. Then, the full TREK-150 dataset can be built just by running
    ```
    pip install got10k
    git clone https://github.com/matteo-dunnhofer/TREK-150-toolkit
    cd TREK-150-toolkit
    python download.py
    ```


### Run the tracker on the TREK-150 dataset

1. Yuo can run the LTMU-H tracker on TREK-150 by running the following command. The tracker will be run using the OPE, MSE, and HOI evaluation protocols.
    ```
    cd ..
    python evaluate_trek150_for_challenge.py
    ```

If you want to run your tracker, you have to make sure it inherits the class ```Tracker``` defined in [```Tracker```](https://github.com/matteo-dunnhofer/TREK-150-toolkit/blob/main/toolkit/trackers/__init__.py) and you have to override the [```init(self, image, box):```](https://github.com/matteo-dunnhofer/TREK-150-toolkit/blob/d774b5842471c103d9b3e04b38d4f31b5c4150ec/toolkit/trackers/__init__.py#L16) and [```update(self, image):```](https://github.com/matteo-dunnhofer/TREK-150-toolkit/blob/d774b5842471c103d9b3e04b38d4f31b5c4150ec/toolkit/trackers/__init__.py#L19) methods. The first is used to initialize the tracker in the first frame of the suquence, the second to get the tracker's predicted bounding-box in the other frames.


### Prepare the results for the challenge

1. After having obained the results for each of the experimental protocols, you can create a zip file containing the valid JSON for the submission by running the following command

    Run the evaluation on TREK-150 by running the following command.
    ```
    python export_trek150_results_for_challenge.py
    ```

## Implement and test your tracker
The exemplar scripts to implement your tracker according the toolkit and to run the experiments are given in the files
```
tracker.py
evaluate_trek150_for_challenge.py
export_trek150_results_for_challenge.py
```
of this repository.


### Citing
When using the code, please reference:

```
@Article{TREK150ijcv,
author = {Dunnhofer, Matteo and Furnari, Antonino and Farinella, Giovanni Maria and Micheloni, Christian},
title = {Visual Object Tracking in First Person Vision},
journal = {International Journal of Computer Vision (IJCV)},
year = {2023}
}

@InProceedings{TREK150iccvw,
author = {Dunnhofer, Matteo and Furnari, Antonino and Farinella, Giovanni Maria and Micheloni, Christian},
title = {Is First Person Vision Challenging for Object Tracking?},
booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops},
month = {Oct},
year = {2021}
}
```
