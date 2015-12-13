$(function(){
  $('#input').keyup(function(){
  var input = $('#input').val();
  //len = input.length;
    if(input != ""){
      $('#show').html("");
      $.ajax({
             url:"/"+input,
             crossDomain: true,
             type:"GET",
             dataType:'json',
             success: function(html) {
                result = html['result'];
                result_split = result.split(",");
                console.log(result_split);
                $.each(result_split,function(k,v){
          				$('#show').append("<div>"+v+"</div>"+"<br>").addClass("item");
          			});
             },
            error:function(html){
                alert('error');
            }
       });
    }
  });
});
