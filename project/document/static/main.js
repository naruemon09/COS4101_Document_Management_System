var dt_obj= new Date();
function addOption(selectbox,text,value ) {
	var optn = document.createElement("OPTION");
	optn.text = text;
	optn.value = value;
	selectbox.options.add(optn);
}


///////////// date //////////////////
var today_date= dt_obj.getDate();
function addOption_list1() {
	for (var i=1; i < 32;++i) {
		var dt_day = document.getElementById("dt_day");
		addOption(dt_day, i, i);
		if(i== today_date){
			dt_day.options[i].selected=true;
		}
	}
	addOption_list2();
}
//////////////End of Date //////////


///////////// Month //////////////////
var current_month=dt_obj.getMonth() +1;
function addOption_list2() {
	var dt_month = document.getElementById("dt_month");
	for (var i=1; i < 13;++i) {
		addOption(dt_month, i, i);
		if(i== current_month) {
			dt_month.options[i].selected=true;
		}
	}
	addOption_list3();
}
//////////////End of Month //////////


///////////// Year //////////////////
var current_year=dt_obj.getFullYear();
function addOption_list3() {
	var dt_year = document.getElementById("dt_year");
	for (var i=0; i < 7;++i) {
		var j=current_year+i-2;
		match_year=current_year+i;
		addOption(dt_year, j, j);
		if((j-1)== current_year ) {
			dt_year.options[i].selected=true;
		}
	}
}
//////////////End of Year //////////


///////////// Position //////////////////
function addOption_list4() {
	var select = document.getElementById("selectPosition");
	var position = ["เจ้าหน้าที่", "อาจารย์"];
	for(var i = 0; i < position.length; i++) {
		var opt = position[i];
		var el = document.createElement("option");
		el.textContent = opt;
		el.value = opt;
		select.appendChild(el);
	}
}
//////////////End of Position //////////

///////////// Type Doc //////////////////
function addOption_list5() {
	var select_type = document.getElementById("selectType");
	var type = ["การเงิน", "วัสดุ" , "งานบริการการศึกษา" , "งานนโยบายและแผน" , "งานประกัน" , "งานเจ้าหน้าที่" , "คำสั่ง" , "รายงานการประชุมภาค" , "อื่นๆ"];
	for(var i = 0; i < type.length; i++) {
		var opt = type[i];
		var el = document.createElement("option");
		el.textContent = opt;
		el.value = opt;
		select_type.appendChild(el);
	}
	addOption_list1()
}
//////////////End of Type Doc //////////
