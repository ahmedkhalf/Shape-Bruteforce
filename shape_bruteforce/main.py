import argparse
import shape_bruteforce as sb


def main():
    """Entrypoint of application"""
    version = sb.utils.get_version()
    parser = argparse.ArgumentParser(description=f"Shape Bruteforce CLI v{version}")
    parser.add_argument("image", type=str, help="Image to be processed")
    parser.add_argument("-s", "--size", default=128, type=int,
                        help="Max size of image to be processed, smaller = faster")
    args = parser.parse_args()

    target = sb.utils.load_image(args.image)
    target = sb.utils.resize_image(target, args.size)
    sb.utils.show_image(target)


if __name__ == "__main__":
    main()
