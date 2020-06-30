//function GetUrlRelativePath() {
//    var url = document.location.toString();
//    var arrUrl = url.split("//");

//    var start = arrUrl[1].indexOf("/");
//    var relUrl = arrUrl[1].substring(start);

//    if (relUrl.indexOf("?") != -1) {
//        relUrl = relUrl.split("?")[0];
//    }
//    return relUrl;
//}


//$(function () {
//    if (GetUrlRelativePath().search(/admin\/hospital\/patient\/\d+\/(add|change)/) > 0) {
//        $(function () {
//            $("[name=deptid]").change(function () {
//                var selecteddeptid = jQuery(this).children("option:selected").val();
//                $.ajax({
//                    url: "/api/patient_dept_doctor",
//                    method: "post",
//                    data: $(this).serialize(),
//                    success: function (data) {
//                        $("[name=doctorid]").empty()
//                        $("[name=doctorid]").append("<option value=0>---------</option>")
//                        for (var i = 0; i < data.length; i++) {
//                            $("[name=doctorid]").append("<option value=" + i + ">" + data[i] + "</option>");
//                        }
//                    }
//                });
//            });
//        });
//    };
//});