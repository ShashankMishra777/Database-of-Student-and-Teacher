$(document).ready(function() {

                 $('.error').hide();
                 $(".alpha").click(function() {
                     var Name = document.forms["RegForm"]["Name"];    
    var HOD = document.forms["RegForm"]["HOD"];               
    var Department = document.forms["RegForm"]["Department"];  
     if (Name.value == "")                                  
    { 
        window.alert("Please enter teacher's name."); 
        Name.focus(); 
        return false; 
    }

    if (HOD.value == "")                                  
    { 
        window.alert("Please enter your if the teacher is HOD."); 
        HOD.focus(); 
        return false; 
    } 
       if (Department.value == "")                                   
    { 
        window.alert("Please enter the Department "); 
        Department.focus(); 
        return false; 
    }   
    
    $.ajax({                                   
 
   
                     data:{
                        Name:$('#11').val(),
                        HOD:$('#21').val(),
                        Department:$('#31').val()
                     },
                     type: "POST",
                     url: "/tadd",
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
