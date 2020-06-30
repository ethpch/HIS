// ��ȫǰ��˷��뿪����csrf�����������
var csrftoken;
$.get('/csrf_token', function (resp) {
	csrftoken = resp.token;  // ������ͼ�������ص�token�����浽ȫ�ֱ�����
	document.cookie = 'csrftoken=' + resp.token;  // token���õ�cookie��
});
function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
// ��jquery��ÿ��������ǰ����X-CSRFToken
$.ajaxSetup({
	beforeSend: function (xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
