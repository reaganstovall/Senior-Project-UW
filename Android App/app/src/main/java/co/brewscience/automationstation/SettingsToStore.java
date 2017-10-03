package co.brewscience.automationstation;

import java.io.Serializable;
import java.util.Date;

/**
 * Created by andrew on 5/25/17.
 */

public class SettingsToStore implements Serializable {

    public long startdate = 0;
    public long enddate = 0;
    public long starttime = 0;
    public long endtime = 0;
    public int unitstouse = 0;
    public boolean checkboxdate = false;
    public boolean checkboxtime = false;
    public int starthour = 0;
    public int startmin = 0;
    public int endhour = 0;
    public int endmin = 0;

    public void setValues(long sd,long ed, long st, long et, int utu, boolean cbd, boolean cbt){
        startdate = sd;
        enddate = ed;
        starttime = st;
        endtime = et;
        unitstouse = utu;
        checkboxdate = cbd;
        checkboxtime = cbt;

    }
    public boolean isCheckboxtime() {
        return checkboxtime;
    }

    public void setCheckboxtime(boolean checkboxtime) {
        this.checkboxtime = checkboxtime;
    }

    public boolean isCheckboxdate() {
        return checkboxdate;
    }

    public void setCheckboxdate(boolean checkboxdate) {
        this.checkboxdate = checkboxdate;
    }

    public long getStartdate() {
        return startdate;
    }

    public void setStartdate(long startdate) {
        this.startdate = startdate;
    }

    public long getEnddate() {
        return enddate;
    }

    public void setEnddate(long enddate) {
        this.enddate = enddate;
    }

    public long getStarttime() {
        return starttime;
    }

    public void setStarttime(long starttime) {
        this.starttime = starttime;

    }

    public long getEndtime() {
        return endtime;
    }

    public void setEndtime(long endtime) {
        this.endtime = endtime;

    }

    public int getUnitstouse() {
        return unitstouse;
    }

    public void setUnitstouse(int unitstouse) {
        this.unitstouse = unitstouse;
    }


}
