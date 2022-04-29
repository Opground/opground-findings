import argparse

from opground.name_generator.FunnyNameGenerator import FunnyNameGenerator, NameCategory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Funny name generator")
    parser.add_argument(
        "-c",
        "--category",
        choices=[str(category) for category in NameCategory],
        default=NameCategory.Elf,
        help="Category of names to generate",
    )
    parser.add_argument("-m", "--max", default=10, help="maximum number of names to generate")
    args = parser.parse_args()
    category = args.category
    max = args.max
    generator = FunnyNameGenerator()
    generated_names = generator.generate(category=category, max_number=max)
    print(f"GENERATED NAMES OF {category.upper()} CATEGORY")
    print(",".join(generated_names))
