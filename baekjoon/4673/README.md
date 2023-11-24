# 4673 
Source URL: https://www.acmicpc.net/problem/4673 
# Description 
<div class="" id="problem-body">
<div class="col-md-12">
<section class="problem-section" id="description">
<div class="headline">
<h2>문제</h2>
</div>
<div class="problem-text" id="problem_description">
<p>셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.</p>
<p>양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. </p>
<p>예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.</p>
<p>33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...</p>
<p>n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다. </p>
<p>생성자가 없는 숫자를 셀프 넘버라고 한다. 100보다 작은 셀프 넘버는 총 13개가 있다. 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97</p>
<p>10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="input">
<div class="headline">
<h2>입력</h2>
</div>
<div class="problem-text" id="problem_input">
<p>입력은 없다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="output">
<div class="headline">
<h2>출력</h2>
</div>
<div class="problem-text" id="problem_output">
<p>10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="limit" style="display:none;">
<div class="headline">
<h2>제한</h2>
</div>
<div class="problem-text" id="problem_limit">
</div>
</section>
</div>
<div class="col-md-12">
<div class="row">
<div class="col-md-6">
<section id="sampleinput1">
<div class="headline">
<h2>예제 입력 1
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-input-1" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-input-1"></pre>
</section>
</div>
<div class="col-md-6">
<section id="sampleoutput1">
<div class="headline">
<h2>예제 출력 1
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-output-1" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-output-1">1
3
5
7
9
20
31
42
53
64
 |
 |       &lt;-- a lot more numbers
 |
