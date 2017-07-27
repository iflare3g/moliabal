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

<div class="container-fluid">
    <div class="row">
      
      <div id="spazio">
      
      <div class="col-md-6 col-xs-offset-5 col-xs-12">
          <img src="img/loginimg.png" class="img-responsive" style="height:350px; margin-top:77px;">
      </div>
       
       <div class="col-md-3 col-xs-12 form">
        
        <h2 id="titololog">LOG IN</h2>
        
        <form action="">
         
         <div class="input-container">
          
          <input id="input" type="email" placeholder="email" name="email">
          <input id="input" type="password" placeholder="password" name="password">
           
         </div>
   
          <a><button id="btn-e">ENTER</button></a>
        
        </form>
    
       </div>
       </div>
    </div>
</div>

<?php include("footer.php") ?>

</body>
</html>