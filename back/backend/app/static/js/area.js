function crypt(){
  
        var pwd = document.getElementById('password');
        var pwd_len = pwd.value.length;
        var pass = md5(pwd.value);
        var passString = pass.toString().substring(0,pwd_len);
        pwd.value = passString;

}

