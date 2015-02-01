function gplus_login(resp,csrf_token) {
    //console.log("create post is working!") // sanity check
    resp['hidden'] = {"name":"","value":""};

    var split_csrf = csrf_token.split("='");
    var csrf_name = split_csrf[2].replace("' ", '');
    var csrf_value = split_csrf[3].replace("' ", '').replace("/>", '');
    
    // resp['hidden'].name = csrf_name;
    // resp['hidden'].value = csrf_value;

    $.ajax({
        url : "/gplus_login/", // the endpoint
        type : "POST", // http method
        data : { the_post : resp, csrfmiddlewaretoken: csrf_value}, // data sent with the post request



        // handle a successful response
        success : function(json) {
            //$('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            //location.reload(true);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    //console.log(resp);
    //console.log(csrf_token);
    // var split_csrf = csrf_token.split("='");
    // console.log(split_csrf[2].replace("' ", ''));
    // console.log(split_csrf[3].replace("' ", '')); //
};