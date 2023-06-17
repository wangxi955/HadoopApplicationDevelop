package com.company;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;

public class TemperatureJob {
    public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
        Configuration conf = new Configuration();
        conf.set("fs.defaultFS","hdfs://s198hadoop:9000");
        String[] otherArgs = (new GenericOptionsParser(conf,args)).getRemainingArgs();
        if(otherArgs.length<2){
            System.err.println("Usage: Temperature <in> [<in>...] <out>");
            System.exit(2);
        }
        //获取作业对象
        Job job = Job.getInstance(conf,"Temperature");
        //设置主类
        job.setJarByClass(TemperatureJob.class);
        //设置job参数
        job.setMapperClass(TemperatureMap.class);
        job.setReducerClass(TemperatureReduce.class);
        //设置map和reduce输出类型
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        //设置job输入输出
        for(int i = 0; i < otherArgs.length - 1; ++i) {
            FileInputFormat.addInputPath(job, new Path(otherArgs[i]));
        }
        FileOutputFormat.setOutputPath(job, new Path(otherArgs[otherArgs.length - 1]));
        //提交作业
        System.out.println(job.waitForCompletion(true) ? 0 : 1);;
    }
}
