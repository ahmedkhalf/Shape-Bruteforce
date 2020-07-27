import argparse
from shape_bruteforce import utils


def main():
    """Entrypoint of application"""
    version = utils.get_version()
    parser = argparse.ArgumentParser(description=f"Shape Bruteforce CLI v{version}")
    parser.add_argument("image", type=str, help="Image to be processed")
    args = parser.parse_args()

    img = utils.load_image(args.image)
    utils.show_image(img)


if __name__ == "__main__":
    main()
