# SS
Protein secondary structure prediction based on attention model

Paper:Attention-based deep learning for accurate prediction of protein secondary structures

# Operating environment

The key library has been written in file `requirements.txt` You can use the following command to deploy the environment

```python
pip install -r requirements.txt
```

Note:Here the  tensorflow  uses a version with GPU acceleration. If you want to use this version, you need to additionally install the corresponding  acceleration library (such as NVIDIA's cudnn).



# Get data

(1) **Data from** [ICML2014](http://www.princeton.edu/~jzthree/datasets/ICML2014/), we need the file is  `cb513+profile_split1.npy.gz` and `cullpdb+profile_6133_filtered.npy.gz`

(2) **Data description** see the `dataset_readme.txt `under this connection



# Data preprocessing

(1)**Get Featrues:** Use script `1.Getfeatrue.ipynb` to get the properties of each amino acid and PSMM matrix features.

(2)**Sorting amino acids:** To quickly split the window behind, use the script `2.ChangeSort.py` to sort the amino acids according to the position of the original chain.

(3)**Sliding window:**  Sliding window extraction feature for each chain using script `3.SliWind.ipynb`

(4)**Split Data:** Use script `4.SplitData.ipynb` to normalize the characteristics of each window and extract the verification data by 10%



Note: The file `AaminoAcid` is a table of amino acid properties. You can find it from [wiki](https://en.wikipedia.org/wiki/Amino_acid) .



# Loading model

The  compressed package **xx** is a model we have trained. When loading the  model, you need to copy the file AttentionDecoder.py to ` /usr/local/lib/python3.5/dist-packages/keras/layers` and then add the following code to the `__init__.py` file in this directory.

```python
from .AttentionDecoder import AttentionDecoder
```

Finally use the following python code to load the model.

```python
from keras.models import load_model

model=load_model('xxx.hdf5')  #Xxx.hdf5 file saves the model (including model structure and weights)
```
