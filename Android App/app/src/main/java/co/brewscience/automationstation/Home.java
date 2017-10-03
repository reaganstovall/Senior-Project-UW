package co.brewscience.automationstation;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.view.View;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.sql.Connection;
import java.util.ArrayList;



public class Home extends AppCompatActivity implements View.OnClickListener{

    final String[] sensors = {
            "1", "2", "3", "4", "5",
            "6", "7","8", "9", "10", "11", "12",
            "13", "14", "15", "16"};
    final String[] motors = {
            "test-one", "two", "three", "four", "five",
            "six", "seven","one", "two", "three", "four", "five",
            "six", "seven"};
    Button graphBtn,livegraphBtn,settingBtn,exitBtn;
    MultiSpinner sensorspinner;
    MultiSpinner motorspinner;
    static Connection mConnection;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);



        setupcomp();
        sensorspinner.setItems(sensors);
        sensorspinner.setSelection(0);
        motorspinner.setItems(motors);


    }

    // This method sets up all button and listviews that are used
    public void setupcomp(){



        sensorspinner = (MultiSpinner) findViewById(R.id.mySpinner1);
        motorspinner = (MultiSpinner) findViewById(R.id.mySpinner2);

        graphBtn = (Button) findViewById(R.id.graphBtn);
        livegraphBtn = (Button) findViewById(R.id.liveGraphBtn);
        settingBtn = (Button) findViewById(R.id.settingBtn);
        exitBtn = (Button) findViewById(R.id.stopBtn);

        graphBtn.setOnClickListener(this);
        livegraphBtn.setOnClickListener(this);
        settingBtn.setOnClickListener(this);
        exitBtn.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {

        switch(view.getId()) {
            case R.id.settingBtn:
                Intent i = new Intent(this, Settings.class);

                startActivity(i);
                break;
            case R.id.graphBtn:
                Intent v = new Intent(view.getContext(), Graph.class);

                if(!sensorspinner.getSelectedStrings().isEmpty()) {
                    v.putExtra("SENSOR", sensorspinner.getSelectedItemsAsString());
                    this.startActivity(v);
                }else{

                    Toast toast = Toast.makeText(this, "Must Select At Least One Sensor", Toast.LENGTH_SHORT);
                    toast.show();
                }

                break;
            case R.id.liveGraphBtn:




                break;
            case R.id.stopBtn:



                break;
        }

    }
}
