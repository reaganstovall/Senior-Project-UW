package co.brewscience.automationstation;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.helper.DateAsXAxisLabelFormatter;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Locale;
import java.util.Timer;
import java.util.TimerTask;

/**
 * Created by andrew on 4/23/17.
 */


public class Graph extends AppCompatActivity {

   // private Button buttonAdd;
    private GraphView graph;
    private GraphView graph1;
    private GraphView graph2;
    private GraphView graph3;
    private GraphView graph4;
    private GraphView graph5;
    private GraphView graph6;
    private GraphView graph7;
    private GraphView graph8;
    private GraphView graph9;
    private GraphView graph10;
    private GraphView graph11;
    private GraphView graph12;
    private GraphView graph13;
    private GraphView graph14;
    private GraphView graph15;
    ArrayList<Graphpointsandtime> gpt;
    String[] gettingSen;
    private Timer autoUpdate;
    private static int TIMETOWAIT = 60000; //40sec = 40_000
    SettingsToStore sts;

    @Override


    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.graph);


        sts = load();

        Intent intent = getIntent();
        String graphstoadd = intent.getStringExtra("SENSOR");
        gettingSen = graphstoadd.split(",");
        SimpleDateFormat format = new SimpleDateFormat("dd, HH:mm", Locale.US);

        //TODO add viewport to each graph
        //TODO fix setting time
       for(int i =0; i < gettingSen.length; i++){
           if(gettingSen[i].equalsIgnoreCase("")){
           }
          else if(Integer.parseInt(gettingSen[i].trim()) == 1) {
               graph = (GraphView) findViewById(R.id.graph);
               graph.setVisibility(View.VISIBLE);
               graph.setTitle("Sensor 1");
               graph.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph.getViewport().setScrollable(true); // enables horizontal scrolling
           }
           else if(Integer.parseInt(gettingSen[i].trim()) == 2){
              graph1 = (GraphView) findViewById(R.id.graph1);
              graph1.setTitle("Sensor 2");
               graph1.setVisibility(View.VISIBLE);
               graph1.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph1.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph1.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 3){
              graph2 = (GraphView) findViewById(R.id.graph2);
              graph2.setTitle("Sensor 3");
               graph2.setVisibility(View.VISIBLE);
               graph2.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph2.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph2.getViewport().setScrollable(true); // enables horizontal scrolling
           }else if(Integer.parseInt(gettingSen[i].trim()) == 4){
              graph3 =(GraphView) findViewById(R.id.graph3);
              graph3.setTitle("Sensor 4");
               graph3.setVisibility(View.VISIBLE);
               graph3.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph3.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph3.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 5){
              graph4 = (GraphView) findViewById(R.id.graph4);
              graph4.setTitle("Sensor 5");
              graph4.setVisibility(View.VISIBLE);
               graph4.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph4.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph4.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 6){
              graph5 = (GraphView) findViewById(R.id.graph5);
              graph5.setTitle("Sensor 6");
              graph5.setVisibility(View.VISIBLE);
               graph5.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph5.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph5.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 7){
              graph6 = (GraphView) findViewById(R.id.graph6);
              graph6.setTitle("Sensor 7");
              graph6.setVisibility(View.VISIBLE);
               graph6.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph6.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph6.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 8){
              graph7 = (GraphView) findViewById(R.id.graph7);
              graph7.setTitle("Sensor 8");
              graph7.setVisibility(View.VISIBLE);
               graph7.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph7.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph7.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 9){
              graph8 = (GraphView) findViewById(R.id.graph8);
              graph8.setTitle("Sensor 9");
              graph8.setVisibility(View.VISIBLE);
               graph8.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph8.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph8.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 10){
              graph9 = (GraphView) findViewById(R.id.graph9);
              graph9.setTitle("Sensor 10");
              graph9.setVisibility(View.VISIBLE);
               graph9.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph9.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph9.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 11){
              graph10 = (GraphView) findViewById(R.id.graph10);
              graph10.setTitle("Sensor 11");
              graph10.setVisibility(View.VISIBLE);
               graph10.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph10.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph10.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 12){
              graph11 = (GraphView) findViewById(R.id.graph11);
              graph11.setTitle("Sensor 12");
              graph11.setVisibility(View.VISIBLE);
               graph11.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph11.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph11.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 13){
              graph12 = (GraphView) findViewById(R.id.graph12);
              graph12.setTitle("Sensor 13");
              graph12.setVisibility(View.VISIBLE);
               graph12.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph12.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph12.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 14){
              graph13 = (GraphView) findViewById(R.id.graph13);
              graph13.setTitle("Sensor 14");
              graph13.setVisibility(View.VISIBLE);
               graph13.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph13.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph13.getViewport().setScrollable(true); // enables horizontal scrolling
           }else if(Integer.parseInt(gettingSen[i].trim()) == 15){
              graph14 = (GraphView) findViewById(R.id.graph14);
              graph14.setTitle("Sensor 15");
              graph14.setVisibility(View.VISIBLE);
               graph14.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph14.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph14.getViewport().setScrollable(true); // enables horizontal scrolling
          }else if(Integer.parseInt(gettingSen[i].trim()) == 16) {
               graph15 = (GraphView) findViewById(R.id.graph15);
               graph15.setTitle("Sensor 16");
               graph15.setVisibility(View.VISIBLE);
               graph15.getGridLabelRenderer().setLabelFormatter(new DateAsXAxisLabelFormatter(this,format));
               graph15.getGridLabelRenderer().setNumHorizontalLabels(4);
               graph15.getViewport().setScrollable(true); // enables horizontal scrolling
           }

       }

    }
    public void onResume() {
        super.onResume();
        autoUpdate = new Timer();
        autoUpdate.schedule(new TimerTask() {
            @Override
            public void run() {
                runOnUiThread(new Runnable() {
                    public void run() {
                        getAMS();
                    }
                });
            }
        }, 0, TIMETOWAIT);
    }

    @Override
    public void onPause() {
        autoUpdate.cancel();
        super.onPause();
    }

    private void getAMS(){

        class GetEmployee extends AsyncTask<Void,Void,String>{
            ProgressDialog loading;

            @Override
            protected void onPreExecute() {
                super.onPreExecute();
               // loading = ProgressDialog.show(Graph.this,"Fetching...","Wait...",false,false);
            }

            @Override
            protected void onPostExecute(String s) {
                super.onPostExecute(s);
                //loading.dismiss();

                int temp = 0;
                for(int j = 0 ; j<gettingSen.length; j++) {
                    temp = Integer.parseInt(gettingSen[j].trim());

                    addtograph(gpt.get(temp-1).getSeries(), gpt.get(temp-1).id);
                }

            }

            @Override
            protected String doInBackground(Void... params) {
                RequestHandler rh = new RequestHandler();
                gpt = rh.sendGetRequestParam(Config.URL_GET,"1",sts);
                return "worked";

            }
        }
        GetEmployee ge = new GetEmployee();
        ge.execute();

    }

    private void addtograph(LineGraphSeries<DataPoint> sr , int id){
        switch (id) {
            case 1:
            graph.addSeries(sr);
                break;
            case 2:
                graph1.addSeries(sr);
                break;
            case 3:
                graph2.addSeries(sr);
                break;
            case 4:
                graph3.addSeries(sr);
                break;
            case 5:
                graph4.addSeries(sr);
                break;
            case 6:
                graph5.addSeries(sr);
                break;
            case 7:
                graph6.addSeries(sr);
                break;
            case 8:
                graph7.addSeries(sr);
                break;
            case 9:
                graph8.addSeries(sr);
                break;
            case 10:
                graph9.addSeries(sr);
                break;
            case 11:
                graph10.addSeries(sr);
                break;
            case 12:
                graph11.addSeries(sr);
                break;
            case 13:
                graph12.addSeries(sr);
                break;
            case 14:
                graph13.addSeries(sr);
                break;
            case 15:
                graph14.addSeries(sr);
                break;
            case 16:
                graph15.addSeries(sr);
                break;
        }
    }
    public SettingsToStore load(){
        SettingsToStore sts = null;
        try {
            String filename = "Data";
            FileInputStream iStream = openFileInput(filename);
            ObjectInputStream ois = new ObjectInputStream(iStream);
            sts = (SettingsToStore) ois.readObject();

            ois.close();
            iStream.close();
        }catch(Exception e1){
            e1.printStackTrace();
        }


        return sts;
    }


}
