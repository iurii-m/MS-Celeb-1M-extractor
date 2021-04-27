# One more implementation of MS-Celeb-1M extractor.

For some reasons many of available implementations for extracting and cleaning MS-Celeb-1M dataset didnt work out of the box for me. So I decided to combine one more implementation and keep it as minimalistic as possible. 

This is a 3-steps process:

1. The dataset may be downloaded with torrents from [here](https://academictorrents.com/details/9e67eb7cc23c9417f39778a8e06cca5e26196a97) and [here](https://hyper.ai/datasets/5543) (April 2021):


2. To extract the dataset images clone this repository and execute in the console:
```sh
cd [PATH/TO/THIS/REPOSITORY]
```
```sh
python extract.py -edp [PATH/TO/EXTRACTED/DATASET] -tfp [PATH/TO/TSV/FILE/FaceImageCroppedWithOutAlignment.tsv]
```
3. The original dataset is rather noisy. There are several implementations for cleaning the dataset. Many thanks to [EB-Dodo](https://github.com/EB-Dodo) for [C-MS-Celeb](https://github.com/EB-Dodo/C-MS-Celeb) which is used here.
Copy files and   from [C-MS-Celeb](https://github.com/EB-Dodo/C-MS-Celeb) and put them to the root of this repository. 
The copy of these files is [here](https://drive.google.com/drive/folders/1aOR-F9cse3ESY3OsGpulI_b3NMzCAZA4?usp=sharing)
Then execute:

```sh
python c-ms-celeb.py -ms [PATH/TO/EXTRACTED/DATASET] -clms [PATH/TO/CLEANED/DATASET] 
```
requirements:
Python 3.x (3.7.9 was used)

