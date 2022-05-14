from parsers import ParserFactory


def handler(source_filename, output_filename, source_type, output_type):
    if source_type == output_type:
        raise ValueError(f"Source type is output type {source_type}, use different types")

    source_sd = ParserFactory.create_parser(source_type)
    output_sd = ParserFactory.create_parser(output_type)

    with open(source_filename, "r") as f:
        source = source_sd.load(f)

    with open(output_filename, "w") as f:
        output_sd.dump(source, f)