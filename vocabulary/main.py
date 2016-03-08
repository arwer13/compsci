#!/usr/bin/env python3
import sys
import pandas as pd
import sqlite3


def load_frequencies_from_excel(file_path):
    df = pd.read_excel(file_path, sheetname='SAT WordList')
    return df


def write_to_sqlite3_db(df, db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    query = 'INSERT INTO words (word, frequency) VALUES (?, ?)'
    for _, row in df.iterrows():
        try:
            values = (row['Word'], round(row['Avg']))
            cur.execute(query, values)
        except ValueError as e:
            pass  # pandas goes through many empty rows because there is filled row 11021

    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <text file with word frequencies> <db file>'.format(sys.argv[0]))
        sys.exit(1)

    words_file = sys.argv[1]
    db_file = sys.argv[2]

    freq_data = load_frequencies_from_excel(words_file)
    write_to_sqlite3_db(freq_data, db_file)


