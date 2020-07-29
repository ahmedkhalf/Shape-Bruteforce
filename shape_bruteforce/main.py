import argparse
import shape_bruteforce as sb


def egg():
    print("""
        ████
      ██░░░░██
    ██░░░░░░░░██
    ██░░░░░░░░██
  ██░░░░░░░░░░░░██  Congratulations!
  ██░░░░░░░░░░░░██  You are one of the few people who read my code.
  ██░░░░░░░░░░░░██  Here is an egg.
    ██░░░░░░░░██
      ████████
    """)


def main():
    """Entrypoint of application"""
    version = sb.utils.get_version()
    parser = argparse.ArgumentParser(description=f"Shape Bruteforce CLI v{version}")
    parser.add_argument("image", type=str, nargs='?', default="", help="Image to be processed")
    parser.add_argument("-s", "--size", default=128, type=int,
                        help="Max size of image to be processed, smaller = faster")
    parser.add_argument("--egg", action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.egg:
        egg()
        return

    if args.image == "":
        parser.print_help()
        return

    target = sb.utils.load_image(args.image)
    target = sb.utils.resize_image(target, args.size)
    sb.utils.show_image(target)


if __name__ == "__main__":
    main()
