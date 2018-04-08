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

			$dosars=30; $sandwichrs=30; $samosars=40; $vprs=20; $kachorirs=30; $cbrs=40; $manchurianrs=30; $noodlesrs=30; $ljrs=30; $pjrs=20; $mjrs=20; $ajrs=30;
			$total=$dosars*$dosa + $sandwichrs*$sandwich + $manchurian*$manchurianrs + $noodles*$noodlesrs + $vp*$vprs + $samosa*$samosars + $cb*$cbrs + $kachori*$kachorirs + $pj*$pjrs + $lj*$ljrs + $mj*$mjrs + $ajrs*$aj;


			echo "Your total billing is $total ";

		}

?>