# HadoopApplicationDevelop

## 本仓库为Hadoop课程设计存档，主要分为四个任务

### 搭建Hadoop和Spark集群
#### 搭建Hadoop
准备工作：
（1）选定一台机器作为 Master
（2）在 Master 节点上配置 hadoop 用户、安装 SSH server、安装 Java 环境
（3）在 Master 节点上安装 Hadoop，并完成配置
（4）在其他 Slave 节点上配置 hadoop 用户、安装 SSH server、安装 Java 环境（可采用脚本分发）
（5）将 Master 节点上的 /usr/local/hadoop 目录复制到其他 Slave 节点上
（6）在 Master 节点上开启 Hadoop
网络配置：
（1）搭建5台机器组成集群模式，s198hadoop作为主节点，其余作为从节点。
- 10.244.1.51  s198hadoop
- 10.244.1.99  s194hadoop
- 10.244.1.117 s193hadoop
- 10.244.1.101 s195hadoop
- 10.244.1.107 s197hadoop
（2）分别修改5台虚拟机的/etc/hosts文件，编写集群节点主机名与IP地址的映射关系
（3）集群/分布式模式配置：
- 集群/分布式模式需要修改 /usr/local/hadoop/etc/hadoop 中的5个配置文件。配置workers、code-site.xml、hdfs-site.xml、hdfs-site.xml、mapred-site.xml、yarn-site.xml文件
- 在主节点上将公钥传输到从节点，在从节点将ssh公钥加入授权
（4）可从http://s198hadoop:8088/cluster/查看hadoop集群

#### 搭建Spark
（1）集群分布式配置：
修改/usr/local/spark文件夹下的slaves、spark-env.sh文件夹
之后把整个/usr/local/spark文件夹压缩分发到各个节点
（2）可从http://s198hadoop:7077查看spark集群

### 任务一 气象数据集分析，求每日最高和最低气温
采用数据集为ftp://ftp.ncdc.noaa.gov/pub/data/noaa
![image](https://github.com/wangxi955/HadoopApplicationDevelop/assets/80522598/9a200ded-828b-4577-93d3-c7494b3a9170)
需要导入jar包
具体代码放在Task01

### 任务二 电影评分数据集分析，平均评分最高的100部电影，并给出平均评分
采用数据集为https://grouplens.org/datasets/movielens/ 
![image](https://github.com/wangxi955/HadoopApplicationDevelop/assets/80522598/7cb2bf67-6edb-4091-8245-f3a441d8384a)
具体代码放在Task02

### 任务三 电商网站评价数据分析
1、爬取电商网站商品详情页的商品评价数据（数据采集）
2、清洗电商评价数据（数据清洗）
对采集到的数据进行清洗，提取出需要的字段，以得到结构化的文本文件
3、利用HiveSQL离线分析评价数据（数据装载、分析）
使用Hive对以下指标进行统计：
1）统计每天评论数
2）统计每个评分段（score）的人数
即统计出评1分的人数数量；2分的人数统计；……
4、利用Sqoop进行数据迁移至Mysql数据库（数据迁移）
将Hadoop上的分析结果迁移到关系数据库中
5、完成数据图表展示过程（数据可视化）
常用可视化工具   JavaWeb + Echarts   或   pyecharts + matplotlib 等
1）统计每天评论数   给出折线图
2）统计每个评分段（score）的人数   给出柱状图
6、编写Spark应用程序，利用分词算法（如：IKAnalyzer）分析电商评论数据，对每个分词进行词频统计，统计结果存入MySQL；利用可视化工具读取MySQL，给出词云图。
具体代码放在Task03

### 任务四 ELK(ElasticSearch, Logstash, Kibana)环境搭建，附上B站数据分析
1.从elastic官网下载filebeat、logstash、elasticsearch、kibana软件，软件版本统一为7.16.2。
- 配置elasticsearch.yml文件
- 配置logstash,在/usr/local/logstash/bin目录下新建logstash1.conf文件
- 配置kibana.yml文件
2.通过python采集数据，然后把所采集的数据存入本地文件

