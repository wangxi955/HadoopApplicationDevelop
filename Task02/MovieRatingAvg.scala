import org.apache.spark
import org.apache.spark.SparkContext
import org.apache.spark.{SparkConf, SparkContext}

object MovieRatingAvg {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("movie rating avg").setMaster("local");
    val sc = new SparkContext(conf);
    // 读取HDFS文件系统中三个文件的数据
    val rdd1 = sc.textFile("hdfs://s198hadoop:9000/user/hadoop/input/u.data")
    val rdd2 = sc.textFile("hdfs://s198hadoop:9000/user/hadoop/input/u.item")
    val rdd3 = sc.textFile("hdfs://s198hadoop:9000/user/hadoop/input/u.user")
    // 获取u.item表中电影id和电影名
    val movieMsg = rdd2.map{x=>val line = x.split("\\|");(line(0),line(1))}
    // 获取u.data表中电影id和对应的评分，并将评分转为Float型
    var ratingMsg = rdd1.map(line =>(line.split("\t")(1).trim(),line.split("\t")(2).trim().toFloat))
    //movieMsg.foreach(x=>println("movieId: " + x._1+ "   movieName: " + x._2))
    //ratingMsg.foreach(x=>println("movieId: " + x._1+ "   rating: " + x._2))
    // 计算电影id对应的平均评分
    val ratingAvg =ratingMsg.mapValues(x=>(x,1)).reduceByKey((x,y)=>(x._1+y._1,x._2+y._2)).mapValues(x=>x._1/x._2)
    //ratingAvg.foreach(println)
    // 根据平均评分进行排序，并保留排名前100的电影
    val movieRatingAvg = ratingAvg.join(movieMsg).sortBy(x=>x._2._1,false,1).take(100)
    // 按照"电影ID::电影名，平均评分"的格式直接输出
    //movieRatingAvg.foreach(x=>println(x._1 + "::"+x._2._2+", "+x._2._1.formatted("%.2f")))

    // 定义输出文件，按照"电影ID::电影名，平均评分"的格式,小数点后保留两位
    val outputFile = movieRatingAvg.map(x=>x._1+ "::"+x._2._2+", "+x._2._1.formatted("%.2f"))
    // 字符串数组转换为RDD
    val test = sc.parallelize(outputFile)
    // 将输出输出到主节点的output目录下
    test.saveAsTextFile("hdfs://s198hadoop:9000/user/hadoop/output")
  }
}
