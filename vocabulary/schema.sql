CREATE TABLE words (
    "id" INTEGER PRIMARY KEY,
    "word" TEXT NOT NULL UNIQUE,
    "frequency" INTEGER
);