ALTER TABLE library.books ADD COLUMN language VARCHAR(255) AFTER location;
ALTER TABLE library.books ADD COLUMN photo VARCHAR(255) AFTER language;