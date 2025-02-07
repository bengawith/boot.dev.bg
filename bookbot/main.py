from pathlib import Path


def get_path(filename: str) -> str:
    return Path.cwd() / "bookbot" / "books" / filename

class BookBot:
    def __init__(self, book_path):
        self.book_path = book_path
        self.name = self._get_name()
        self.contents = self._get_contents()
        self.words = self._len_book()
        self.char_dict = self._char_count()

    def _get_name(self) -> str:
        book_split = str(self.book_path).split("/")
        return book_split[-1]

    def _get_contents(self) -> str:
        with open(self.book_path) as f:
            book_contents = f.read()
        return book_contents
    
    def _len_book(self) -> int:
        return len(self.contents.split())
    
    def _char_count(self) -> dict:
        char_dict = {}
        for char in self.contents.lower():
            if char.isalpha():
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1
        return char_dict

    def print_info(self):
        print(f"--- Begin report of books/{self.name} ---")
        print(f"{self.words} words found in the document\n")
        for char in self.char_dict.keys():
            print(f"The '{char}' character was found {self.char_dict[char]} times")
        print("--- End report ---")
    
if __name__ == "__main__":
    book_path = get_path(input("Enter the name of the book: "))
    bb = BookBot(book_path)
    bb.print_info()
