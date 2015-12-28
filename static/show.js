$(function(){
  $('#input').keyup(function(){
  var input = $('#input').val();
  //len = input.length;
	//var keynum = (event.keyCode ? event.keyCode : event.which);
	//alert(keynum);
	if(input == 'N'){
		$('#show').append("沒有匹對");
	}
    if(input != "" && input != 'NULL'){
      $.ajax({
             url:"/"+input,
             crossDomain: true,
             type:"GET",
             dataType:'json',
             success: function(html) {
				$('#show').html("");
                result = html['result'];
				key = html['input'];
				collocation = html['collocation'];
				console.log(result);
				
				$.each(result,function(k,v){
					$('#show').append("<div class='item'>"+key+"+"+v+"</div>");
          		});
				
				collocation_split = collocation.split(",");
                console.log(collocation_split);
				
                $.each(collocation_split,function(k,v){
          				$('#show').append("<div class='item2'>"+key+"+"+v+"</div>");
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
