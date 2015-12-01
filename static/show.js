function Go(){
  var input = $('#input').val();
  $.ajax({
         url:"/"+input,
         crossDomain: true,
         type:"GET",
         dataType:'json',
         success: function(html) {
            result = html['result'];
            $('#show').html("結果: "+result);
         },
        error:function(html){
            alert('error');
        }
   });
}
