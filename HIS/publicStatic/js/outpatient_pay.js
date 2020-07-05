$(function(){
	//点击search图标，查询患者信息和收费列表
	$("#search").click(function(){
		var pid = $("#pid").val();
		if(pid==""){
			alert("请输入要查询的病历号");
		}else if(isNaN(pid)){
			alert("病历号必须为数字");
		}else{
			$.ajax({
				type:"post",
				url:"/api/selectPatientByPno/"+$("#pid").val(),
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
						
						//清空表格中已有的记录
						$("#item_data tr:not(:first)").empty();
						
						var totalPay=0;
						
						//追加检查申请的记录
						for(var i=0;i<data.cirList.length;i++){
							var pstatus;
							if(data.cirList[i].paystatus==0){
								pstatus="未缴费";
								$("#item_data").append("<tr><td><input type='checkbox'  name='cid' value='"+data.cirList[i].id+"'     class='chk'  ></td>" +
										"<td>"+data.cirList[i].checkItem.itemname+"</td>" +
										"<td>"+data.cirList[i].checkItem.price+"</td>" +
										"<td>"+data.cirList[i].amount+"</td>" +
												"<td class='payCount'  >"+(data.cirList[i].checkItem.price * data.cirList[i].amount) +"</td>" +
												"<td>"+pstatus+"</td></tr>");
							}else{
								pstatus="已缴费";
								$("#item_data").append("<tr><td><input type='checkbox'  disabled   class='chk'  ></td>" +
										"<td>"+data.cirList[i].checkItem.itemname+"</td>" +
										"<td>"+data.cirList[i].checkItem.price+"</td>" +
										"<td>"+data.cirList[i].amount+"</td>" +
												"<td>"+(data.cirList[i].checkItem.price * data.cirList[i].amount) +"</td>" +
												"<td>"+pstatus+"</td></tr>");
							}
							
							
							totalPay = totalPay + (data.cirList[i].checkItem.price * data.cirList[i].amount);
						}
						//追加检验申请的记录
						for(var i=0;i<data.iirList.length;i++){
							var pstatus;
							if(data.iirList[i].paystatus==0){
								pstatus="未缴费";
								$("#item_data").append("<tr><td><input type='checkbox' name='iid' value='"+data.iirList[i].id+"'    class='chk'  ></td>" +
										"<td>"+data.iirList[i].inspectItem.inspectname+"</td>" +
										"<td>"+data.iirList[i].inspectItem.price+"</td>" +
										"<td>"+data.iirList[i].amount+"</td>" +
												"<td class='payCount'  >"+(data.iirList[i].inspectItem.price * data.iirList[i].amount)+"</td>" +
												"<td>"+pstatus+"</td></tr>");
							}else{
								pstatus="已缴费";
								$("#item_data").append("<tr><td><input type='checkbox'  disabled  class='chk'  ></td>" +
										"<td>"+data.iirList[i].inspectItem.inspectname+"</td>" +
										"<td>"+data.iirList[i].inspectItem.price+"</td>" +
										"<td>"+data.iirList[i].amount+"</td>" +
												"<td>"+(data.iirList[i].inspectItem.price * data.iirList[i].amount)+"</td>" +
												"<td>"+pstatus+"</td></tr>");
							}
							
							totalPay = totalPay +(data.iirList[i].inspectItem.price * data.iirList[i].amount);
						}
						//将总金额显示在页面上
						$("#totalPay").html(totalPay);
					}
				}
			});
		}
	});
	
	
	//复选框全选
	$("#selectAll").click(function(){
		var chks =$(".chk");
		var payCountTd = $(".payCount");
		var total=0;
		if($(this)[0].checked==true){
			for(var i=0;i<chks.length;i++){
				chks[i].checked = true;
			}
			for(var j=0;j<payCountTd.length;j++){
				total = total + parseFloat($(payCountTd[j]).html());
			}
			$("#currentPay").html(total);
		}else{
			for(var i=0;i<chks.length;i++){
				chks[i].checked = false;
			}
			$("#currentPay").html(0);
		}
	});
	
	//在每一行的复选框上绑定单击事件
	$(document).on("click",".chk",function(){
		//当前的应收金额
		var currentPay = $("#currentPay").html();
		//操作行对应的金额
		var pay = $(this).parent().next().next().next().next().html();
		if($(this)[0].checked==true){
			$("#currentPay").html(parseFloat(currentPay) + parseFloat(pay));
		}else{
			$("#currentPay").html(parseFloat(currentPay) - parseFloat(pay));
		}
	});
	
	//收费
	$("#submitItem").click(function(){
		var chks =$(".chk");
		var flag = false;
		for(var k=0;k<chks.length;k++){
			if(chks[k].checked == true){
				flag = true;
				break;
			}
		}
		//判断是否有选中的复选框
		if(!flag){
			alert("请选择要交费的记录");
		}else{
			$.ajax({
				type:"post",
				url:"/api/payItems",
				data:$("#form1").serialize(),
				dataType:"json",
				success:function(data){
					console.log(data);
					alert(data.result);
					location.reload();
				}
			});
		}
	})
	
	$("#div1_1").click(function(){
		location.href="outpatient_register.html";
	})
	
	$("#refund").click(function(){
		location.href="outpatient_refund.html";
	})
	
})


