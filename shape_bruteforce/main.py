import argparse
import shape_bruteforce as sb


def main():
    """Entrypoint of application"""
    version = sb.utils.get_version()
    parser = argparse.ArgumentParser(description=f"Shape Bruteforce CLI v{version}")
    parser.add_argument("image", type=str, help="Image to be processed")
    args = parser.parse_args()

    target = sb.utils.load_image(args.image)


if __name__ == "__main__":
    main()
