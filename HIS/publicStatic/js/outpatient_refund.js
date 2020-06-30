$(function(){
	
	$("#search").click(function(){
		var pid = $("#pid").val();
		if(pid==""){
			alert("请输入要查询的病历号");
		}else if(isNaN(pid)){
			alert("病历号必须为数字");
		}else{
			$.ajax({
				type:"post",
				url:"/api/getPatientByNo/"+pid,
				data:{},
				dataType:"json",
				success:function(data){
					console.log(data);
					if(data.pid==0){
						alert("系统中不存在该患者");
					}else{
						$("#pno").val(data.pid);
						$("#pname").val(data.pname);
						if(data.sex=="男"){
							$("#sex1")[0].checked=true;
						}else{
							$("#sex0")[0].checked=true;
						}
						$("#createdate").val(data.createDate);
						$("#idcard").val(data.idcard);
						$("#level").val(data.level.levelname);
						if(data.pstatus=="未看诊" || data.pstatus=="已退号"){
							$("#pstatus").html("否");
						}else{
							$("#pstatus").html("是");
						}
						if(data.pstatus=="已退号"){
							$("#status").html("已退号");
						}else{
							$("#status").html("正常");
						}
						$("#deptname").val(data.dept.deptname);
						$("#dname").val(data.doc.dname);
						if(data.pstatus=="未看诊"){
							$("#refund")[0].disabled=false;
						}
					}
				}
			});
		}
	})
	
	//退号
	$("#refund").click(function(){
		$.ajax({
			type:"post",
			url:"/api/refundPatient/"+$("#pid").val(),
			data:{},
			dataType:"json",
			success:function(data){
				console.log(data);
				$("#status").html("已退号");
				$("#refund")[0].disabled=true;
				alert("退号成功");
			}
		});
	})
	
	//点击门诊挂号管理回到挂号页面
	$("#div1_1").click(function(){
		location.href="outpatient_register.html";
	})
	
	
	//点击门诊收费管理进入收费页面
	$("#div1_2").click(function(){
		location.href="outpatient_pay.html";
	})
	
})
