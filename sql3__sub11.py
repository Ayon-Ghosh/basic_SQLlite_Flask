import	sqlite3
SELECT name, sql FROM sqlite_master
WHERE type='table'
ORDER BY name;
