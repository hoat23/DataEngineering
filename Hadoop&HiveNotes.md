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
SET hive.execution.engine = mr;
SET spark.job.queue.name = default;

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

## PIVOT ROWS IN COLUMNS

TABLA:
```-----------------------------------------------
fecinteraccion	codappautorizador	cant	
-----------------------------------------------
 2021-05-25	          AM	        585	
 2021-05-25	          CP	        213563	
 2021-05-25	          GT	        98055	
 2021-05-25	          NS	        94	
 2021-05-25	          OE	        2388	
 2021-05-25	          PH	        114	
 2021-05-25	          PS	        29377	
 2021-05-25	          PZ	        39994	
 2021-05-25	          SY	        820387	
 2021-05-25	          TF	        4375	
 2021-05-25	          TI	        98	
 2021-05-25	          TM	        1519	
-----------------------------------------------
```

```hql
SELECT
  fecinteraccion, 
  COLLECT_SET(AM)[0] AS AM,
  COLLECT_SET(CP)[0] AS CP,
  COLLECT_SET(GT)[0] AS GT,
  COLLECT_SET(NS)[0] AS NS,
  COLLECT_SET(OE)[0] AS OE,
  COLLECT_SET(PH)[0] AS PH,
  COLLECT_SET(PS)[0] AS PS,
  COLLECT_SET(PZ)[0] AS PZ,
  COLLECT_SET(SY)[0] AS SY,
  COLLECT_SET(TF)[0] AS TF,
  COLLECT_SET(TI)[0] AS TI,
  COLLECT_SET(TM)[0] AS TM
FROM (
	SELECT
		fecinteraccion,
		case when codappautorizador='AM' then cant as AM
		case when codappautorizador='CP' then cant as CP
		case when codappautorizador='GT' then cant as GT
		case when codappautorizador='NS' then cant as NS
		case when codappautorizador='OE' then cant as OE
		case when codappautorizador='PH' then cant as PH
		case when codappautorizador='PS' then cant as PS
		case when codappautorizador='PZ' then cant as PZ
		case when codappautorizador='SY' then cant as SY
		case when codappautorizador='TF' then cant as TF
		case when codappautorizador='TI' then cant as TI
		case when codappautorizador='TM' then cant as TM
		FROM TABLA
) TBL1
GROUP BY fecinteraccion;
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

## FUNCTIONS

### Convertion functions

#### cast
```hql
select cast((t1*1000 +t2.1000) as varchar) from t1.
```
#### try_cast
```hql
 select try_cast((t1*1000 +t2.1000) as varchar) from t1.
 ```
 ### typeof
 ```hql
Select typeOf('chanchal') ; 
>output :-- varchar(8)
 ```
## Mathematical functions
- abs(n): This function returns the absolute value.
- cbrt(n): This method returns the cube root of a given number.
- ceiling(n): This function returns n rounded up to the nearest integer.
- floor(n): This method returns n rounded down to the nearest integer
- power(x, y): This function returns x raised to the power of y.
 
## String functions
- concat(string1, ..., stringN): This function is used to concatenate multiple string into a single string: select concat('packt','publication') as concat_value;.
- length(string): This function returns the length of a string.
- lower(string): This function converts a string to lowercase, which means that lowercase('CHINA') would return CHINA.
- ltrim(string): This function removes any leading whitespace from a string.
- rtrim(string): This function removes trailing whitespace from a string.
- replace(sourcestring, search): This function removes all instances of a search string from a string.
- replace(string, searchstring, replace): This function replaces all instances of search strings with replace strings in the original string.
- reverse(string): This function reverses the string.
- split(string, delimiter): This split function in Presto is similar to the split function of Java that splits the string based on delimiter and returns the array of string.
- split(string, delimiter, limit): This is an advanced version of the split function which splits the string on delimiter and returns an array of string with limit specified. The last string index in the array always contains everything left in the string.
- split_part(string, delimiter, index): This function splits the string on delimiter and returns the string at index. The index starts with 1 and if the index is greater than the number of fields, then null is returned.
