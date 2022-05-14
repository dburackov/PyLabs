import argparse
import re
import sys

from console_utility import console_handler

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="serialization-deserialization console utility")
    parser.add_argument("-source_filename", dest="source_filename", type=str)
    parser.add_argument("-output_filename", dest="output_filename", type=str)
    parser.add_argument("-source_type", dest="source_type", type=str)
    parser.add_argument("-output_type", dest="output_type", type=str)
    parser.add_argument("-config_file", dest="config_file_name", type=str)

    args = parser.parse_args()

    source_filename = None
    output_filename = None
    source_type = None
    output_type = None

    if args.config_file_name is not None:
        try:
            config_file_name = re.search(r"(.+)\.py$", args.config_file_name).group(1)
            module = __import__(config_file_name)

            if hasattr(module, "source_filename"):
                source_filename = module.source_filename

            if hasattr(module, "output_filename"):
                output_filename = module.output_filename

            if hasattr(module, "source_type"):
                source_type = module.source_type

            if hasattr(module, "output_type"):
                output_type = module.output_type

        except ModuleNotFoundError as e:
            print(f"can't open file because {e.msg}. Be aware, file should be .py")

    if args.source_filename is not None:
        source_filename = args.source_filename

    if args.output_filename is not None:
        output_filename = args.output_filename

    if args.source_type is not None:
        source_type = args.source_type

    if args.output_type is not None:
        output_type = args.output_type

    broken = False
    if source_filename is None:
        broken = True
        print("No source file")

    if output_filename is None:
        broken = True
        print("No output file")

    if source_type is None:
        broken = True
        print("No source type")

    if output_type is None:
        broken = True
        print("No output type")

    if broken:
        sys.exit()

    console_handler.handler(source_filename, output_filename, source_type, output_type)