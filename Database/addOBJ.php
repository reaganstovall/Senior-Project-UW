<?php 
	if($_SERVER['REQUEST_METHOD']=='POST'){
		
		//Getting values
		$arraydata = $_POST['dataarray'];
		
		
		//Creating an sql query
		$sql = "INSERT INTO amstation (dataarray) VALUES ('$arraydata')";
		
		//Importing our db connection script
		require_once('amsConnect.php');
		
		//Executing query to database
		if(mysqli_query($con,$sql)){
			echo 'Data Added Successfully';
		}else{
			echo 'Could Not Add Data';
		}
		
		//Closing the database 
		mysqli_close($con);
	}
