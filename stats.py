def get_num_words(text):
  return len(text.split())

def get_char_count(text):
  text = list(text)
  count = {}
  for char in text:
    char = char.lower()
    if char in count:
      count[char] += 1
    else:
      count[char] = 1
  return count