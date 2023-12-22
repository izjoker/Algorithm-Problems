# 1051 
Source URL: https://www.acmicpc.net/problem/1051 
# Description 
<div class="" id="problem-body">
<div class="col-md-12">
<section class="problem-section" id="description">
<div class="headline">
<h2>문제</h2>
</div>
<div class="problem-text" id="problem_description">
<p>N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="input">
<div class="headline">
<h2>입력</h2>
</div>
<div class="problem-text" id="problem_input">
<p>첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="output">
<div class="headline">
<h2>출력</h2>
</div>
<div class="problem-text" id="problem_output">
<p>첫째 줄에 정답 정사각형의 크기를 출력한다.</p>
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
<pre class="sampledata" id="sample-input-1">3 5
42101
22100
22101
</pre>
</section>
</div>
<div class="col-md-6">
<section id="sampleoutput1">
<div class="headline">
<h2>예제 출력 1
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-output-1" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-output-1">9
</pre>
</section>
</div>
</div>
</div>
<div class="col-md-12">
<div class="row">
<div class="col-md-6">
<section id="sampleinput2">
<div class="headline">
<h2>예제 입력 2
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-input-2" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-input-2">2 2
12
34
</pre>
</section>
</div>
<div class="col-md-6">
<section id="sampleoutput2">
<div class="headline">
<h2>예제 출력 2
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-output-2" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-output-2">1
</pre>
</section>
</div>
</div>
</div>
<div class="col-md-12">
<div class="row">
<div class="col-md-6">
<section id="sampleinput3">
<div class="headline">
<h2>예제 입력 3
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-input-3" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-input-3">2 4
1255
3455
</pre>
</section>
</div>
<div class="col-md-6">
<section id="sampleoutput3">
<div class="headline">
<h2>예제 출력 3
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-output-3" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-output-3">4
</pre>
</section>
</div>
</div>
</div>
<div class="col-md-12">
<div class="row">
<div class="col-md-6">
<section id="sampleinput4">
<div class="headline">
<h2>예제 입력 4
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-input-4" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-input-4">1 10
1234567890
</pre>
</section>
</div>
<div class="col-md-6">
<section id="sampleoutput4">
<div class="headline">
<h2>예제 출력 4
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-output-4" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-output-4">1
</pre>
</section>
</div>
</div>
</div>
<div class="col-md-12">
<div class="row">
<div class="col-md-6">
<section id="sampleinput5">
<div class="headline">
<h2>예제 입력 5
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-input-5" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-input-5">11 10
9785409507
2055103694
0861396761
3073207669
1233049493
2300248968
9769239548
7984130001
1670020095
8894239889
4053971072
</pre>
</section>
</div>
<div class="col-md-6">
<section id="sampleoutput5">
<div class="headline">
<h2>예제 출력 5
							<button class="btn btn-link copy-button" data-clipboard-target="#sample-output-5" style="padding: 0px;" type="button">복사</button>
</h2>
</div>
<pre class="sampledata" id="sample-output-5">49
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
</div>