9903
9914
9925
9927
9938
9949
9960
9971
9982
9993
</pre>
</section>
</div>
</div>
</div>
<div class="col-md-12">
<section class="problem-section" id="hint" style="display: none;">
<div class="headline">
<h2>힌트</h2>
</div>
<div class="problem-text" id="problem_hint">
</div>
</section>
</div>
<div style="display: none;">
<div id="problem-lang-base64">W3sicHJvYmxlbV9pZCI6IjQ2NzMiLCJwcm9ibGVtX2xhbmciOiIwIiwidGl0bGUiOiJcdWMxNDBcdWQ1MDQgXHViMTE4XHViYzg0IiwiZGVzY3JpcHRpb24iOiI8cD5cdWMxNDBcdWQ1MDQgXHViMTE4XHViYzg0XHViMjk0IDE5NDlcdWIxNDQgXHVjNzc4XHViM2M0IFx1YzIxOFx1ZDU1OVx1Yzc5MCBELlIuIEthcHJla2FyXHVhYzAwIFx1Yzc3NFx1Yjk4NCBcdWJkOTlcdWM2MDBcdWIyZTQuIFx1YzU5MVx1Yzc1OCBcdWM4MTVcdWMyMTggblx1YzVkMCBcdWIzMDBcdWQ1NzRcdWMxMWMgZChuKVx1Yzc0NCBuXHVhY2ZjIG5cdWM3NTggXHVhYzAxIFx1Yzc5MFx1YjlhY1x1YzIxOFx1Yjk3YyBcdWIzNTRcdWQ1NThcdWIyOTQgXHVkNTY4XHVjMjE4XHViNzdjXHVhY2UwIFx1YzgxNVx1Yzc1OFx1ZDU1OFx1Yzc5MC4gXHVjNjA4XHViOTdjIFx1YjRlNFx1YzViNCwgZCg3NSkgPSA3NSs3KzUgPSA4N1x1Yzc3NFx1YjJlNC48XC9wPlxyXG5cclxuPHA+XHVjNTkxXHVjNzU4IFx1YzgxNVx1YzIxOCBuXHVjNzc0IFx1YzhmY1x1YzViNFx1Yzg0Y1x1Yzc0NCBcdWI1NGMsIFx1Yzc3NCBcdWMyMThcdWI5N2MgXHVjMmRjXHVjNzkxXHVkNTc0XHVjMTFjIG4sIGQobiksIGQoZChuKSksIGQoZChkKG4pKSksIC4uLlx1YWNmYyBcdWFjMTlcdWM3NDAgXHViYjM0XHVkNTVjIFx1YzIxOFx1YzVmNFx1Yzc0NCBcdWI5Y2NcdWI0ZTQgXHVjMjE4IFx1Yzc4OFx1YjJlNC4mbmJzcDs8XC9wPlxyXG5cclxuPHA+XHVjNjA4XHViOTdjIFx1YjRlNFx1YzViNCwgMzNcdWM3M2NcdWI4NWMgXHVjMmRjXHVjNzkxXHVkNTVjXHViMmU0XHViYTc0IFx1YjJlNFx1Yzc0YyBcdWMyMThcdWIyOTQgMzMgKyAzICsgMyA9IDM5XHVjNzc0XHVhY2UwLCBcdWFkZjggXHViMmU0XHVjNzRjIFx1YzIxOFx1YjI5NCAzOSArIDMgKyA5ID0gNTEsIFx1YjJlNFx1Yzc0YyBcdWMyMThcdWIyOTQgNTEgKyA1ICsgMSA9IDU3XHVjNzc0XHViMmU0LiBcdWM3NzRcdWI3ZjBcdWMyZGRcdWM3M2NcdWI4NWMgXHViMmU0XHVjNzRjXHVhY2ZjIFx1YWMxOVx1Yzc0MCBcdWMyMThcdWM1ZjRcdWM3NDQgXHViOWNjXHViNGU0IFx1YzIxOCBcdWM3ODhcdWIyZTQuPFwvcD5cclxuXHJcbjxwPjMzLCAzOSwgNTEsIDU3LCA2OSwgODQsIDk2LCAxMTEsIDExNCwgMTIwLCAxMjMsIDEyOSwgMTQxLCAuLi48XC9wPlxyXG5cclxuPHA+blx1Yzc0NCBkKG4pXHVjNzU4IFx1YzBkZFx1YzEzMVx1Yzc5MFx1Yjc3Y1x1YWNlMCBcdWQ1NWNcdWIyZTQuIFx1YzcwNFx1Yzc1OCBcdWMyMThcdWM1ZjRcdWM1ZDBcdWMxMWMgMzNcdWM3NDAgMzlcdWM3NTggXHVjMGRkXHVjMTMxXHVjNzkwXHVjNzc0XHVhY2UwLCAzOVx1YjI5NCA1MVx1Yzc1OCBcdWMwZGRcdWMxMzFcdWM3OTAsIDUxXHVjNzQwIDU3XHVjNzU4IFx1YzBkZFx1YzEzMVx1Yzc5MFx1Yzc3NFx1YjJlNC4gXHVjMGRkXHVjMTMxXHVjNzkwXHVhYzAwIFx1ZDU1YyBcdWFjMWNcdWJjZjRcdWIyZTQgXHViOWNlXHVjNzQwIFx1YWNiZFx1YzZiMFx1YjNjNCBcdWM3ODhcdWIyZTQuIFx1YzYwOFx1Yjk3YyBcdWI0ZTRcdWM1YjQsIDEwMVx1Yzc0MCBcdWMwZGRcdWMxMzFcdWM3OTBcdWFjMDAgMlx1YWMxYyg5MVx1YWNmYyAxMDApIFx1Yzc4OFx1YjJlNC4mbmJzcDs8XC9wPlxyXG5cclxuPHA+XHVjMGRkXHVjMTMxXHVjNzkwXHVhYzAwIFx1YzVjNlx1YjI5NCBcdWMyMmJcdWM3OTBcdWI5N2MgXHVjMTQwXHVkNTA0IFx1YjExOFx1YmM4NFx1Yjc3Y1x1YWNlMCBcdWQ1NWNcdWIyZTQuIDEwMFx1YmNmNFx1YjJlNCBcdWM3OTFcdWM3NDAgXHVjMTQwXHVkNTA0IFx1YjExOFx1YmM4NFx1YjI5NCBcdWNkMWQgMTNcdWFjMWNcdWFjMDAgXHVjNzg4XHViMmU0LiAxLCAzLCA1LCA3LCA5LCAyMCwgMzEsIDQyLCA1MywgNjQsIDc1LCA4NiwgOTc8XC9wPlxyXG5cclxuPHA+MTAwMDBcdWJjZjRcdWIyZTQgXHVjNzkxXHVhYzcwXHViMDk4IFx1YWMxOVx1Yzc0MCBcdWMxNDBcdWQ1MDQgXHViMTE4XHViYzg0XHViOTdjIFx1ZDU1YyBcdWM5MDRcdWM1ZDAgXHVkNTU4XHViMDk4XHVjNTI5IFx1Y2Q5Y1x1YjgyNVx1ZDU1OFx1YjI5NCBcdWQ1MDRcdWI4NWNcdWFkZjhcdWI3YThcdWM3NDQgXHVjNzkxXHVjMTMxXHVkNTU4XHVjMmRjXHVjNjI0LjxcL3A+XHJcbiIsImlucHV0IjoiPHA+XHVjNzg1XHViODI1XHVjNzQwIFx1YzVjNlx1YjJlNC48XC9wPlxyXG4iLCJvdXRwdXQiOiI8cD4xMCwwMDBcdWJjZjRcdWIyZTQgXHVjNzkxXHVhYzcwXHViMDk4IFx1YWMxOVx1Yzc0MCBcdWMxNDBcdWQ1MDQgXHViMTE4XHViYzg0XHViOTdjIFx1ZDU1YyBcdWM5MDRcdWM1ZDAgXHVkNTU4XHViMDk4XHVjNTI5IFx1Yzk5ZFx1YWMwMFx1ZDU1OFx1YjI5NCBcdWMyMWNcdWMxMWNcdWI4NWMgXHVjZDljXHViODI1XHVkNTVjXHViMmU0LjxcL3A+XHJcbiIsImhpbnQiOiIiLCJvcmlnaW5hbCI6IjAiLCJodG1sX3RpdGxlIjoiMCIsInByb2JsZW1fbGFuZ190Y29kZSI6IktvcmVhbiJ9LHsicHJvYmxlbV9pZCI6IjQ2NzMiLCJwcm9ibGVtX2xhbmciOiIxIiwidGl0bGUiOiJTZWxmIE51bWJlcnMiLCJkZXNjcmlwdGlvbiI6IjxwPkluIDE5NDkgdGhlIEluZGlhbiBtYXRoZW1hdGljaWFuIEQuUi4gS2FwcmVrYXIgZGlzY292ZXJlZCBhIGNsYXNzIG9mIG51bWJlcnMgY2FsbGVkIHNlbGYtbnVtYmVycy4gRm9yIGFueSBwb3NpdGl2ZSBpbnRlZ2VyIG4sIGRlZmluZSBkKG4pIHRvIGJlIG4gcGx1cyB0aGUgc3VtIG9mIHRoZSBkaWdpdHMgb2Ygbi4gKFRoZSBkIHN0YW5kcyBmb3IgZGlnaXRhZGl0aW9uLCBhIHRlcm0gY29pbmVkIGJ5IEthcHJla2FyLikgRm9yIGV4YW1wbGUsIGQoNzUpID0gNzUgKyA3ICsgNSA9IDg3LiBHaXZlbiBhbnkgcG9zaXRpdmUgaW50ZWdlciBuIGFzIGEgc3RhcnRpbmcgcG9pbnQsIHlvdSBjYW4gY29uc3RydWN0IHRoZSBpbmZpbml0ZSBpbmNyZWFzaW5nIHNlcXVlbmNlIG9mIGludGVnZXJzIG4sIGQobiksIGQoZChuKSksIGQoZChkKG4pKSksIC4uLi4gRm9yIGV4YW1wbGUsIGlmIHlvdSBzdGFydCB3aXRoIDMzLCB0aGUgbmV4dCBudW1iZXIgaXMgMzMgKyAzICsgMyA9IDM5LCB0aGUgbmV4dCBpcyAzOSArIDMgKyA5ID0gNTEsIHRoZSBuZXh0IGlzIDUxICsgNSArIDEgPSA1NywgYW5kIHNvIHlvdSBnZW5lcmF0ZSB0aGUgc2VxdWVuY2U8XC9wPlxyXG5cclxuPHA+MzMsIDM5LCA1MSwgNTcsIDY5LCA4NCwgOTYsIDExMSwgMTE0LCAxMjAsIDEyMywgMTI5LCAxNDEsIC4uLjxcL3A+XHJcblxyXG48cD5UaGUgbnVtYmVyIG4gaXMgY2FsbGVkIGEgZ2VuZXJhdG9yIG9mIGQobikuIEluIHRoZSBzZXF1ZW5jZSBhYm92ZSwgMzMgaXMgYSBnZW5lcmF0b3Igb2YgMzksIDM5IGlzIGEgZ2VuZXJhdG9yIG9mIDUxLCA1MSBpcyBhIGdlbmVyYXRvciBvZiA1NywgYW5kIHNvIG9uLiBTb21lIG51bWJlcnMgaGF2ZSBtb3JlIHRoYW4gb25lIGdlbmVyYXRvcjogZm9yIGV4YW1wbGUsIDEwMSBoYXMgdHdvIGdlbmVyYXRvcnMsIDkxIGFuZCAxMDAuIEEgbnVtYmVyIHdpdGggbm8gZ2VuZXJhdG9ycyBpcyBhIHNlbGYtbnVtYmVyLiBUaGVyZSBhcmUgdGhpcnRlZW4gc2VsZi1udW1iZXJzIGxlc3MgdGhhbiAxMDA6IDEsIDMsIDUsIDcsIDksIDIwLCAzMSwgNDIsIDUzLCA2NCwgNzUsIDg2LCBhbmQgOTcuPFwvcD5cclxuXHJcbjxwPldyaXRlIGEgcHJvZ3JhbSB0byBvdXRwdXQgYWxsIHBvc2l0aXZlIHNlbGYtbnVtYmVycyBsZXNzIHRoYW4gMTAwMDAgaW4gaW5jcmVhc2luZyBvcmRlciwgb25lIHBlciBsaW5lLjxcL3A+XHJcbiIsImlucHV0IjoiIiwib3V0cHV0IjoiIiwiaGludCI6IiIsIm9yaWdpbmFsIjoiMSIsImh0bWxfdGl0bGUiOiIwIiwicHJvYmxlbV9sYW5nX3Rjb2RlIjoiRW5nbGlzaCJ9XQ==</div>
</div>
</div>