from src.crawler import crawl_site
from src.indexer import tokenize, build_index
from src.indexer import tokenize

index = {}

def build():

    global index

    pages_content = crawl_site()

    index = build_index(pages_content)

    save_index(index)

    print("Build completed.")


def shell():

    global index

    print("Search Engine Tool")

    while True:

        command = input("\n> ").strip()

        if command == "build":

            build()

        elif command == "load":

            index = load_index()

        elif command.startswith("print "):

            word = command[6:]
            print_word(index, word)

        elif command.startswith("find "):

            query = command[5:]
            find_query(index, query)

        elif command == "exit":

            print("Goodbye.")
            break

        else:

            print("Unknown command.")

if __name__ == "__main__":
    shell()