$(function(){
	
	//点击病例进入病例页面
	$("#div1_1").click(function(){
		location.href="doctor_medicalrecord.html";
	})
	
	//点击检验申请进入下一页面
	$("#div1_3").click(function(){
		location.href="doctor_inspectitem.html";
	})
	
	//点击检查申请进入检查申请页面
	$("#div1_2").click(function(){
		location.href="doctor_checkitem.html";
	})
	
	$("#search").click(function(){
		var pid = $("#pid").val();
		if(pid==""){
			alert("请输入要查询的病历号");
		}else if(isNaN(pid)){
			alert("病历号必须为数字");
		}else{
			$.ajax({
				type:"post",
				url:"/api/getPatientAndMrData/"+pid,
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
						//显示病例信息
						$("#description").html(data.mr.description);
						$("#medicalhistory").html(data.mr.medicalhistory);
						$("#familyhistory").html(data.mr.familyhistory);
						$("#initialresult").html(data.mr.initialresult);
						$("#result").html(data.mr.result);
						$("#finalresult").html(data.mr.finalresult);
						$("#id").val(data.mr.id);
					}
				}
			});
		}
	});
	
	//提交确诊结果
	$("#submitItem").click(function(){
		if($("#pid").val()==""){
			alert("请先选择患者！")
		}else{
			$.ajax({
				type:"post",
				url:"/api/updateMedicalRecord",
				data:$("#form1").serialize(),
				dataType:"json",
				success:function(data){
					console.log(data);
					alert(data.result);
					location.href="doctor_medicalrecord.html";
				}
			});
		}
	})
	
	
	
})
