// 完全前后端分离开发的csrf保护解决方案
var csrftoken;
$.get('/csrf_token', function (resp) {
	csrftoken = resp.token;  // 接受视图函数返回的token，保存到全局变量中
	document.cookie = 'csrftoken=' + resp.token;  // token设置到cookie中
});
function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
// 在jquery的每个请求发起前设置X-CSRFToken
$.ajaxSetup({
	beforeSend: function (xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
