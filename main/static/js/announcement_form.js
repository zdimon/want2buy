$( document ).ready(function() {
    
    

    $.getJSON( "/api/regions", function( data ) {
        var regions = data;
       
        $('#id_region').on('change', function() {
          
            var arrayLength = regions.length;
            for (var i = 0; i < arrayLength; i++) {
                if(parseInt(this.value)==parseInt(regions[i].id)){
                    $('#id_city').empty();
                    for (var ii = 0; ii < regions[i].cities.length; ii++) {
                        $('#id_city').append('<option value="'+regions[i].cities[ii].id+'">'+regions[i].cities[ii].name+'</option>');
                    }
                    $("#id_city").chosen("destroy");   
                    $("#id_city").chosen(); 

                }
                
            } 
          });

        
    })  
    .fail(function() {
        console.log( "error in geting /api/regions" );
     });

  
     $.getJSON( "/api/categories", function( data ) {
        var categories = data;
        console.log(categories);

        $('#id_category').on('change', function() {
            $('#id_sub_sub_category').empty();
            $("#id_sub_category").chosen("destroy");   
            $("#id_sub_category").chosen();             
            var arrayLength = categories.length;
            for (var i = 0; i < arrayLength; i++) {
                if(parseInt(this.value)==parseInt(categories[i].id)){
                    $('#id_sub_category').empty();
                   
                    for (var ii = 0; ii < categories[i].sub_category.length; ii++) {
                        $('#id_sub_category').append('<option value="'+categories[i].sub_category[ii].id+'">'+categories[i].sub_category[ii].name+'</option>');
                    }
                    $("#id_sub_category").chosen("destroy");   
                    $("#id_sub_category").chosen(); 
                    

                    if(categories[i].sub_category.length==0){
                        $('#id_sub_sub_category').append('<option value="">----</option>');         $('#id_sub_category').append('<option value="">----</option>'); 
                        $("#id_sub_category").chosen("destroy");   
                        $("#id_sub_category").chosen();
                        $("#id_sub_sub_category").chosen("destroy");   
                        $("#id_sub_sub_category").chosen();                        
                        
                    } else {
                        setSubSubCategory( categories[i].sub_category[0]); 
                    }

                }
                
            } 
          });



          function setSubSubCategory(sub_c){
            $('#id_sub_sub_category').empty();
            $("#id_sub_sub_category").chosen("destroy");   
            $("#id_sub_sub_category").chosen(); 
            
            for (var iii = 0; iii < sub_c.sub_category.length; iii++) {
                $('#id_sub_sub_category').append('<option value="'+sub_c.sub_category[iii].id+'">'+sub_c.sub_category[iii].name+'</option>');
            }
            if(sub_c.sub_category.length==0){
                $('#id_sub_sub_category').append('<option value="">----</option>');                
            }
            $("#id_sub_sub_category").chosen("destroy");   
            $("#id_sub_sub_category").chosen();             

         };


          $('#id_sub_category').on('change', function() {
            
            var arrayLength = categories.length;
            for (var i = 0; i < arrayLength; i++) {
                for (var ii = 0; ii < categories[i].sub_category.length; ii++) {
                    if(parseInt(this.value)==parseInt(categories[i].sub_category[ii].id)){
                        setSubSubCategory(categories[i].sub_category[ii]);                       
                    }
                }
                
            } 
          });          


     })
     .fail(function() {
        console.log( "error" );
     });   


});