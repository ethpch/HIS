use his_django;
INSERT INTO `hospital_checkitem` VALUES ('1', 'B超检查', '158.00');
INSERT INTO `hospital_checkitem` VALUES ('2', 'CT检查', '880.00');
INSERT INTO `hospital_checkitem` VALUES ('3', '核磁共振检查', '1200.00');

INSERT INTO `hospital_dept` VALUES ('5', '儿科');
INSERT INTO `hospital_dept` VALUES ('4', '消化科');
INSERT INTO `hospital_dept` VALUES ('3', '眼科');
INSERT INTO `hospital_dept` VALUES ('2', '耳鼻喉科');
INSERT INTO `hospital_dept` VALUES ('1', '骨科');

INSERT INTO `hospital_doctor` VALUES ('1', '于鹏', '1');
INSERT INTO `hospital_doctor` VALUES ('2', '沙首行', '1');
INSERT INTO `hospital_doctor` VALUES ('3', '杨卫轩', '2');
INSERT INTO `hospital_doctor` VALUES ('4', '孙英', '3');
INSERT INTO `hospital_doctor` VALUES ('5', '李博文', '3');
INSERT INTO `hospital_doctor` VALUES ('6', '郑飞雪', '4');
INSERT INTO `hospital_doctor` VALUES ('7', '夏伟松', '4');
INSERT INTO `hospital_doctor` VALUES ('8', '刘思光', '5');
INSERT INTO `hospital_doctor` VALUES ('9', '姚望', '5');

INSERT INTO `hospital_inspectitem` VALUES ('1', '验血', '54.00');
INSERT INTO `hospital_inspectitem` VALUES ('2', '验尿', '15.80');

INSERT INTO `hospital_level` VALUES ('1', '普通号', '8');
INSERT INTO `hospital_level` VALUES ('2', '专家号', '15');

INSERT INTO `hisoperator_user` VALUES ('1', '陈曦', '123456', '门诊管理员');
INSERT INTO `hisoperator_user` VALUES ('2', '于鹏', '111111', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('3', '沙首行', '666666', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('4', '杨卫轩', '888888', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('5', '孙英', '999999', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('6', '李博文', '777777', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('7', '郑飞雪', '666666', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('8', '夏伟松', '333333', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('9', '姚望', '888888', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('10', '刘思光', '888888', '医生管理员');
INSERT INTO `hisoperator_user` VALUES ('11', '郭秋玲', 'admin', '系统管理员');