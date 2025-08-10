import os
import re
from pathlib import Path


def merge_folder_to_wiki(docs_dir, output_dir):
    """Merge all .md files in numbered folders into combined wiki pages."""
    for folder in sorted(os.listdir(docs_dir)):
        if not re.match(r"^\d{2}", folder):  # Skip non-numbered folders
            continue

        wiki_name = re.sub(r"^\d{2}_", "", folder).replace("-", " ")
        output_file = Path(output_dir) / f"{wiki_name}.md"

        with open(output_file, "w", encoding="utf-8") as outfile:
            # Write h1 header from folder
            outfile.write(f"# {wiki_name}\n\n")

            folder_path = Path(docs_dir) / folder

            # Add to table of contents
            outfile.write("## Table of Contents\n")
            for md_file in sorted(folder_path.glob("*.md")):
                title = md_file.stem.replace("-", " ")
                outfile.write(f"- [{title}](#{title.lower().replace(' ', '-')})\n")  # noqa:E501
            outfile.write("\n")

            for md_file in sorted(folder_path.glob("*.md")):
                if md_file.name.lower() == "readme.md":  # Skip README
                    continue

                # Write h2 from filename
                title = md_file.stem.replace("-", " ")
                outfile.write(f"## {title}\n\n")

                # Write file content
                with open(md_file, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    content = re.sub(r"^#\s+.+\n", "",
                                     content,
                                     flags=re.MULTILINE)
                    outfile.write(content + "\n\n")


if __name__ == "__main__":
    docs_dir = "docs"
    output_dir = "wiki"
    os.makedirs(output_dir, exist_ok=True)
    merge_folder_to_wiki(docs_dir, output_dir)
