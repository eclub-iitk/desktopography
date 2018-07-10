var padlock = document.getElementById('padlock');
var bar = document.getElementById('bar');
var combinationInputTemplate = document.querySelector('.combination-input-template');
var combinationInputContainer = document.getElementById('combination-input-container');
var unlockButton = document.getElementById('unlock-button');
var responseText = document.getElementById('response-text');

var inputWidth = 60;
var comboArray = [0, 0, 0, 0];

var lockRestingColor = void 0;

TweenMax.set('#padlock', { transformOrigin: '50% 50%' });

var searchParams = {};
window.location.search.replace('?', '').split('&').forEach(function (x) {
	var a = x.split('=');searchParams[a[0]] = a[1];
});
if (searchParams['h']) {
	var number = parseInt(searchParams['h'], 16);
	if (!isNaN(number)) {
		comboArray = (number + '').split('').map(function (x) {
			return parseInt(x, 10);
		});
	}
}

for (var i = 0; i < comboArray.length; i++) {
	var clone = combinationInputTemplate.cloneNode(true);

	var x = i * inputWidth - (comboArray.length - 1) * inputWidth / 2;
	clone.setAttribute('transform', 'translate(' + x + ',0)');
	clone.setAttribute('class', 'combination-input');

	combinationInputContainer.appendChild(clone);
}

unlockButton.onclick = function () {
	if (checkCombination()) {
		startUnlockAttempt(function () {
			var tl = new TimelineMax({ onComplete: finishUnlockAttempt });
			lockRestingColor = 'hsl(120,50%,100%)';
			responseText.innerHTML = 'correct';

			tl.to('#box', 0, { fill: lockRestingColor });
			tl.to('#bar', 0, { stroke: lockRestingColor });
			tl.to('#bar', 0.3, { y: -20, ease: Back.easeOut.config(4) }, 'b');
			tl.to('#padlock', 0.3, { scale: 1.2, ease: Back.easeOut.config(4) }, 'b');
			tl.to('#box', 0.3, { fill: 'hsl(120,50%,60%)' }, 'b');
			tl.to('#bar', 0.3, { stroke: 'hsl(120,50%,60%)' }, 'b');
		});
	} else {
		startUnlockAttempt(function () {
			var tl = new TimelineMax({ onComplete: finishUnlockAttempt });
			lockRestingColor = 'hsl(0,50%,100%)';
			responseText.innerHTML = 'incorrect';

			tl.to('#box', 0, { fill: lockRestingColor });
			tl.to('#bar', 0, { stroke: lockRestingColor });
			tl.to('#bar', 0.1, { y: 0, ease: Power0.easeNone }, 'b');
			tl.to('#padlock', 0.1, { scale: 1, ease: Power0.easeNone }, 'b');
			tl.to('#box', 0.1, { fill: 'hsl(0,50%,60%)' }, 'b');
			tl.to('#bar', 0.1, { stroke: 'hsl(0,50%,60%)' }, 'b');
			tl.to('#padlock', 0.1, { x: 260 });
			tl.to('#padlock', 0.1, { x: 240 });
			tl.to('#padlock', 0.1, { x: 260 });
			tl.to('#padlock', 0.1, { x: 250 });
		});
	}
};

var startUnlockAttempt = function startUnlockAttempt(onComplete) {
	var tl = new TimelineMax({ onComplete: onComplete });

	tl.to('#unlock-button', 0.5, { y: 550, opacity: 0, ease: Power2.easeInOut }, 'a');
	tl.staggerTo('.combination-input', 0.5, { y: 200, opacity: 0, ease: Power2.easeInOut }, 0.1, 'a+=0.25');
	tl.to('#padlock', 0.5, { y: 250, ease: Power2.easeInOut });

	tl.to('#padlock', 1, { scale: 0.9 }, 'build');
	tl.to('#bar', 1, { y: 10 }, 'build');
};

var finishUnlockAttempt = function finishUnlockAttempt() {
	var tl = new TimelineMax();

	tl.to('#response-text', 0.5, { y: 30, opacity: 1 });
	tl.to('#response-text', 2, {});
	tl.to('#response-text', 0.5, { y: 0, opacity: 0 });
	tl.to('#box', 0.25, { fill: lockRestingColor, ease: Power2.easeInOut }, 'a');
	tl.to('#bar', 0.25, { stroke: lockRestingColor, y: 0, ease: Power2.easeInOut }, 'a');
	tl.to('#padlock', 0.25, { scale: 1, y: 220 }, 'a');
	tl.to('#unlock-button', 0.5, { y: 450, opacity: 1 }, 'b');
	tl.staggerTo('.combination-input', 0.5, { y: 0, opacity: 1 }, 0.1, 'b+=0.25');
};

var delegateFunction = function delegateFunction(e) {
	if (e.target.matches('.up-button')) {
		var text = e.target.parentElement.querySelector('.text-value');
		text.innerHTML = rollOver(parseInt(text.innerHTML) + 1);
	} else if (e.target.matches('.down-button')) {
		var _text = e.target.parentElement.querySelector('.text-value');
		_text.innerHTML = rollOver(parseInt(_text.innerHTML) - 1);
	}
};

var rollOver = function rollOver(val) {
	if (val > 9) {
		return val % 10;
	}if (val < 0) {
		return val + 10;
	}
	return val;
};

var checkCombination = function checkCombination() {
	var inputs = document.querySelectorAll('.combination-input .text-value');
	var valid = true;

	for (var _i = 0; _i < inputs.length; _i++) {
		if (parseInt(inputs[_i].innerHTML) !== comboArray[_i]) {
			valid = false;
		}
	}

	return valid;
};

document.onmouseup = delegateFunction;
document.ontouchend = delegateFunction;