package co.brewscience.automationstation;

import android.app.DatePickerDialog;
import android.app.TimePickerDialog;
import android.content.Context;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.InputType;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TimePicker;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Locale;

/**
 * Created by andrew on 4/23/17.
 */

public class Settings extends AppCompatActivity implements View.OnClickListener{
    private EditText fromDateEtxt;
    private EditText toDateEtxt;
    private EditText startTime;
    private EditText endTime;
    private CheckBox endDatecb;
    private CheckBox endTimecb;
    private Button save;
    SettingsToStore sts;

    Calendar myCalendar = Calendar.getInstance();
    Calendar endCalendar = Calendar.getInstance();
    Calendar startTimeCalendar = Calendar.getInstance();
    Calendar endTimeCalendar = Calendar.getInstance();

    TimePickerDialog.OnTimeSetListener sTimePicker,eTimePicker;
    DatePickerDialog.OnDateSetListener startdate, enddate;

    Spinner unitstouse;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.settings);

        sts = load();

        if(sts == null){
            sts = new SettingsToStore();
        }

        fromDateEtxt = (EditText) findViewById(R.id.editText_startdate);
        toDateEtxt = (EditText) findViewById(R.id.editText_endDate);
        startTime = (EditText) findViewById(R.id.editText_starttime);
        endTime = (EditText) findViewById(R.id.editText_endTime);
        unitstouse = (Spinner) findViewById(R.id.mySpinner1);
        endDatecb = (CheckBox) findViewById(R.id.cbEndDate);
        endTimecb = (CheckBox) findViewById(R.id.cbCurrentTime);
        save = (Button) findViewById(R.id.buttonSave);

        fromDateEtxt.setInputType(InputType.TYPE_NULL);
        toDateEtxt.setInputType(InputType.TYPE_NULL);
        startTime.setInputType(InputType.TYPE_NULL);
        endTime.setInputType(InputType.TYPE_NULL);

        fromDateEtxt.setOnClickListener(this);
        toDateEtxt.setOnClickListener(this);
        startTime.setOnClickListener(this);
        endTime.setOnClickListener(this);
        save.setOnClickListener(this);

