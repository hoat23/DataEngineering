# HADOOP COMMANDS

## Config CLI paramters:
```bash
set hive.cli.print.header=true;
```


## Delete broad

```bash
hadoop fs -rm -r /path/file
```



# HIVE COMMANDS

## Insert data
```sql
INSERT INTO group_database.database_01  PARTITION (fieldpartition = 'yyyy-mm-dd')  VALUES
('col1','col2','col3',...,'coln'),
('col1','col2','col3',...,'coln')
```
## WITH AS
```sql
WITH name_temp_db
AS (
    SELECT * FROM group_database.database_01
),
AS (
   SELECT * FROM group_database.database_01
);
```
