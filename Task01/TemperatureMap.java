package com.company;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import java.io.IOException;

public class TemperatureMap extends
        Mapper<LongWritable,Text, Text, IntWritable> {
    private static final int MISSING = 9999;
    @Override
    protected void map(LongWritable key,Text value,Context context) throws IOException, InterruptedException {
        //读取一条数据
        String line = value.toString();
        //获取日期
        String year = line.substring(15,23);
        int airTem;
        if(line.charAt(87) == '+'){
            //判断温度正负
            airTem = Integer.parseInt(line.substring(88,92));
        }else{
            airTem = Integer.parseInt(line.substring(87,92));
        }
        String quality = line.substring(92,93);
        //判断温度是否异常
        if(airTem != MISSING && quality.matches("[01459]")){
            try{
            context.write(new Text(year),new IntWritable(airTem));
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        };
    }
}
