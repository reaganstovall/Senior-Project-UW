package co.brewscience.automationstation;

import android.support.v4.util.TimeUtils;
import android.util.Log;

import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.TimeZone;
import java.util.concurrent.TimeUnit;

/**
 * Created by andrew on 5/20/17.
 */

public class Graphpointsandtime {
    int id;
    List<Double> values;
    List<Long> time;
    SettingsToStore sts;
    Date startdate;
    Date enddate;
    Date starttime;
    Date endtime;


    Graphpointsandtime(int id, SettingsToStore s2s){
        this.id = id;
        sts = s2s;
        startdate = new Date(sts.getStartdate());
        enddate = new Date(sts.getEnddate());
        starttime = new Date(sts.getStarttime());
        endtime = new Date(sts.getEndtime());
        values = new ArrayList<>();
        time = new ArrayList<>();

    }
    //, int units, int start, int end
    public void setValueandTime(double vvalue, String vtimestring){

        int milseconds = 0;
        int seconds = 0;
        int min = 0;
        int hour = 0;
        int day = 0;
        long month = 0;
        long year = 0;
        long temp = 0;

        Date sensordate = new Date((long)(Double.parseDouble(vtimestring)* 3600 * 1000));
        long epotime = sensordate.getTime();
      /*  temp = sensordate.getTime();
        milseconds = (int)(temp%1000);
        temp = (temp)/1000;
        seconds = (int)(temp%60);
        temp = (temp)/60;
        min = (int)(temp%60);
        temp = temp/60;
        hour = (int)(temp%24)- 7;
        temp = temp/24;*/


        SimpleDateFormat format = new SimpleDateFormat("dd/MM/yyyy", Locale.US);
        format.setTimeZone(TimeZone.getDefault());

/*
        Log.d("Time", "setValueandTime: "+ "calculated date:"+ format.format(sensordate)+ " time: " + hour+ "hr "+ min + "min. " + seconds + "sec.");
*/
        //TODO need to only add to array if


            if(sts.isCheckboxtime()){

                if(sensordate.after(startdate)){

                            values.add(vvalue);
                            time.add(epotime);

                }


            }
            else{

                if(sensordate.after(startdate) && sensordate.before(enddate)){
                            values.add(vvalue);
                            time.add(epotime);
                }


            }


        }


    public LineGraphSeries<DataPoint> getSeries(){
        LineGraphSeries<DataPoint> series = new LineGraphSeries<>();
        DataPoint dp;
        for(int i = 0; i<values.size(); i++){


            dp = new DataPoint(time.get(i),values.get(i));

            series.appendData(dp,true,100);



        }
        return series;
    }

}
