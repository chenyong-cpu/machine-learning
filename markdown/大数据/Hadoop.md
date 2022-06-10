# Hadoop

## 概念

1. 大数据(big data)，或称巨量资料，指的是所涉及的资料量规模巨大到无法透过主流软件工具，在合理时间内达到撷取、管理、处理、并整理成为帮助企业经营决策更积极目的的资讯。
2. 特点（4V）
   1. 大量（Volume）
   2. 高速（Velocity）
   3. 多样（Variety）
   4. 低价值密度（Value）
3. Hadoop是一个分布式系统基础框架
   1. 海量数据的储存
   2. 海量数据的计算
4. 优势
   1. 高可靠性：存在多个副本
   2. 高扩展性：动态扩展节点
   3. 高效性：并行工作
   4. 高容错性：失败的任务重新分配

## HDFS架构

1. NameNode（nn）：储存文件的元数据，如文件名，文件目录结构，文学属性，以及每个文件的快列表和所在的DataNode
2. DataNode（dn）：在本地文件系统储存文件块数据，以及数据的校验和
3. Secondary NameNode(2nn)：美隔一段时间对NameNode的元数据进行备份

## YARN架构

1. ResourceManager（RM）：整个集群资源的老大
2. NodeManager（NM）：单个节点服务器资源老大
3. ApplicationMaster（AM）：单个人物运行的老大
4. Container：容器，相当于一台独立的服务器，里面封装了任务运行需要的资源

## 大数据技术生态体系

![avator](resource/1.png)

## 集群部署

1. NameNode,Secondary NameNode,ResourceManager分贝放在三台服务器上
2. 配置文件说明
   1. 默认配置文件
      1. core-default.xml
      2. hdfs-default.xml
      3. mapred-default.xml
      4. yarn-default.xml
   2. 自定义配置文件
      1. core-site.xml
         1. 指定NameNode的地址
         2. 指定hadoop数据的储存目录
         3. 配置HDFS网页登录使用的静态用户
      2. hdfs-site.xml
         1. NameNode的web端访问地址
         2. Secondary-NameNode的web端访问地址
      3. yarn-site.xml
         1. 指定MR走shuffle的地址
         2. 指定ResourceManager的地址
         3. 环境变量的继承
         4. 日志聚焦功能
      4. mapred-site.xml
         1. 指定MapReduce运行在yarn上（默认是本地运行）
         2. 配置历史服务器
3. 配置work
4. 启动集群
   1. 如果集群是第一次启动，需要格式化NameNode节点
      1. hdfs namenode -format
   2. 启动HDFS
      1. sbin/start-hdfs.sh
   3. 启动YARN
      1. sbin/start-yarn.sh
5. hdfs上传文件
   1. hadoop fs -put 文件
6. 常用端口
   1. NameNode内部常用端口：8020/9000/9820
   2. NameNode用户查询端口：9870
   3. Yarn查看任务运行情况：8088
   4. 历史服务器：19888

## HDFS

> 分布式文件系统，适合一次写入多次读出的场景

1. 优点
   1. 高容错性
   2. 适合处理打数据
   3. 可构建在廉价机器上
2. 缺点
   1. 不适合低延时数据访问
   2. 无法高效的对大量小文件进行储存
   3. 不适合并发写入，文件随机修改
3. NameNode
   1. 管理HDFS名称空间
   2. 配置副本策略
   3. 管理数据快映射信息
   4. 处理客户端读写请求
4. DataNode
   1. 储存实际的数据块
   2. 执行数据块的读/写操作
5. Client：客户端
   1. 文件切分
   2. 与NameNode交互，获取文件的位置信息
   3. 与DataNode交互，读取或者写入数据
   4. Client提供命令
6. 文件块大小：分块储存
   1. 文件块默认值为128M
   2. 寻址时间为传输时间的1%为最佳状态
7. SHELL操作
   1. hadoop fs先生操作命令
   2. -moveFromLocal 从本地剪切粘贴到HDFS
   3. -copyFromLocal 从本地文件系统中拷贝到HDFS路径去
   4. -put 等同于copyFromLocal,生产环境更习惯用put
   5. -appendToFile 追加一个文件到已经存在文件末尾
   6. -copyToLocal 从HDFS拷贝到本地
   7. -get 等同于copyToLocal,生产环境更习惯用get
   8. -ls 显示目录信息
   9. -cat 显示文件内容
   10. -chgrp -chmod -chown
   11. -mkdir 创建路径
   12. -cp
   13. -mv
   14. -tail 显示文件末尾1KB的数据
   15. -rm 删除文件或文件夹
   16. -rm -r 递归删除目录及目录里面内容
   17. -du 统计删除目录及目录里面内容
   18. -du 统计文件夹的大小信息
   19. -setrep 设置HDFS文件的副本数量
8. 写数据流程
9. 读数据流程
