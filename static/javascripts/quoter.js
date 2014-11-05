$(document).ready(function(){
	$("#form_success, #form_failure").hide();
	$("#add_quote").submit(function() {
	    $.post($(this).attr("action"), $(this).serialize(), function(e) {
	        if (e.status == "success") {
	            $("#form_success").fadeIn();
	            var elements = "<div class='item'><blockquote>" + e.quote.quote + "<cite>" + e.quote.author.first_name + e.quote.author.last_name + "</cite></blockquote></div>";
	            $("#quotes_block").masonry( 'addItems', elements )
	        } else if (e.status == "failure") {
	            $("#form_failure").fadeIn();
	        }
	    }, "json");
	    $("input[type=text]").val("");
	    $("textarea").val("");
	    return false
	});
})