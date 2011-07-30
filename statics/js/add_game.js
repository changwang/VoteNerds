jQuery(function(){
    var form = jQuery("#add_game_form");
    form.submit(function(e){
        jQuery("#add_game_button").attr("disabled", true);
        jQuery("#add_game").load(
            form.attr("action"),
            form.serializeArray(),
            function(responseText, responseStatus) {
                jQuery("#add_game_button").attr("disabled", false);
            }
        );
        e.preventDefault();
    });
});
