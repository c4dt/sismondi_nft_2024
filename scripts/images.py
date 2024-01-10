from PIL import Image
import io
import os
import base64
import itertools

image_dir = os.path.join(os.path.dirname(__file__), "..", "images")


def calc_min_dimensions(image_names):
    images = [Image.open(os.path.join(image_dir, image)) for image in image_names]
    min_width = min([image.width for image in images])
    min_height = min([image.height for image in images])
    return min_width, min_height


def create_composite_image(file_paths, width, height, output_width, index):
    # Load the images
    images = [Image.open(os.path.join(image_dir, fp)).convert("RGBA").resize((width, height)) for fp in file_paths]

    # Superimpose the images one over the other
    composite = Image.alpha_composite(Image.alpha_composite(images[0], images[1]), images[2])

    # Resize the image
    aspect_ratio = composite.height / composite.width
    new_height = int(output_width * aspect_ratio)
    resized_composite = composite.resize((output_width, new_height))
    results_dir = os.path.join(image_dir, "results")
    os.makedirs(results_dir, exist_ok=True)
    resized_composite.save(os.path.join(results_dir, f"composite_{index}.png"))

    # Convert the image to base64
    buffered = io.BytesIO()
    resized_composite.save(buffered, format="PNG")
    img_str_base64 = base64.b64encode(buffered.getvalue())

    return f"data:image/png;base64,{img_str_base64.decode()}"


def get_common(images):
    pre = os.path.commonprefix(images)
    remaining_parts = ['"' + s[len(pre):] for s in images]
    return pre + '"', remaining_parts


def get_image_strings(background_names, shoe_names, sole_names):
    image_names = list(itertools.chain.from_iterable([background_names, shoe_names, sole_names]))
    width, height = calc_min_dimensions(image_names)
    print(f"Resizing all images to width={width}, height={height}")
    # Uncomment the following lines to set the width and height to a given value
    # width = 320
    # height = 240

    # For-loop with all combinations of backgrounds / shoe / sole
    images_long = []
    index = 0
    for background in background_names:
        for shoe in shoe_names:
            for sole in sole_names:
                img_str = create_composite_image([background, shoe, sole], width, height, 30, index)
                images_long.append(f"\"{img_str}\"")
                index += 1

    return images_long


def write_contract(images_long):
    prefix, images_short = get_common(images_long)

    nft_parts_prefix = os.path.join(os.path.dirname(__file__), "SismondiNFT_")
    with open(os.path.join(image_dir, "..", "contracts", "SismondiNFT.sol"), "w") as nft:
        with open(f"{nft_parts_prefix}1.sol") as pre:
            nft.write(pre.read())

        nft.write(prefix)
        with open(f"{nft_parts_prefix}2.sol") as middle:
            nft.write(middle.read())

        nft.write(",\n".join(images_short))
        with open(f"{nft_parts_prefix}3.sol") as end:
            nft.write(end.read())

    print("../contracts/SismondiNFT.sol has been rewritten.")


# Example usage (replace 'file1.png', 'file2.png', 'file3.png' with actual file paths)
backgrounds = [
    "background/file1.png",
    "background/file2.png",
]
shoes = [
    "shoe/file1.png",
    "shoe/file2.png",
]
soles = [
    "sole/file1.png",
    "sole/file2.png",
]

write_contract(get_image_strings(backgrounds, shoes, soles))
