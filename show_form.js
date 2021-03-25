function show() {
	btn1.style.visibility = 'hidden';
	btn2.style.visibility = 'hidden';
	hidden.style.visibility = 'visible';
	hidden_btn.style.visibility = 'visible';
};

function show2() {
	btn1.style.visibility = 'hidden';
	btn2.style.visibility = 'hidden';
	hidden2.style.visibility = 'visible';
	hidden_btn2.style.visibility = 'visible';
};

btn1.addEventListener("click", show);
btn2.addEventListener("click", show2);
