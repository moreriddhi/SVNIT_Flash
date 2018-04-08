<?php
session_start();
$con=mysqli_connect("127.0.0.1","root","")or
    die("Could not connect: " . mysql_error());
    mysqli_select_db($con,"order")or
        die("Could not select db: " . mysql_error());


        $dosa=$_POST['dosa'];
		$manchurian=$_POST['manchurian'];
		$noodles=$_POST['noodles'];
		$vp=$_POST['vp'];
		$samosa=$_POST['samosa'];
		$cb=$_POST['cb'];
		$sandwich=$_POST['sandwich'];
		$kachori=$_POST['kachori'];
		$pj=$_POST['pj'];
		$lj=$_POST['lj'];
		$mj=$_POST['mj'];
		$aj=$_POST['aj'];

		$qry = "INSERT INTO `food`(dosa,sandwich,samosa,vadapav,kachori,cholebhature,manchurian,noodles,lemonjuice,pineapplejuice,mangojuice,applejuice) VALUES($dosa,$manchurian,$noodles,$vp,$samosa,$cb,$sandwich,$kachori,$pj,$lj,$mj,$aj)";
		if(mysqli_query($con,$qry))
		{
			echo "Submitted !";
			//header("Location:background.php");

		}

?>