import sys

def count_words(filename, N):
  # Open the file and read its contents
  with open(filename) as f:
    contents = f.read()

  # Split the contents into a list of words
  words = contents.split()

  # Create an empty dictionary to store the word counts
  word_counts = {}

  # Loop through the list of words and count the frequency of each word
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  # Sort the dictionary by count in descending order
  sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

  # Print the top N most common words
  for i in range(N):
    word, count = sorted_word_counts[i]
    print(f'{word}: {count}')

# Main function
def main():
  # Get the name of the file to read from the command line
  filename = sys.argv[1]

  # Get the number of most common words to print from the command line
  N = int(sys.argv[2])

  # Count the words in the file and print the top N most common words
  count_words(filename, N)

if __name__ == '__main__':
  main()
