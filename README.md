
# simimgs
simimgs is a python script that helps users to compare images and assign a similarity score based on SSIM. It takes a csv file that contains pairs of images and assigns a similarity score to each pair. Resuls are saved in an output csv file.

## Usage
Assumed python3 and pip3 have been installed. In a CLI(Linux, Mac or Windows), first get the package:
```
pip install simimgs==0.0.15
``` 
Then to run it:
```
 python -m simimgs in_csv_file_path out_csv_file_path
``` 

To get help text:
```
 python -m simimgs -h
``` 
To upgrade to the latest version on PyPi:
```
 pip install --upgrade simimgs
``` 
https://pypi.org/project/simimgs/

## Design Considerations and Approach
1. To have confidence that the code works, I set up a simple CI pipeline using Git Workflow that runs unit tests against every commit. The unit tests ensure that the script produces reasonable similarity scores and the correct output on correct or broken input files.
2. Bjorn used to assign similarity scores by comparing the colors shapes and other visual attributes. I used SSIM on multiple channels to mimic this approach. I think the more advanced way to do this is to use machine learning libraries and understand what's in each image.
3. Bjorn can find how to use this script in many places. For example, he can use the script's built-in `-h` flag, read the README on this GitHub page.
4. PyPi package will give Bjorn a quick and easy experience to get, run and update the script.
5. To make Ferris's life easier, The following things would help:
     * docstrings and type annotation on functions
     * unit tests and CI workflow to run unit tests on every commit
     * requirements.txt lists out what other libraries this script depends on
     * a release tag to mark a stable state of the script
 
