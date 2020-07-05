$(function () {

	//生成病历号
	$.ajax({
		type:"post",
		url:"/api/getPatientNo",
		data:{},
		dataType:"json",
		success:function(data){
			console.log(data);
			$("#pid").val(data.pno);
		}
	});
	
	//查询挂号级别
	$.ajax({
		type:"post",
		url:"/api/getLevelData",
		data:{},
		dataType:"json",
		success:function(data){
			console.log(data);
			for(var i=0;i<data.length;i++){
				$("#level").append("<option data-cost='"+data[i].cost+"'   value='"+data[i].id+"' >"+data[i].levelname+"</option>")
			}
		}
	});
	
	//查询所有科室信息
	$.ajax({
		type:"post",
		url:"/api/getDeptData",
		data:{},
		dataType:"json",
		success:function(data){
			console.log(data);
			for(var i=0;i<data.length;i++){
				$("#dept").append("<option value='"+data[i].id+"' >"+data[i].deptname+"</option>")
			}
		}
	});
	
	//查询患者信息，每页显示2条，显示第一页的数据
	var pagesize=2;
	var pagenum=1;
	getPageData();
	
	//刷新
	$("#div4_1").click(function(){
		pagenum=1;
		getPageData();
		$("#pnum").html(1);
	})
	
	//上一页
	$("#last").click(function(){
		if(pagenum-1==0){
			alert("没有上一页数据");
		}else{
			pagenum=pagenum-1;
			getPageData();
			$("#pnum").html(pagenum);
		}
	})
	//下一页
	$("#next").click(function(){
		pagenum=pagenum+1;
		getPageData();
		//$("#pnum").html(parseInt($("#pnum").html())+1);
	})
	
	function  getPageData(){
		$.ajax({
			type:"post",
			url:"/api/getPatientData/"+pagesize+"/"+pagenum,
			data:{},
			dataType:"json",
			success:function(data){
				console.log(data);
				//如果不是第一页，没有查询到数据
				if(pagenum>1 && data.length>0){
					$("#pnum").html(pagenum);
				}
				if (pagenum > 1 && data.length == 0) {
					pagenum = pagenum - 1;
					alert("没有更多数据了");
				}else{
					$("#data_table tr:not(:first)").empty();
					for(var i=0;i<data.length;i++){
						var status="";
						if(data[i].pstatus=="已退号"){
							status = "已退号";
						}else{
							status = "正常";
						}
						$("#data_table").append("<tr><td>"+data[i].pid+"</td><td>"+data[i].pname+"</td><td>"+data[i].sex+"</td>" +
								"<td>"+data[i].idcard+"</td><td>"+data[i].createDate+"</td><td>"+data[i].level.levelname+"</td>" +
								"<td>"+data[i].pstatus+"</td><td>"+status+"</td><td>"+data[i].dept.deptname+"</td><td>"+data[i].doc.dname+"</td></tr>")
					}
				}
			}
		});
		
	}
	
	
	$("#age").blur(function(){
		var age = $("#age").val();
		var day = new Date();
		var currentYear = day.getFullYear();
		var year = currentYear - age;
		$("#year").val(year);
	})
	
	$("#year").blur(function(){
		var year = $("#year").val();
		var day = new Date();
		var currentYear = day.getFullYear();
		var age = currentYear - year;
		$("#age").val(age);
	})
	
	//选择科室去变更医生列表
	$("#dept").change(function(){
		$.ajax({
			type:"post",
			url:"/api/getDoctorByDept/"+$("#dept").val(),
			data:{},
			dataType:"json",
			success:function(data){
				console.log(data);
				$("#doctor").empty();
				$("#doctor").append("<option value='-1' >------请选择------</option>");
				for(var i=0;i<data.length;i++){
					$("#doctor").append("<option value='"+data[i].id+"' >"+data[i].dname+"</option>");
				}
			}
		});
	})
	
	//选择挂号级别得到应收金额
	$("#level").change(function(){
		var cost = $("#level option:selected").attr("data-cost");
		$("#cost").val("0");
		var flag = $("#yes");
		if(flag[0].checked){
			$("#cost").val(parseInt(cost)+1);
		}else{
			$("#cost").val(parseInt(cost));
		}
	})
	
	//切换是否需要病历本，变更应收金额
	$("#yes").click(function(){
		var cost = $("#level option:selected").attr("data-cost");
		$("#cost").val("0");
		$("#cost").val(parseInt(cost)+1);
	})
	
	$("#no").click(function(){
		var cost = $("#level option:selected").attr("data-cost");
		$("#cost").val("0");
		$("#cost").val(parseInt(cost));
	})
	
	//挂号
	$("#regBtn").click(function(){
		$.ajax({
			type:"post",
			url:"/api/savePatient",
			data:$("#form1").serialize(),
			dataType:"json",
			success:function(data){
				console.log(data);
				alert(data.result);
				location.reload();
			}
		});
	})
	
	//点击退号管理进入退号页面
	$("#refund").click(function(){
		location.href="outpatient_refund.html";
	});
	
	//点击门诊收费管理进入收费页面
	$("#div1_2").click(function(){
		location.href="outpatient_pay.html";
	})
		
})












