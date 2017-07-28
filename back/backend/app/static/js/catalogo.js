$(document).ready(function(){
   show(); 
});

function show(){
     var folder = "/getFolder";

        $.ajax({
            url : folder,
            success: function (data) {
                //console.log(data);
                $.each(data,function(){
                    data.file.forEach(function(entry){
                        if( entry.match(/\.(jpe?g|png|gif)$/) ) { 
                            $("#uno").append( "<div class='col-xs-3'> <img src='"+ entry +"' class='img-responsive' id='imgar'></div>" );
                    } 
                    });
                    //console.log(data.file[0]);
                });
            }
        });
}