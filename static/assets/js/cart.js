function jsIncreaseValue(field) {
    nr = parseInt(document.getElementById(field).value);
    document.getElementById(field).value = nr + 1;
   }
    
   function jsDecreaseValue(field) {
       
    nr = parseInt(document.getElementById(field).value);
    
    alert(nr);
    if (nr > 0) {
        alert("nr > 0");
      if( (nr - 1) > 0) {
          alert("nr -1 > 0");
        document.getElementById(field).value = nr - 1;
      }
    }
   } 