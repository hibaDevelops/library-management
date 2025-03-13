ALTER TABLE library.books ADD COLUMN language VARCHAR(255) AFTER location;
ALTER TABLE library.books ADD COLUMN photo VARCHAR(255) AFTER language;
ALTER TABLE library.books ADD COLUMN bookstore_location VARCHAR(255) AFTER location;
ALTER TABLE library.books CHANGE location library_location VARCHAR(255);