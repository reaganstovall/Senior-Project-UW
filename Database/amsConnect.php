<?php

/* author: Andrew Klonitsko

 HOST is mysql.hostinger.in
 USER u750059057_peeps
 PASSWORD Klonitsko1
 DATABASE u750059057_ams

*/


//Defining Constants
 define('HOST','mysql.hostinger.in');
 define('USER','u750059057_peeps');
 define('PASS','Klonitsko1');
 define('DB','u750059057_ams');


//Connecting to the Database
$con = mysqli_connect(HOST,USER,PASS,DB) or die('Unable to Connect');
