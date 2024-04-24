import os

def search_phrase_in_files(phrase, extensions):
    found_count = 0
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(tuple(extensions)):
                filepath = os.path.join(root, file)
                with open(filepath, 'rb') as f:
                    for line_number, line in enumerate(f, start=1):
                        try:
                            line = line.decode('utf-8')
                        except UnicodeDecodeError:
                            continue
                        if phrase in line:
                            print(f"Znaleziono w pliku: {filepath} :: Linia {line_number}: {line.strip()}")
                            found_count += 1
    print(f"Znaleziono {found_count} wystąpień.")

if __name__ == "__main__":
    search_phrase = input("Podaj tekst do wyszukania: ")
    print(f"Szukana fraza: {search_phrase}")
    extensions = ['.txt', '.py']
    search_phrase_in_files(search_phrase, extensions)
