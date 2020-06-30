$(function () {
	//自动填充角色信息
	$.ajax({
		url: "/api/selectRoles",
		success: function (data) {
			for (var i = 0; i < data.length; i++) {
				$("#role").append("<option value='" + data[i] + "'>" + data[i] + "</option>");
			}
		}
	});
	$("#loginBtn").click(function () {
		if ($("#username").val() == '') {
			alert("对不起，用户名不得为空！");
			return;
		}
		if ($("#password").val() == '') {
			alert("对不起，密码不得为空！");
			return;
		}
		$.ajax({
			url: "/api/selectUser",
			data: $("#form1").serialize(),
			method: "post",
			success: function (data) {
				if (data == "门诊管理员") {
					window.location.href = "outpatient_register.html";
				} else if (data == "医生管理员") {
					location.href = "doctor_medicalrecord.html";
				} else if (data == "error") {
					alert("对不起，登录信息有误，请重新登录！");
				}
			}
		});
	});
});
