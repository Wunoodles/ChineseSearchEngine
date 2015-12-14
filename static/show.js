$(function(){
  $('#input').keyup(function(){
  var input = $('#input').val();
  //len = input.length;
    if(input != ""){
      $.ajax({
             url:"/"+input,
             crossDomain: true,
             type:"GET",
             dataType:'json',
             success: function(html) {
                $('#show').html("");
                result = html['result'];
                result_split = result.split(",");
                console.log(result_split);
                $.each(result_split,function(k,v){
          				$('#show').append("<div class=\' item \'>"+v+"</div>");
          			});
             },
            error:function(html){
                alert('error');
            }
       });
    }
    if(input == ""){
      $('#show').html("");
    }
  });
});
