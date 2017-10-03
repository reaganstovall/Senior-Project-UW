package co.brewscience.automationstation;

import android.util.Log;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import javax.net.ssl.HttpsURLConnection;

import static co.brewscience.automationstation.Config.KEY_AMS_DARRAY;
import static co.brewscience.automationstation.Config.KEY_AMS_ID;

/**
 * Created by andrew on 5/15/17.
 */

public class RequestHandler {


    //Method to send httpPostRequest
    //This method is taking two arguments
    //First argument is the URL of the script to which we will send the request
    //Other is an HashMap with name value pairs containing the data to be send with the request
    public String sendPostRequest(String requestURL,
                                  HashMap<String, String[]> postDataParams) {
        //Creating a URL
        URL url;

        String stringtosend = null;
        int first = 0;
        for(int i = 0 ; i < postDataParams.get(KEY_AMS_DARRAY).length; i++){
            if(first == 0){
                stringtosend = postDataParams.get(KEY_AMS_DARRAY)[i];
                first++;
            }else {
                stringtosend +=","+postDataParams.get(KEY_AMS_DARRAY)[i];
            }
        }
        //StringBuilder object to store the message retrieved from the server
        StringBuilder sb = new StringBuilder();
        try {
            //Initializing Url
            url = new URL(requestURL);

            //Creating an httmlurl connection
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            //Configuring connection properties
            conn.setReadTimeout(15000);
            conn.setRequestMethod("POST");

            conn.setDoInput(true);
            conn.setDoOutput(true);

            OutputStream os = conn.getOutputStream();
            //Creating an output stream


            BufferedWriter writer = new BufferedWriter(
                    new OutputStreamWriter(os, "UTF-8"));

            writer.write(KEY_AMS_DARRAY + "="+ stringtosend);

            writer.flush();
            writer.close();
            os.close();

            int responseCode = conn.getResponseCode();

            if (responseCode == HttpsURLConnection.HTTP_OK) {

                BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                sb = new StringBuilder();
                String response;
                //Reading server response
                while ((response = br.readLine()) != null) {
                    sb.append(response);
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
        return sb.toString();
    }
    //This returns an arraylist of the class Graphpoint, this gets data from the db and formats it in a way to
    // make it easy to work with. It goes though each row and gets all the values. it then goes though
    //each of those sets adds them to the corresponding class and sets the time for the data.
    public ArrayList<Graphpointsandtime> sendGetRequestParam(String requestURL, String id, SettingsToStore sts){
        StringBuilder sb =new StringBuilder();
        List<String> sarray = new ArrayList<>() ;
        ArrayList<Graphpointsandtime> gpat = null;

        try {
            URL url;
            url = new URL(requestURL );
                HttpURLConnection con = (HttpURLConnection) url.openConnection();

                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(con.getInputStream()));
                String s;

                while ((s = bufferedReader.readLine()) != null) {
                    sarray.add(s);
                }


                gpat = setupGraphpointandTime(sarray,sts);
            Log.d("HERE", "sendGetRequestParam: " + gpat.size());


        }catch(Exception e){
            //Log.d("HERE", "sendGetRequestParam: " + "here");
        }

        return gpat;
    }

    private ArrayList<Graphpointsandtime> setupGraphpointandTime(List<String> sarray, SettingsToStore s2s) {
        ArrayList<Graphpointsandtime> gpt = new ArrayList<>();
        String[] splitstr;
        Graphpointsandtime graph1 = new Graphpointsandtime(1,s2s);
        Graphpointsandtime graph2 = new Graphpointsandtime(2,s2s);
        Graphpointsandtime graph3 = new Graphpointsandtime(3,s2s);
        Graphpointsandtime graph4 = new Graphpointsandtime(4,s2s);
        Graphpointsandtime graph5 = new Graphpointsandtime(5,s2s);
        Graphpointsandtime graph6 = new Graphpointsandtime(6,s2s);
        Graphpointsandtime graph7 = new Graphpointsandtime(7,s2s);
        Graphpointsandtime graph8 = new Graphpointsandtime(8,s2s);
        Graphpointsandtime graph9 = new Graphpointsandtime(9,s2s);
        Graphpointsandtime graph10 = new Graphpointsandtime(10,s2s);
        Graphpointsandtime graph11 = new Graphpointsandtime(11,s2s);
        Graphpointsandtime graph12 = new Graphpointsandtime(12,s2s);
        Graphpointsandtime graph13 = new Graphpointsandtime(13,s2s);
        Graphpointsandtime graph14 = new Graphpointsandtime(14,s2s);
        Graphpointsandtime graph15 = new Graphpointsandtime(15,s2s);
        Graphpointsandtime graph16 = new Graphpointsandtime(16,s2s);

        for(int j = 0 ; j < sarray.size(); j ++){

            splitstr = sarray.get(j).split(",");

            try{
                for(int k = 0; k< splitstr.length; k++){

                    switch (k){
                        case 0:
                            graph1.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 1:
                            graph2.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 2:
                            graph3.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 3:
                            graph4.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 4:
                            graph5.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 5:
                            graph6.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 6:
                            graph7.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 7:
                            graph8.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 8:
                            graph9.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 9:
                            graph10.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 10:
                            graph11.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 11:
                            graph12.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 12:
                            graph13.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 13:
                            graph14.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 14:
                            graph15.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;
                        case 15:
                            graph16.setValueandTime(Double.parseDouble(splitstr[k]),splitstr[splitstr.length-1]);
                            break;

                    }

                }


            }catch(Exception e){


            }




        }

        gpt.add(graph1);
        gpt.add(graph2);
        gpt.add(graph3);
        gpt.add(graph4);
        gpt.add(graph5);
        gpt.add(graph6);
        gpt.add(graph7);
        gpt.add(graph8);
        gpt.add(graph9);
        gpt.add(graph10);
        gpt.add(graph11);
        gpt.add(graph12);
        gpt.add(graph13);
        gpt.add(graph14);
        gpt.add(graph15);
        gpt.add(graph16);

        return gpt;
    }

}