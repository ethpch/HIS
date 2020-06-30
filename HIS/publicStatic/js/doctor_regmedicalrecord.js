$(function(){
	var pid = location.href.substr(location.href.indexOf('=')+1);
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
			}
		}
	});
	
	//点击生成病历按钮存储病例信息
	$("#regMr").click(function(){
		$.ajax({
			type:"post",
			url:"/api/regMedicalRecord/"+pid,
			data:$("#form1").serialize(),
			dataType:"json",
			success:function(data){
				console.log(data);
				alert(data.result);
				location.href="doctor_medicalrecord.html";
			}
		});
	})
	
	
})
