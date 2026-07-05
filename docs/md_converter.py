import os
import re
import json
import xml.sax.saxutils as saxutils


def load_config(config_path="config.json"):
    """Loads script configuration from a JSON file."""
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_markdown_file(file_path):
    """
    Reads a markdown file.
    1. Extracts the main Category Name from the first Heading 1 (#) found.
    2. Extracts topic sections divided by Heading 2 (##) syntax.
    3. Strips one hashtag from sub-headings (lines starting with 3+ hashtags).
    4. Performs text sanitization and escaping (backslashes, XML, newlines, parentheses).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the very first Heading 1 (#) to use as the category name
    h1_match = re.search(r"^#\s+(.+)$", content, flags=re.MULTILINE)
    if h1_match:
        category_name = h1_match.group(1).strip()
    else:
        # Fallback if a file lacks a Heading 1 element
        category_name = "Untitled Category"

    # Split content by lines starting with '##' (Heading 2)
    chunks = re.split(r"^##\s+", content, flags=re.MULTILINE)

    sections = []
    # The first chunk contains text before the first '##' (like the main # title), so we skip it
    for chunk in chunks[1:]:
        if not chunk.strip():
            continue

        lines = chunk.splitlines()
        if not lines:
            continue

        # The first line of the chunk is the Heading 2 title text
        title_text = lines[0].strip()

        # Everything else is the body content under that heading
        body_lines = lines[1:]
        processed_body_lines = []

        for line in body_lines:
            # Stripping extra hashtags: check if line starts with 3 or more hashtags (e.g., ###, ####)
            # ^(#+)(#)\s* matches the hashtags, capturing all but the last one in group 1
            # Hashtags are stripped to for cleaner presentation in Encyclopedia Description Box
            # Removes the last hashtag if 3 or more
            # modified_line = re.sub(r"^(##+)(#)(\s+.*|$)", r"\1\3", line)
            # Removes the last two hashtags if 3 or more
            modified_line = re.sub(r"^(#+)(##)(\s+.*|$)", r"\1\3", line)
            processed_body_lines.append(modified_line)

        body_content = "\n".join(processed_body_lines).strip()

        if title_text:
            # --- 1. ESCAPE BACKSLASHES FIRST ---
            title_text = title_text.replace("\\", "\\\\")
            body_content = body_content.replace("\\", "\\\\")

            # --- 2. ESCAPE XML CHARACTERS (&, <, >) ---
            escaped_title = saxutils.escape(title_text)
            escaped_body = saxutils.escape(body_content)

            # --- 3. CONVERT NEWLINES ---
            single_line_body = escaped_body.replace("\n", "\\n")

            # --- 4. ESCAPE PARENTHESES ---
            single_line_body = single_line_body.replace("(", "\\(").replace(")", "\\)")
            escaped_title = escaped_title.replace("(", "\\(").replace(")", "\\)")

            sections.append({"title": escaped_title, "body": single_line_body})

    return category_name, sections


def generate_xml():
    # 1. Load configuration
    config = load_config()
    prepend_file = config["prepend_file"]
    markdown_dir = config["markdown_dir"]
    output_file = config["output_file"]

    # 2. Read prepend XML content
    if os.path.exists(prepend_file):
        with open(prepend_file, "r", encoding="utf-8") as f:
            xml_output = f.read().strip()
    else:
        print(f"Error: Prepend file '{prepend_file}' not found.")
        return

    # 3. Find and sort all markdown files in the specified directory
    if not os.path.exists(markdown_dir):
        print(f"Error: Markdown directory '{markdown_dir}' does not exist.")
        return

    md_files = [f for f in os.listdir(markdown_dir) if f.endswith(".md")]
    md_files.sort()  # Ensure consistent processing order

    # 4. First pass: Parse files to collect categories based on internal markdown content
    valid_categories = []
    start_topic_page_id = 698008003

    for md_file in md_files:
        file_path = os.path.join(markdown_dir, md_file)
        category_name, sections = parse_markdown_file(file_path)

        if sections:
            valid_categories.append(
                {
                    "name": category_name,
                    "sections": sections,
                    "target_page_id": start_topic_page_id,
                }
            )
            start_topic_page_id += 1  # Increment target page ID for next category

    # If no files have sections, close XML and exit
    if not valid_categories:
        if not xml_output.endswith("</language>"):
            xml_output += "\n</language>\n"
        with open(output_file, "w", encoding="utf-8", newline="\n") as f:
            f.write(xml_output)
        print("No valid markdown sections found.")
        return

    # 5. Build Categories Section (Page ID 698008002)
    categories_xml = "\n"
    categories_xml += '  <page id="698008002" title="Lacuna Notebook Categories" descr="" voice="no">\n'

    cat_t_id = 1
    for cat in valid_categories:
        # First entry: Name extracted from Heading 1 (#)
        categories_xml += f'    <t id="{cat_t_id}">{cat["name"]}</t>\n'
        cat_t_id += 1
        # Second entry: Pointer to the page ID where entries are stored
        categories_xml += f'    <t id="{cat_t_id}">{cat["target_page_id"]}</t>\n'
        cat_t_id += 1

    categories_xml += "  </page>\n"
    xml_output += categories_xml

    # 6. Build Individual Topic Content Sections
    for cat in valid_categories:
        # Counter resets to 1 for every unique category page created
        t_id_counter = 1

        topic_xml = f'  <page id="{cat["target_page_id"]}" title="Lacuna Notebook {cat["name"]} Topics" descr="" voice="no">\n'

        for section in cat["sections"]:
            # First t_id: Heading 2 Title of the entry
            topic_xml += f'    <t id="{t_id_counter}">{section["title"]}</t>\n'
            t_id_counter += 1

            # Second t_id: Single-line string body content under Heading 2
            topic_xml += f'    <t id="{t_id_counter}">{section["body"]}</t>\n'
            t_id_counter += 1

        topic_xml += "  </page>\n"
        xml_output += topic_xml

    # 7. Safely close out the root <language> element
    if not xml_output.endswith("</language>"):
        xml_output += "</language>\n"

    # 8. Write final contents to disk
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(xml_output)

    print(
        f"Success! Generated XML file using internal Markdown titles at: {output_file}"
    )


if __name__ == "__main__":
    generate_xml()
