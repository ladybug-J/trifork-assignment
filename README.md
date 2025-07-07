# Trifork assignment
## Resize the images in given directory and their corresponding bounding box coordinates.

To run the code: clone the repository, install the dependencies, and run the main script "resize.py".

```
git clone https://github.com/ladybug-J/trifork-assignment.git
cd trifork-assignment
pip install -r requirements.txt
python resize.py
```
The resize function allows command line input arguments. The default values will use the paths in the repository, and the requested resize(284 284), and will generate the outputs in a directory named "output".
```
python resize.py --input_images <Path to image directory>
                 --input_annotations <Path to annotation directory>
                 --resize <Tuple indicating desired output width and height (width, height)>
                 --output_dir <Path to output directory that will be created. If it already exists, the script will exit>
```
