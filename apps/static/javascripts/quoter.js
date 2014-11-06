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
})