import wikipedia
import concurrent.futures
import time
import re
import os

def sanitize_filename(filename):
    """
    Remove characters that are not allowed in filenames.
    """
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def wiki_dl_and_save(topic):

    # Retrieve the Wikipedia page for the topic with auto_suggest turned off.
    page = wikipedia.page(topic, auto_suggest=False)


    # Get the page title and references.
    title = page.title
    references = page.references  # Should be a list of URL strings.
    
    # Sanitize the title so it can be used as a valid filename.
    filename = sanitize_filename(title) + ".txt"
    
    # Determine the directory where this script resides.
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        # Fallback if __file__ is not defined.
        script_dir = os.getcwd()
    
    # Build the full file path.
    filepath = os.path.join(script_dir, filename)
    
    # Write all references into the file, one per line.
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            for ref in references:
                file.write(str(ref) + "\n")
    except Exception as e:
        print(f"Error writing file '{filename}': {e}")

def main():
    # Start the performance counter.
    start_time = time.perf_counter()
    
    # 1. Use wikipedia.search to get topics related to 'generative artificial intelligence'
    query = "generative artificial intelligence"
    topics = wikipedia.search(query)
    
    # 3. Use ThreadPoolExecutor to concurrently process each topic with wiki_dl_and_save.
    concurrent.futures.ThreadPoolExecutor().map(wiki_dl_and_save, topics)
    
    # 4. Print the total execution time.
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    main()
