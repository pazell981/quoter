$(document).ready(function(){
	$("#form_success, #form_failure").hide();
	$("#add_quote").submit(function() {
	    $.post($(this).attr("action"), $(this).serialize(), function(e) {
	        if (e.status == "success") {
	            $("#form_success").fadeIn();
	            var wRand = Math.random();
	            var widthClass = wRand > 0.8 ? 'w5' : wRand > 0.6 ? 'w4' : wRand > 0.4 ? 'w3' : wRand > 0.2 ? 'w2' : 'w1';
	            var elements = $("<div class='item " + widthClass + "'><blockquote>" + e.quote + "<cite>" + e.first_name + " " + e.last_name + "</cite></blockquote></div>");
	            console.log(elements);
	            $("#quotes_block").append(elements)
	            $("#quotes_block").masonry( 'appended', elements )
	        } else if (e.status == "failure") {
	            $("#form_failure").fadeIn();
	        }
	    }, "json");
	    $("input[type=text]").val("");
	    $("textarea").val("");
	    setTimeout(function() { 
	    	$("#form_success, #form_failure").fadeOut(); 
	    }, 5000);
	    return false;
	});
    if (window.location != window.parent.location){
        setTimeout(function(){
        	$("#login_form input[name='username']").val('u')
        }, 100)
        setTimeout(function(){
        	$("#login_form input[name='username']").val('us')
        }, 200)
        setTimeout(function(){
        	$("#login_form input[name='username']").val('use')
        }, 300)
        setTimeout(function(){
        	$("#login_form input[name='username']").val('user')
        }, 400)
        setTimeout(function(){
        	$("#login_form input[name='password']").val('J')
        }, 500)
        setTimeout(function(){
        	$("#login_form input[name='password']").val('Ja')
        }, 600)
        setTimeout(function(){
        	$("#login_form input[name='password']").val('JaV')
        }, 700)
        setTimeout(function(){
        	$("#login_form input[name='password']").val('JaVa')
        }, 800)
        setTimeout(function(){
        	$("#login_form input[name='password']").val('JaVa9')
        }, 900)
        setTimeout(function(){
        	$("#login_form input[name='password']").val('JaVa98')
        }, 1000)
        setTimeout(function(){
        	$("#login_form input[name='password']").val('JaVa981')
        }, 1100)
        setTimeout(function(){
        	$("#submit").trigger('click')
        }, 1200)
    }
})