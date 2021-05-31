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

## CONFIG PERFOMANCE

```hql
-- Configuracion base
SET hive.exec.compress.output = true;
SET parquet.compression = snappy;
SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;
SET hive.execution.engine = ${hiveconf:PRM_HIVE_ENGINE};
SET spark.job.queue.name = ${hiveconf:PRM_HIVE_QUEUE};

 

-- Configuracion Mappers
SET mapreduce.job.maps = 60;
SET mapreduce.map.cpu.vcores = 2;
SET mapreduce.input.fileinputformat.split.maxsize = 100000000000;
SET mapreduce.input.fileinputformat.split.minsize = 100000000000;
SET mapreduce.map.memory.mb = 8500;

-- Configuracion Reducers
SET mapreduce.job.reduces = 60;
SET mapreduce.reduce.cpu.vcores = 2;
SET mapreduce.reduce.memory.mb = 10000;
```


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
  fieldname_04 TIMESTAMP
)
STORED AS PARQUET
LOCATION '/${hiveconf:PRM_AMBIENTE}/bcp/udv/int/temp/H23_TMP_DIRECTORY'
TBLPROPERTIES( "parquet.compress"="SNAPPY" );
```
