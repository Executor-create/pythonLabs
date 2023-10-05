class BookBuilder:
    def __init__(self, book_type):
        self.book = Book(book_type)

    def add_page(self, page_content):
        self.book.add_page(page_content)

    def build(self):
        return self.book
    
    def create_book(builder, book_type, content):
      for i, page_content in enumerate(content, start=1):
        builder.add_page(f"Page {i} - {page_content}")
        pageSingleton.add_page(id(page_content))
      return builder.build()

class Book:
    def __init__(self, book_type):
        self.book_type = book_type
        self.content = []

    def add_page(self, page_content):
        self.content.append(page_content)

class PageSingleton:
    _instance = None
    _page_id = set()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PageSingleton, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def add_page(page_id):
        PageSingleton._page_id.add(page_id)

    @staticmethod
    def get_page_ids():
        return list(PageSingleton._page_id)

pageSingleton = PageSingleton()

characters = {
  "Herald from Rivia": "Witcher who kills all monsters in Poland",
  "Kartman": "Fatass guy",
  "Invoker": "Piano for your crooked hands",
  "Pudge": "The same as Cartman, only kinder",
  "Giant from Skyrim": "Сan launch you into the stratosphere"
}

images = {
  "1": "https://www.pinterest.com/pin/cartman--33073378503342646/",
  "2": "https://www.pinterest.com/pin/141230138306880771/",
  "3": "https://www.pinterest.com/pin/604537949995175440/",
  "4": "https://www.pinterest.com/pin/south-park-in-2023--314337249005405425/",
  "5": "https://www.pinterest.com/pin/678284393903261096/",
  "6": "https://www.pinterest.com/pin/72690981479185097/"
}

science_content = ["Content for scientific books", "References", "glossary"]
scientific_book_builder = BookBuilder("Science Book")
scientific_book = scientific_book_builder.create_book("Science Book", science_content)

novel_content = [f"{key}: {desc}" for key, desc in characters.items()]
novel_builder = BookBuilder("Novel")
novel = novel_builder.create_book("Novel", novel_content)

manual_content = [link for link in images.values()]
manual_builder = BookBuilder("Manual")
manual = manual_builder.create_book("Manual", manual_content)

page_ids = pageSingleton.get_page_ids()

print("Science Book:")
print(vars(scientific_book))
print("\nNovel:")
print(vars(novel))
print("\nManual:")
print(vars(manual))
print("\nUnique Page IDs:", page_ids)
