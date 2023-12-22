# 1057 
Source URL: https://www.acmicpc.net/problem/1057 
# Description 
<div class="" id="problem-body">
<div class="col-md-12">
<section class="problem-section" id="description">
<div class="headline">
<h2>문제</h2>
</div>
<div class="problem-text" id="problem_description">
<p>김지민은 N명이 참가하는 스타 토너먼트에 진출했다. 토너먼트는 다음과 같이 진행된다. 일단 N명의 참가자는 번호가 1번부터 N번까지 배정받는다. 그러고 난 후에 서로 인접한 번호끼리 스타를 한다. 이긴 사람은 다음 라운드에 진출하고, 진 사람은 그 라운드에서 떨어진다. 만약 그 라운드의 참가자가 홀수명이라면, 마지막 번호를 가진 참가자는 다음 라운드로 자동 진출한다. 다음 라운드에선 다시 참가자의 번호를 1번부터 매긴다. 이때, 번호를 매기는 순서는 처음 번호의 순서를 유지하면서 1번부터 매긴다. 이 말은 1번과 2번이 스타를 해서 1번이 진출하고, 3번과 4번이 스타를 해서 4번이 진출했다면, 4번은 다음 라운드에서 번호 2번을 배정받는다. 번호를 다시 배정받은 후에 한 명만 남을 때까지 라운드를 계속 한다.</p>
<p>마침 이 스타 대회에 임한수도 참가했다. 김지민은 갑자기 스타 대회에서 우승하는 욕심은 없어지고, 몇 라운드에서 임한수와 대결하는지 궁금해졌다. 일단 김지민과 임한수는 서로 대결하기 전까지 항상 이긴다고 가정한다. 1 라운드에서 김지민의 번호와 임한수의 번호가 주어질 때, 과연 김지민과 임한수가 몇 라운드에서 대결하는지 출력하는 프로그램을 작성하시오.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="input">
<div class="headline">
<h2>입력</h2>
</div>
<div class="problem-text" id="problem_input">
<p>첫째 줄에 참가자의 수 N과 1 라운드에서 김지민의 번호와 임한수의 번호가 순서대로 주어진다. N은 2보다 크거나 같고, 100,000보다 작거나 같은 자연수이고, 김지민의 번호와 임한수의 번호는 N보다 작거나 같은 자연수이고, 서로 다르다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="output">
<div class="headline">
<h2>출력</h2>
</div>
<div class="problem-text" id="problem_output">
<p>첫째 줄에 김지민과 임한수가 대결하는 라운드 번호를 출력한다. 만약 서로 대결하지 않을 때는 -1을 출력한다.</p>
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
<pre class="sampledata" id="sample-input-1">16 1 2
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
<pre class="sampledata" id="sample-output-1">1
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
<pre class="sampledata" id="sample-input-2">16 8 9
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
<pre class="sampledata" id="sample-output-2">4
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
<pre class="sampledata" id="sample-input-3">1000 20 31
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
<pre class="sampledata" id="sample-input-4">65536 1000 35000
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
<pre class="sampledata" id="sample-output-4">16
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
<pre class="sampledata" id="sample-input-5">60000 101 891
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
<pre class="sampledata" id="sample-output-5">10
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