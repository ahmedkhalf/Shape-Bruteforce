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
    parser.add_argument("-s", "--size", default=64, type=int,
                        help="Max size of image during training, smaller = faster")
    parser.add_argument("-a", "--shapes", default=256, type=int, help="Number of shapes")
    parser.add_argument("-g", "--generations", default=2000, type=int, help="Generations per shape")
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
    target = sb.utils.normalize_image(target)
    trainer = sb.training.Training(target)
    trainer.train(shape_count=args.shapes, gens_per_shape=args.generations)

    result = trainer.parent.to_array()
    sb.utils.show_image(result)


if __name__ == "__main__":
    main()
