jungle_book = "jungle_book.txt"

def read_file(filename):
    source_file = open(filename, "r")
    list_of_lines = source_file.readlines()
	source_file.close
	
	return list_of_lines

lines_from_file = read_file(jungle_book)
count_words_from_list_of_lines(lines_from_file)

def count_words_from_list_of_lines(lines_from_file)
    word_count = 0
	
	for line in lines_from_file:
	    word_count += len(line.split())
	return word_count

word_count = count_words_from_list_of_lines(lines_from_file)

def make_huge_list_from_lines(lines_from_file):
    huge_list = []
    for line in lines_from_file:
	    words_in_line = line.split()
		huge_list.extend(words_in_line)
	return huge_list

huge_list = make_huge_list_from_lines(lines_from_file)

unique











source_file.close()