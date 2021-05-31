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
```hql
INSERT INTO group_database.database_01  PARTITION (fieldpartition = 'yyyy-mm-dd')  VALUES
('col1','col2','col3',...,'coln'),
('col1','col2','col3',...,'coln')
```

## WITH AS
```hql
WITH 
tmp_db_01 AS (
    SELECT * FROM group_database.database_01
),
tmp_db_02 AS (
    SELECT * FROM group_database.database_02
)
SELECT * FROM tmp_db_02.field01 = tmp_db_02.field_01
;
```


