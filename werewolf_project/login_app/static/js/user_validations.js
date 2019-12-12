$(document).ready(function(){
    $('#emailInput').keyup(function(){
        if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test($('[name="email"]').val() ))) {
            $('#emailMsg').html("<p>Invalid Email Address")
        }
        else{
            var data = $("#registerForm").serialize()
            $.ajax({
                method: "POST",
                url: "/checkEmail",
                data: data
            })
            .done(function(res){
                $('#emailMsg').html(res)
            })
        }
    })
    $('#registerForm').submit(function(){
        errorsFound = false
        errorMsgs = []
        if ($('[name="first_name"]').val().length < 2){
            errorMsgs.push("First Name must be at least 2 characters!")
            errorsFound = true
        }
        if ($('[name="last_name"]').val().length < 2){
            errorMsgs.push("Last Name must be at least 2 characters!")
            errorsFound = true
        }
        if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test($('[name="email"]').val() ))) {
            errorMsgs.push("Email address invalid!")
            errorsFound = true
        }
        if ($('[name=birthday]').val().length == 0) {
            errorMsgs.push("You must enter a birthday!")
            errorsFound = true
        }
        else {
            var dob = $('[name=birthday]').val().split("-");
            var dateDob = new Date(dob[0], parseInt(dob[1])-1, dob[2]);
            var today = new Date();
            var age = today.getFullYear() - dateDob.getFullYear();
            if (age < 13) {
                errorMsgs.push("Sorry, you must be at least 13 years old to register!");
                errorsFound = true;
            }
        }
        if ($('[name=password]').val().length < 8) {
            errorMsgs.push("Your password must be at least 8 characters long");
            errorsFound = true;
        }
        if ($('[name=password]').val() != $('[name=password2]').val()) {
            errorMsgs.push("Your two entered passwords do not match!");
            errorsFound = true;
        }
        if (errorsFound == true) {
            errorHTML = ""
            for (var i=0; i<errorMsgs.length; i++) {
                errorHTML += "<p>" + errorMsgs[i] + "</p>";
            }
            $('.footer').html(errorHTML);
            return false;
        }
        else if (errorsFound == False) {
            $('#registerForm').submit()
        }
    })
})