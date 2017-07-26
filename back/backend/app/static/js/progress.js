/*global $*/
$(document).ready(function(){
    post();
});


function post(){
    $('form').submit(function(event){
        event.preventDefault();
        //$.LoadingOverlay('show');
        $.ajax({
            xhr:function(){
              var xhr = new window.XMLHttpRequest();
              xhr.upload.addEventListener('progress',function(e){
                  if(e.lengthComputable){
                      var percent = Math.round((e.loaded/e.total) * 100);
                      $('#progress').attr('aria-valuenow',percent).css('width',percent + '%').text(percent + '%');
                  }
                  
              }); 
              
            return xhr;
            },
            type:'POST',
            url:'/upload',
            data:new FormData(this),
            processData : false,
            contentType : false,
            
            success : function(){
                alert('File uploaded!');
                //$.LoadingOverlay('hide');
                $('#progress').attr('aria-valuenow',0).css('width',0 + '%').text(0 + '%');
                clearInput();

            },
            error: function(xhr,status,error){
                if(xhr.status == '413'){
                    //$.LoadingOverlay("hide");
                    alert('FILE TOO LARGE PLEASE UPLOAD ONE SMALLER THAN 10MB');
                    $('#progress').attr('aria-valuenow',0).css('width',0 + '%').text(0 + '%');
                    $('input[type=file]').val('');


                }
            },
            
            statusCode:{
                500:function(){
                    //$.LoadingOverlay('hide');
                    alert('file not allowed');
                    $('#progress').attr('aria-valuenow',0).css('width',0 + '%').text(0 + '%');
                    clearInput();
                }
            }
            
        }); 
    });
}

function clearInput(){
    $('input[type=file]').val('');
    $('input[type=text]').val('');

}