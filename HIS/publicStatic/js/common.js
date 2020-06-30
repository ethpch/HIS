$(function () {
	$("#logout").click(function () {
		$.ajax({
			type:"post",
			url:"logout",
			data:{},
			dataType:"json",
			success:function(data){
				location.href="login.html";
			}
		});
	})
})