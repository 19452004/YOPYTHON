import requests

def search_genre(genre):
    base_url = f"https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": f"subject:{genre}",
        "maxResults": 20 
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'items' in data:
        print(f"Hasil pencarian untuk genre '{genre}':")
        for i, item in enumerate(data['items'], start=1):
            volume_info = item.get("volumeInfo", {})
            title = volume_info.get('title', 'N/A')
            authors = volume_info.get('authors', ['N/A'])

            print(f"{i}. {title} - {', '.join(authors)}")
    else:
        print(f"Tidak ditemukan buku untuk genre '{genre}'.")

def get_top_books_by_genre(genre, max_results=5):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": f"subject:{genre}",
        "orderBy": "relevance",
        "maxResults": max_results
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    top_books = []

    for item in data.get('items', []):
        volume_info = item.get("volumeInfo", {})
        title = volume_info.get('title', 'N/A')
        authors = volume_info.get('authors', ['N/A'])

        top_books.append({
            'title': title,
            'authors': ', '.join(authors),
        })

    return top_books

def search_by_title(title):
    base_url = f"https://www.googleapis.com/books/v1/volumes?q={title}"
    response = requests.get(base_url)
    return response.json()

def get_sorted_titles_from_api(title):
    base_url = f"https://www.googleapis.com/books/v1/volumes?q={title}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            titles = [item["volumeInfo"]["title"] for item in data["items"]]
            sorted_titles = sorted(titles)
            return sorted_titles
        else:
            return []
    else:
        print(f"Permintaan gagal dengan kode status {response.status_code}.")
        return []

def get_sorted_titles_from_api(karakter):
    base_url = f"https://www.googleapis.com/books/v1/volumes?q={karakter}"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])
        titles = [item["volumeInfo"]["title"] for item in items if item["volumeInfo"]["title"].lower().startswith(karakter.lower())]
        sorted_titles = sorted(titles)
        return sorted_titles
    else:
        print(f"Gagal melakukan HTTP request. Kode status: {response.status_code}")
        return []

def main1(karakter):
    sorted_titles = get_sorted_titles_from_api(karakter)
    if sorted_titles:
        print(f"Judul buku yang diurut          kan dan dimulai dengan huruf '{karakter}':")
        for title in sorted_titles:
            print(title)
    else:
        print(f"Tidak ada item buku yang dimulai dengan huruf '{karakter}' dalam hasil pencarian.")

    if __name__ == "__main__":
        karakter = input("Masukkan abjad: ")
        main1(karakter)
    
def main2():
    print("=====================================")
    print("=====SELAMAT DATANG DI E-LIBRARY=====")
    print("=====================================")
    print('')
    nama = input("Masukkan Nama Anda: ").upper()
    print('')
    print("SELAMAT DATANG",nama)

    while True:
        print('')
        print("==================================")
        print("|Pilih salah satu opsi :         |")
        print("==================================")
        print("|1. Cari berdasarkan genre       |")
        print("|2. Cari berdasarkan judul       |")
        print("|3. Cari judul berdasarkan abjad |")
        print("|4. Keluar                       |")
        print("==================================")
        print('')
        choice = input("Pilihan Anda (1/2/3): ")

        if choice == '1':
            print('')
            genre = input("Masukkan genre yang ingin dicari: ")
            try:
                print('')
                print("Pilih metode pencarian:")
                print("1. Top Rekomendasi")
                print("2. Semua Buku")
                print('')
                search_option = input("Pilihan Anda (1/2): ")

                if search_option == '1':
                    top_books = get_top_books_by_genre(genre)
                    if top_books:
                        print('')
                        print(f"Top Rekomendasi Buku untuk Genre '{genre}':")
                        for i, book in enumerate(top_books, start=1):
                            print(f"{i}. {book['title']} - {book['authors']}")
                    else:
                        print(f"Tidak ditemukan buku untuk Genre '{genre}'.")
                elif search_option == '2':
                    print('')
                    # Menambahkan sorting judul berdasarkan abjad
                    search_genre(genre)
                else:
                    print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            title = input("Masukkan judul buku yang ingin dicari: ")
            print("_______________________________________________")
            ketemu = -1
            try:
                data = search_by_title(title)
                for item in data.get('items', []):
                    volume_info = item.get("volumeInfo", {})
                    title = volume_info.get('title', 'N/A')
                    authors = volume_info.get('authors', ['N/A'])
                    description = volume_info.get('description', 'N/A')
                    publisher = volume_info.get('publisher', 'N/A')
                    publishedDate = volume_info.get('publishedDate', 'N/A')

                    print('')
                    print(f"Title: {title}")
                    print(f"Authors: {', '.join(authors)}")
                    print(f"Publisher: {publisher}")
                    print(f"Published Date: {publishedDate}")
                    print(f"Description: {description}")
                    print("\n---\n")
                    ketemu = 1
                    break

            except Exception as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            karakter = str(input("masukan abjad : "))
            hasil_pencarian = get_sorted_titles_from_api(karakter)
            if hasil_pencarian:
                print(f"Hasil pencarian untuk huruf awal '{karakter}':")
                for kata in hasil_pencarian:
                    print(kata)
            else:
                print(f"Tidak ditemukan entri dengan huruf awal '{karakter}'.")
                
        elif choice == '4':
            print("Terima kasih. Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main2()