package co.brewscience.automationstation;

/**
 * Created by andrew on 5/15/17.
 */

public class Config {
    //Address of our scripts of the CRUD
    public static final String URL_ADD="http://automateuw.pe.hu/automationstation/addOBJ.php";
    public static final String URL_GET = "http://automateuw.pe.hu/automationstation/getOBJ.php?id=";

    //Keys that will be used to send the request to php scripts
    public static final String KEY_AMS_DARRAY = "dataarray";
    public static final String KEY_AMS_ID = "id";


    //JSON Tags
    public static final String TAG_JSON_ARRAY="result";
    public static final String TAG_ID = "id";
    public static final String TAG_NAME = "dataarray";

    //ams id to pass with intent
    public static final String AMS_ID = "AMS_id";
}
