# Decision Log: Storage Choice

## Decision
I chose **CSV** (data.csv) to store the daily water delivery demand data.

## Options compared

| Option | Pros | Cons |
|--------|------|------|
| CSV | Simple, opens in Excel/pandas directly, easy to share on GitHub | No SQL queries, slow for huge data, no data types |
| SQLite | Supports SQL queries, handles bigger data, built into Python | Binary file, can't be read in a text editor, extra setup |
| Parquet | Fast, small file size | Needs extra library, not human-readable |

## Why CSV
- Data is small (6,570 rows: 730 days x 3 regions x 3 product types), so speed is not an issue.
- pandas loads it in one line: `pd.read_csv("data.csv")`.
- Mentor and others can open it easily on GitHub.

## When I would switch
If data grows to millions of rows or needs SQL queries, I would use SQLite.