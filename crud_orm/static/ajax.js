$(document).ready(function() {

                 $('.error').hide();
                 $(".alpha").click(function() {
                     var Name = document.forms["RegForm"]["Name"];    
    var Monitor = document.forms["RegForm"]["Monitor"];               
    var Subjects = document.forms["RegForm"]["Subjects"];  
     if (Name.value == "")                                  
    { 
        window.alert("Please enter student's name."); 
        Name.focus(); 
        return false; 
    }

    if (Monitor.value == "")                                  
    { 
        window.alert("Please enter your if the student is monitor."); 
        Monitor.focus(); 
        return false; 
    } 
       if (Subjects.value == "")                                   
    { 
        window.alert("Please enter the subjects "); 
        Subjects.focus(); 
        return false; 
    }   
    
    $.ajax({                                   
 
   
                     data:{
                        Name:$('#1').val(),
                        Monitor:$('#2').val(),
                        Subjects:$('#3').val(),
                     },
                     type: "POST",
                     url: "/add",
                     success: function(result)
                     {
                        
                        console.log(result);
                        location.reload();
                        window.alert('User added successfully');
                     }
                
                   });

            return false;                     
            });
   

    });
