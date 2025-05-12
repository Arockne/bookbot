from stats import get_num_words, get_char_count, sort_count

def get_book_text(filepath):
  file_contents = ''
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main():
  text = get_book_text('./books/frankenstein.txt')
  count = sort_count(get_char_count(text))

  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {get_num_words(text)} total words")
  print("--------- Character Count -------")
  for char_data in count:
    print(f"{char_data['char']}: {char_data['num']}")
  print("============= END ===============")

main()