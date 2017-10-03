<?php 
 
 //Getting the requested id
 $id = $_GET['id'];
 
 //Importing database
 require_once('amsConnect.php');
 
 //Creating sql query with where clause to get an specific employee
 $sql = "SELECT dataarray FROM amstation";
 //WHERE id=$id";
 
 //getting result 
 $r = mysqli_query($con,$sql);
 
 //pushing result to an array 
 
 while ($row = mysqli_fetch_assoc($r)){
	
	echo $row['dataarray']."\r\n";
	//foreach($row as $field){
	//	 echo '{' .$field. '}';
	//}
	

	}

 //displaying in json format 
 //echo $row['dataarray'];
//json_encode(array('result'=>$result));
 
 mysqli_close($con);
