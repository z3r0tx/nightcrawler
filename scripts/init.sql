\setenv DB_USER `cat .env | grep DB_USER | cut -d '=' -f 2-`
\setenv DB_PASSWORD `cat .env | grep DB_PASSWORD | cut -d '=' -f 2-`
\setenv DB_NAME `cat .env | grep DB_NAME | cut -d '=' -f 2-`

CREATE USER :DB_USER WITH PASSWORD :'DB_PASSWORD';

CREATE DATABASE :DB_NAME;

GRANT ALL PRIVILEGES ON DATABASE :DB_NAME TO :DB_USER;

\c :DB_NAME;

CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    source_name TEXT
);

CREATE TABLE IF NOT EXISTS headlines (
    id SERIAL PRIMARY KEY,
    source_id INT,
    title TEXT,
    link TEXT,
    publication_date TEXT,
    visited_on TIMESTAMP,
    FOREIGN KEY (source_id) REFERENCES sources (id)
);

