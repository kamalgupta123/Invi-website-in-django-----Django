$(document).ready(function(){
    $('.gst_details').hide();
    $('.gst_number_form').hide();
    $('#identity').hide();
    $('#verify_otp').hide();
    $('#id_gst').addClass('form-control')
    $(document).on("click","#seller_and_purchaser",function(){
        $('.gst_details').show();
    });
    $(document).on("click","#gst_registered_yes",function(){
        $('.gst_number_form').show();
    });
    $(document).on('submit', '#Gst_form',function(e){
        $.post('/register/', $(this).serialize(), function(data){
            console.log(data);
        });
        e.preventDefault();
    });
    $(document).on('submit', '#otp_form',function(e){
        $.post('/send_otp/', $(this).serialize(), function(data){
            console.log(data);
            $('#verify_otp').show();
        });
        e.preventDefault();
    });
    $(document).on('submit', '#verify_otp_form',function(e){
        $.post('/verify_otp/', $(this).serialize(), function(data){
            console.log(data);
            $('#identity').show();
        });
        e.preventDefault();
    });
});