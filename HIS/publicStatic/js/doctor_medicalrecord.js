$(function(){
	//初始化查询该医生当天的挂号信息
	$.ajax({
		type:"post",
		url:"/api/getPatientDataByDoctor",
		data:{},
		dataType:"json",
		success:function(data){
			console.log(data);
			for(var i=0;i<data.length;i++){
				var status="";
				if(data[i].pstatus=="已退号"){
					status = "已退号";
				}else{
					status = "正常";
				}
				if(data[i].pstatus=="未看诊"){
					$("#data_table").append("<tr class='first_table' data-pid='"+data[i].pid+"'  ><td>"+data[i].pid+"</td><td>"+data[i].pname+"</td><td>"+data[i].sex+"</td>" +
							"<td>"+data[i].idcard+"</td><td>"+data[i].createDate+"</td><td>"+data[i].level.levelname+"</td>" +
							"<td>"+data[i].pstatus+"</td><td>"+status+"</td><td>"+data[i].dept.deptname+"</td><td>"+data[i].doc.dname+"</td></tr>");
				}else{
					$("#data_table_1").append("<tr><td>"+data[i].pid+"</td><td>"+data[i].pname+"</td><td>"+data[i].sex+"</td>" +
							"<td>"+data[i].idcard+"</td><td>"+data[i].createDate+"</td><td>"+data[i].level.levelname+"</td>" +
							"<td>"+data[i].pstatus+"</td><td>"+status+"</td><td>"+data[i].dept.deptname+"</td><td>"+data[i].doc.dname+"</td></tr>");
				}
			}
		}
	});
	
	//未看诊列表的每一行绑定单击事件，跳转到下一页面
	$(document).on("click",".first_table",function(){
		var pid = $(this).attr("data-pid");
		location.href="doctor_regmedicalrecord.html?pid="+pid;
	})
	
	//点击检查申请进入下一页面
	$("#div1_2").click(function(){
		location.href="doctor_checkitem.html";
	})
	
	//点击检验申请进入下一页面
	$("#div1_3").click(function(){
		location.href="doctor_inspectitem.html";
	})
	
	//点击确诊进入确诊页面
	$("#div1_4").click(function(){
		location.href="doctor_result.html";
	})
	
	
})


