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
SELECT * FROM tmp_db_02.field01 = tmp_db_02.field_01;
```

## CREATE TABLE
### Temporary
```hql
DROP TABLE IF EXISTS group_database.database_01;
CREATE TEMPORARY TABLE group_database.database_01
(
  fieldname_01  STRING,
  fieldname_02  STRING,
  fieldname_03  VARCHAR(30),
  fieldname_04  TIMESTAMP
)
STORED AS PARQUET
TBLPROPERTIES( "parquet.compress"="SNAPPY" );
```

### External
```hql
DROP TABLE IF EXISTS group_database.database_01;
CREATE EXTERNAL TABLE group_database.database_01
(
  fieldname_01 STRING,
  fieldname_02 STRING,
  fieldname_03 VARCHAR(30),
  fieldname_04  TIMESTAMP
)
STORED AS PARQUET
LOCATION '/${hiveconf:PRM_AMBIENTE}/bcp/udv/int/temp/H23_TMP_DIRECTORY'
TBLPROPERTIES( "parquet.compress"="SNAPPY" );
```
