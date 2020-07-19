# Week04 作业

## 作业背景：

在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。

因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。

## 作业要求：

请将以下的 SQL 语句翻译成 pandas 语句：

```SQL
1. SELECT * FROM data;
   // data
2. SELECT * FROM data LIMIT 10;
   // data.head(10)
3. SELECT id FROM data;  //id 是 data 表的特定一列
   // data['id']
4. SELECT COUNT(id) FROM data;
   // data['id'].count()
5. SELECT * FROM data WHERE id<1000 AND age>30;
   // data[(data['id'] < 1000) & (data['age'] > 30)]
6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
   // table1.groupby('id')[order_id].count()
7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
   // pd.merge(t1, t2, on='id')
8. SELECT * FROM table1 UNION SELECT * FROM table2;
   // pd.concat([table1, table2])
9. DELETE FROM table1 WHERE id=10;
   // table1.loc[table1['id'] != 10]
10. ALTER TABLE table1 DROP COLUMN column_name;
   // table1.drop(columns=column_name, axis=1)
```

#### 数据结构

维数 | 名称 | 描述
--- | --- | ---
1 | Series |带标签的一维同构数组
2 | DataFrame | 带标签的、大小可变的，二维异构表格

(SQL)[https://pandas.pydata.org/pandas-docs/stable/reference/io.html#sql] | -
--- | ---
read_sql_table(table_name, con[, schema, …]) | Read SQL database table into a DataFrame.
read_sql_query(sql, con[, index_col, …]) | Read SQL query into a DataFrame.
read_sql(sql, con[, index_col, …]) | Read SQL query or database table into a DataFrame.





## 参考链接

- [pandas 中文文档](https://www.pypandas.cn/)