import os
from PIL import Image

def resize_file(filename,
                width=284,
                height=284,
                input_images="./images/",
                input_annot="./kitti_annotations/",
                plot=True,
                output_dir="./resized"
                ):
    """
    Given a filename, path to images and annotations, and output width and height, return a resized image and annotation
    """
    # with Image.open(os.path.join(input_images, filename)) as img:
    img = Image.open(os.path.join(input_images, filename))
    scaled_img = img.resize((width, height), resample=Image.BILINEAR)
    # Save in given output dir:
    scaled_img.save(os.path.join(output_dir, f"images/{filename}"), exist_ok=True)

    # Scaling for bbox:
    original_w, original_h = img.size
    scale_w, scale_h = width / original_w, height / original_h

    annotation_filename = filename.replace(".jpg", ".txt")

    scaled_rectangles = []

    with open(os.path.join(input_annot, annotation_filename), 'r') as file:
        # Read .txt annotation file: format <object_type> <truncation> <occlusion> <alpha> <left> <top> <right> <bottom> <height> <width> <length> <x> <y> <z> <rotation_y>
        lines = file.readlines()
    # Extract and scale bounding box coordinates in image, and write in new .txt file
    with open(os.path.join(output_dir, f"annotations/{annotation_filename}"), 'w') as f:
        for line in lines:
            str_vec = line.split(" ")
            # Elements from 4:7 replaced with their scaled value
            str_vec[4] = str(float(str_vec[4]) * scale_w)
            str_vec[5] = str(float(str_vec[5]) * scale_h)
            str_vec[6] = str(float(str_vec[6]) * scale_w)
            str_vec[7] = str(float(str_vec[7]) * scale_h)
            # Write the joint scaled str
            f.write(" ".join(str_vec))


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="Rezize images and annotations in a given directory")

    parser.add_argument('--input_images',
                        type=str,
                        help="Path to image directory",
                        default="./images/"
                        )
    parser.add_argument('--input_annotations',
                        type=str,
                        help="Path to annotations directory, KITTI format and .txt",
                        default="./kitti_annotations/"
                        )
    parser.add_argument('--resize',
                        type=tuple,
                        help="Width and height for the resizing. E.g: (284, 284)",
                        default=(284, 284)
                        )
    parser.add_argument('--output_dir',
                        type=str,
                        help="Name for the output directory",
                        default="./output/"
                        )
    args = parser.parse_args()

    try:
        os.makedirs(os.path.join(args.output_dir, "images"))
        os.makedirs(os.path.join(args.output_dir, "annotations"))
    except:
        print("Output directories already exist")

    image_list = os.listdir(args.input_images)

    for filename in image_list:
        resize_file(
            filename,
            width=args.resize[0],
            height=args.resize[1],
            input_images=args.input_images,
            input_annot=args.input_annotations,
            output_dir=args.output_dir
        )