# run ./pull_books.sh to get this books from https://gutenberg.org
def count_words(filename):
    """Count ~words in filename by space-splitting"""
    try:
        with open(filename) as f:
           words = f.read().split()
    except FileNotFoundError:
        print(f"No such file {filename}")
    else:
        print(f"{filename} as {len(words)} words")

books = ["alice.txt", "siddhartha.txt", "moby-dick.txt", "eng-fairy-tales.txt"]
for book in books:
    count_words(book)


