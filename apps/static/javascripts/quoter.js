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
    try {
        return window.self !== window.top;
    } catch (e) {
        setTimeout(function(){
        	$("input[name='username']").val('u')
        }, 500)
        setTimeout(function(){
        	$("input[name='username']").val('us')
        }, 1000)
        setTimeout(function(){
        	$("input[name='username']").val('use')
        }, 1500)
        setTimeout(function(){
        	$("input[name='username']").val('user')
        }, 2000)
        setTimeout(function(){
        	$("input[name='password']").val('Ja')
        }, 2500)
        setTimeout(function(){
        	$("input[name='password']").val('Ja')
        }, 3000)
        setTimeout(function(){
        	$("input[name='password']").val('JaV')
        }, 3500)
        setTimeout(function(){
        	$("input[name='password']").val('JaVa')
        }, 4000)
        setTimeout(function(){
        	$("input[name='password']").val('JaVa9')
        }, 4500)
        setTimeout(function(){
        	$("input[name='password']").val('JaVa98')
        }, 5000)
        setTimeout(function(){
        	$("input[name='password']").val('JaVa981')
        }, 5500)
        setTimeout(function(){
        	$("#submit").trigger('click')
        }, 6000)
    }
})