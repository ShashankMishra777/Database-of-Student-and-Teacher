$(document).ready(function() {

                 $('.error').hide();
                 $(".alpha").click(function() {
                     var Class_Name = document.forms["RegForm"]["Class_Name"];    
    var Is_Monitor = document.forms["RegForm"]["Is_Monitor"];               
    var Studying_Subjects = document.forms["RegForm"]["Studying_Subjects"];    
    
    $.ajax({                                   
 
   
                     data:{
                        Class_Name:$('#1').val(),
                        Is_Monitor:$('#2').val(),
                        Studying_Subjects:$('#3').val(),
                     },
                     type: "POST",
                     url: "/add",
                     success: function(result)
                     {
                        
                        console.log(result);
                        location.reload();
                        window.alert(result);
                     }
                
                   });
            return false;                     
            });
   

    });
