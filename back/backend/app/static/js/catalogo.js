$(document).ready(function(){
   show(); 
});

function show(){
    toastr.options = {positionClass:"toast-top-full-width"};
    var btn_text;
    var i = 0;
    $('button').click(function(){
        $('#categoria').hide();
        btn_text = $(this).text().toLowerCase();
        if(!btn_text.startsWith('reserved')){
            var folder = '/getFolder?folder='+btn_text;
        }
        
        var param = getParameterByName('param')
        $.ajax({
            url : folder,
            success: function (data) {
                if(param){
                    //console.log(data);
                    $.each(data,function(){
                        if(data.file == 'Nessun file presente'){
                            toastr.warning('NESSUN FILE PRESENTE');
                        }
                        else{
                            data.file.forEach(function(entry){
                                if( entry.match(/\.(jpe?g|png|gif)$/) ) { 
                                    $('#uno').append("<div id='"+ i++ +"' class='col-md-3 col-xs-6 img-box'> <img src='"+ entry +"' class='img-responsive' id='imgar'><button id='btn-d' onclick='delete_file()'>cancella</button></div>");
                                } 
                            });
                        }
                        //console.log(data.file[0]);
                    });
                }
                else{
                    show_customers(folder);
                }
            }
        });
    });
}

function show_customers(folder){
        $.ajax({
            url : folder,
            success: function (data) {
                $.each(data,function(){
                    if(data.file == 'Nessun file presente'){
                        toastr.warning('NESSUN FILE PRESENTE!');
                    }
                    else{
                        data.file.forEach(function(entry){
                            if( entry.match(/\.(jpe?g|png|gif)$/) ) { 
                                $('#uno').append("<div class='col-md-3 col-xs-6'> <img src='"+ entry +"' class='img-responsive' id='imgar'></div>");
                        } 
                        });
                    }
                    //console.log(data.file[0]);
                });
            }
        });
}

function delete_file(id){
    toastr.options = {positionClass:"toast-top-full-width"};
    var path_to_delete = $('#imgar').attr('src');
    var url = '/deleteFile'
    var data = {'data':path_to_delete}
    $.ajax({
       type:'POST',
       url: url,
       data: data,
       success: function() {
           toastr.success('File eliminato!');
           id = $('.img-box').attr('id');
           $('#' + id).remove();
       },
       error: function() {
           toastr.error('Ops! Qualcosa è andato male :(')
       }
    });
    
}

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}