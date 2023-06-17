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


