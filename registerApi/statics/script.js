var sel = document.getElementById("age");
    const tempOption = document.createElement("option");
    sel[0] = new Option( 'AGE');
    for(var i = 18;i<=65;i++){
        sel[i-18+1] = new Option( i,i);	
    }
    document.body.appendChild(tempOption);