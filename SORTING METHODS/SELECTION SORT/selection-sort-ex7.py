# You work at a digital library, Each book record includes: [title, author, year_published, rating]
# Write a program using selection sort that: 1.Sorts the books in descending order of rating
# 2.If two books have the same rating, sort them alphabetically by title, 3.Prints the sorted list in a clean format

class Selection_Sort:

    def library_books(self, books):

        for i in range(len(books)):
            rating_score = i

            for j in range(i + 1, len(books)):
                if books[j][3] > books[rating_score][3]:
                    rating_score = j
                elif books[j][3] == books[rating_score][3] and books[j][0] < books[rating_score][0]:
                    rating_score = j

            books[i], books[rating_score] = books[rating_score], books[i]

        
        for title, author, year_published, rating in books:
            print(f"Title: {title} | Author: {author} | Year: {year_published} | Rating: {rating}")

        return books
    

books = [
    ["The Alchemist", "Paulo Coelho", 1988, 4.7],
    ["1984", "George Orwell", 1949, 4.9],
    ["To Kill a Mockingbird", "Harper Lee", 1960, 4.8],
    ["The Great Gatsby", "F. Scott Fitzgerald", 1925, 4.7],
    ["Pride and Prejudice", "Jane Austen", 1813, 4.9],
    ["Moby Dick", "Herman Melville", 1851, 4.3],
    ["The Catcher in the Rye", "J.D. Salinger", 1951, 4.5]
]

SS = Selection_Sort()
SS.library_books(books)
