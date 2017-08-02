/*global $*/
$(document).ready(function(){
    post();
});


function post(){
    toastr.options = {positionClass:"toast-top-full-width"};
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
                toastr.success('File Uploaded!');
                //$.LoadingOverlay('hide');
                $('#progress').attr('aria-valuenow',0).css('width',0 + '%').text(0 + '%');
                clearInput();

            },
            error: function(xhr,status,error){
                if(xhr.status == '413'){
                    //$.LoadingOverlay("hide");
                    toastr.error('FILE TOO LARGE PLEASE UPLOAD ONE SMALLER THAN 10MB');
                    $('#progress').attr('aria-valuenow',0).css('width',0 + '%').text(0 + '%');
                    clearInput();


                }
            },
            
            statusCode:{
                500:function(){
                    //$.LoadingOverlay('hide');
                    toastr.error('FILE EXTENSION NOT ALLOWED');
                    $('#progress').attr('aria-valuenow',0).css('width',0 + '%').text(0 + '%');
                    clearInput();
                }
            }
            
        }); 
    });
}

function clearInput(){
    $('input[type=file]').val('');

}