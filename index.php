<?php

$host = 'localhost';
$user = 'root';
$pass = 'P@$$06281a';

$conn = new mysqli($host, $user, $pass);

if ($conn->connect_error){
  die('connection failed: ' . $conn->connect_error);
}
echo 'connected sucessfully!';
$query = 'SELECT * FROM' . $ticker;
$result = $conn->query($query);

if ($result->num_rows > 0){
while($row = $result->fetch_assoc()){
  //This is where we format the data pulled from the database
  //so that it displays everything we want it to display in the
  //form of useful information
  echo '' . $row['']
}else{
  echo '0 results';
}

}
$conn->close();
?>
