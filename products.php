<!doctype html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    
</head>
<body>

<nav class="menu">
 
  <a href="index.html"><img src="img/logo.png" class="img-responsive" id="logo"></a>
  
  <input type="checkbox" id="nav" /><label for="nav"></label>
   
   <ul class="voci">
       <a class="voce" href="home.php"><li>HOME</li></a>
       <a class="voce" href="about.php"><li>ABOUT</li></a>
       <a class="voce" href="location.php"><li>LOCATION</li></a>
       <a class="voce" href="products.php"><li>PRODUCTS</li></a>
       <a class="voce" href="contact.php"><li>CONTACT</li></a>
       <a class="voce" href="area.php"><li>RESERVED AREA</li></a>
   </ul>
    
</nav>

<?php include("products_galleria.php") ?>

<?php include("footer.php"); ?>

</body>
</html>