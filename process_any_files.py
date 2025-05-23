import os


def process_any_files(root_dir):
    """
    Processes all .any files in the given directory and its subdirectories.
    Changes line endings to CRLF, trims trailing whitespaces, removes trailing blank lines, and ensures a single final CRLF newline.
    """
    for subdir, _, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith(".any"):
                filepath = os.path.join(subdir, filename)
                print(f"Processing file: {filepath}")
                try:
                    # Read lines and strip trailing whitespace from each
                    with open(filepath, 'r', encoding='utf-8') as f:
                        stripped_lines = [line.rstrip() for line in f.readlines()]

                    # Remove any blank lines from the end of the content
                    while stripped_lines and not stripped_lines[-1]:
                        stripped_lines.pop()
                    
                    # Prepare the final content string
                    if not stripped_lines:
                        # If all lines were empty or the file was originally empty,
                        # the content should be a single newline.
                        final_content_string = "\n"
                    else:
                        # Join lines with '\n' and add one final '\n'
                        final_content_string = "\n".join(stripped_lines) + "\n"

                    # Write back with CRLF line endings
                    with open(filepath, 'w', encoding='utf-8', newline='\r\n') as f:
                        f.write(final_content_string)
                    
                    print(f"Successfully processed: {filepath}")
                except Exception as e:
                    print(f"Error processing file {filepath}: {e}")

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Starting processing in directory: {script_dir}")
    process_any_files(script_dir)
    print("Processing complete.")
