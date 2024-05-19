// Code taken from ajaxcalls.js by Andrew Beatty 
 
    function getAll(callback){
        $.ajax({
            "url": "http://127.0.0.1:5000/fruits",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                //console.log(result);
                callback(result)
     
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }

    // testing code
    function createFruit(fruit, callback){
        console.log(JSON.stringify(fruit));
        $.ajax({
            "url": "http://127.0.0.1:5000/fruits",
            "method":"POST",
            "data":JSON.stringify(fruit),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }
    function updateFruit(fruit, callback){
        console.log("updateing " +JSON.stringify(fruit));
        $.ajax({
            "url": "http://127.0.0.1:5000/fruits/"+encodeURI(fruit.id),
            "method":"PUT",
            "data":JSON.stringify(fruit),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)   
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    function deleteFruit(id, callback){
        $.ajax({
            "url": "http://127.0.0.1:5000/fruits/"+id,
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }



    // testing code
    
    function processGetAllResponse(result){
        console.log("in process")
        //console.log(result)
        for (fruit of result){
            displayFruit = {}
            displayFruit.id = fruit.id
            displayFruit.name = fruit.Name
            displayFruit.country_of_origin = fruit.Country_of_origin
            displayFruit.price = fruit.Price
            // you can now pass it to addfruitToTable
            console.log(displayfruit)
        }
    }
     getAll(processGetAllResponse)

     ///// Create
    function processCreateResponse(result){
        console.log(result)
    }

    //// update
    function processUpdateResponse(result){
        console.log(result)
    }
    fruit = {id:155,"Price":999} 
    
    ////delete
    
    function processDeleteResponse(result){
        console.log("in process delete")
        console.log(result)
    } 