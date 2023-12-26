import re

def extract_tags(readme_content):
    pattern = r"`(Tag\w+)`"  # Adjust the regex pattern based on your tag format
    return set(re.findall(pattern, readme_content))

def update_readme_with_tags(readme_content, tags):
    # Define start and end markers for the tags section
    start_marker = "## Aggregated Tags\n"
    end_marker = "\n## End of Aggregated Tags"

    # Remove the old tags section
    start_index = readme_content.find(start_marker)
    end_index = readme_content.find(end_marker)
    if start_index != -1 and end_index != -1:
        readme_content = readme_content[:start_index] + readme_content[end_index + len(end_marker):]

    # Add the new tags section with each tag in a box, all in one row
    tags_formatted = ' '.join(f"`{tag}`" for tag in sorted(tags))
    new_tags_section = f"{start_marker}\n{tags_formatted}\n{end_marker}"
    return readme_content + "\n\n" + new_tags_section

def main():
    with open('README.md', 'r') as file:
        readme_content = file.read()

    tags = extract_tags(readme_content)
    updated_readme = update_readme_with_tags(readme_content, tags)

    with open('README.md', 'w') as file:
        file.write(updated_readme)

if __name__ == "__main__":
    main()