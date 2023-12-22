# 1058 
Source URL: https://www.acmicpc.net/problem/1058 
# Description 
<div class="" id="problem-body">
<div class="col-md-12">
<section class="problem-section" id="description">
<div class="headline">
<h2>문제</h2>
</div>
<div class="problem-text" id="problem_description">
<p>지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.</p>
<p>A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="input">
<div class="headline">
<h2>입력</h2>
</div>
<div class="problem-text" id="problem_input">
<p>첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="output">
<div class="headline">
<h2>출력</h2>
</div>
<div class="problem-text" id="problem_output">
<p>첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.</p>
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
<pre class="sampledata" id="sample-input-1">3
NYY
YNY
YYN
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
<pre class="sampledata" id="sample-output-1">2
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
<pre class="sampledata" id="sample-input-2">3
NNN
NNN
NNN
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
<pre class="sampledata" id="sample-output-2">0
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
<pre class="sampledata" id="sample-input-3">5
NYNNN
YNYNN
NYNYN
NNYNY
NNNYN
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
<pre class="sampledata" id="sample-input-4">10
NNNNYNNNNN
NNNNYNYYNN
NNNYYYNNNN
NNYNNNNNNN
YYYNNNNNNY
NNYNNNNNYN
NYNNNNNYNN
NYNNNNYNNN
NNNNNYNNNN
NNNNYNNNNN
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
<pre class="sampledata" id="sample-output-4">8
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
<pre class="sampledata" id="sample-input-5">15
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNYNNNNNNN
NNNNNNNYNNNNNNY
NNNNNNNNNNNNNNY
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNYYNNNNNNNNNNN
NNNNNYNNNNNYNNN
NNNNNNNNNNNNNNY
NNNNNNNNNNNNNNN
NNNNNNNNYNNNNNN
NNNNNNNNNNNNNNN
NNNNNNNNNNNNNNN
YNNYYNNNNYNNNNN
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
<pre class="sampledata" id="sample-output-5">6
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