if(sts != null) {
    if (sts.getStartdate() > 0) {
        String myFormat = "MM/dd/yy"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);
        fromDateEtxt.setText(sdf.format(sts.getStartdate()));

    }
    if (sts.getEnddate() > 0) {
        String myFormat = "MM/dd/yy"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);
        toDateEtxt.setText(sdf.format(sts.getEnddate()));
    }
    if (sts.getStarttime() > 0) {
        String myFormat = "HH:mm"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);
        startTime.setText(sdf.format(sts.getStarttime()));
    }
    if (sts.getEndtime() > 0) {
        String myFormat = "HH:mm"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);
        endTime.setText(sdf.format(sts.getEndtime()));
    }


    if (sts.checkboxtime) {
        endTimecb.setChecked(true);

    }
    if (sts.checkboxdate) {
        endDatecb.setChecked(true);

    }
}

        sTimePicker = new TimePickerDialog.OnTimeSetListener(){
            @Override
            public void onTimeSet(TimePicker timePicker, int hour, int min) {
                startTimeCalendar.set(Calendar.HOUR, hour);
                startTimeCalendar.set(Calendar.MINUTE, min);
                updateStartTime();
            }
        };
        eTimePicker = new TimePickerDialog.OnTimeSetListener(){
            @Override
            public void onTimeSet(TimePicker timePicker, int hour, int min) {
                endTimeCalendar.set(Calendar.HOUR, hour);
                endTimeCalendar.set(Calendar.MINUTE, min);
                updateEndTime();
            }
        };

        startdate = new DatePickerDialog.OnDateSetListener( ){
        @Override
        public void onDateSet(DatePicker view, int year, int monthOfYear,
        int dayOfMonth) {
            // TODO Auto-generated method stub
            myCalendar.set(Calendar.YEAR, year);
            myCalendar.set(Calendar.MONTH, monthOfYear);
            myCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
            updateStartDate();
        }
        };
        enddate = new DatePickerDialog.OnDateSetListener( ){
            @Override
            public void onDateSet(DatePicker view, int year, int monthOfYear,
                                  int dayOfMonth) {
                // TODO Auto-generated method stub
                endCalendar.set(Calendar.YEAR, year);
                endCalendar.set(Calendar.MONTH, monthOfYear);
                endCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth);
                updateEndDate();
            }

        };

    }

    @Override
    public void onClick(View view) {
    if(view == fromDateEtxt){
        new DatePickerDialog(Settings.this, startdate, myCalendar
                .get(Calendar.YEAR), myCalendar.get(Calendar.MONTH),
                myCalendar.get(Calendar.DAY_OF_MONTH)).show();

    } else if(view == toDateEtxt){
        new DatePickerDialog(Settings.this, enddate, endCalendar
                .get(Calendar.YEAR), endCalendar.get(Calendar.MONTH),
                endCalendar.get(Calendar.DAY_OF_MONTH)).show();

    }else if(view == startTime){
        new TimePickerDialog(Settings.this, sTimePicker, startTimeCalendar
                .get(Calendar.HOUR), startTimeCalendar.get(Calendar.MINUTE),false
                ).show();

    }else if(view == endTime){
        new TimePickerDialog(Settings.this, eTimePicker, endTimeCalendar
                .get(Calendar.HOUR), endTimeCalendar.get(Calendar.MINUTE),false
        ).show();
    }else if(view == save){
        //TODO need to add error checking so times are always right


        try{

            sts.setCheckboxdate(endDatecb.isChecked());
            sts.setCheckboxtime(endTimecb.isChecked());
            //sts.setUnitstouse(unitstouse.getSelectedItemPosition());

        }catch(Exception e){


        }

      if(sts.getStartdate()< sts.getEnddate()) {
          save(sts);
          finish();
      }


    }
    }
    private void updateStartDate() {

        String myFormat = "MM/dd/yy"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);

        sts.setStartdate(myCalendar.getTimeInMillis());
        fromDateEtxt.setText(sdf.format(myCalendar.getTime()));
        Log.d("Time", "setValueandTime: "+ "calculated date:"+ myCalendar.getTimeInMillis());

    }
    private void updateEndDate(){
        String myFormat = "MM/dd/yy"; //In which you need put here
        SimpleDateFormat sdf = new SimpleDateFormat(myFormat, Locale.US);
        sts.setEnddate(endCalendar.getTimeInMillis());
        toDateEtxt.setText(sdf.format(endCalendar.getTime()));
        Log.d("Time", "setValueandTime: "+ "calculated date:"+ endCalendar.getTimeInMillis());

    }
    private void updateStartTime(){
        String myFormat = "HH:mm"; //In which you need put here
        SimpleDateFormat sedf = new SimpleDateFormat(myFormat, Locale.US);
        sts.setStarttime(startTimeCalendar.getTimeInMillis());
        startTime.setText(sedf.format(startTimeCalendar.getTime()));

    }
    private void updateEndTime(){
        String myFormat = "HH:mm"; //In which you need put here
        SimpleDateFormat sodf = new SimpleDateFormat(myFormat, Locale.US);
        sts.setEndtime(endTimeCalendar.getTimeInMillis());
        endTime.setText(sodf.format(endTimeCalendar.getTime()));

    }
    public void save(SettingsToStore sts){

        String filename = "Data";
        FileOutputStream outputStream = null;


        try {

            outputStream = openFileOutput(filename,Context.MODE_PRIVATE);
            //openFileOutput(filename, Context.MODE_PRIVATE);
            ObjectOutputStream out = new ObjectOutputStream(outputStream);
            out.writeObject(sts);
            out.close();
            outputStream.close();

        } catch (Exception e) {
            e.printStackTrace();
            Log.d("here", "IT failed");
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
