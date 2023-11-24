# 1021 
Source URL: https://www.acmicpc.net/problem/1021 
# Description 
<div class="" id="problem-body">
<div class="col-md-12">
<section class="problem-section" id="description">
<div class="headline">
<h2>문제</h2>
</div>
<div class="problem-text" id="problem_description">
<p>지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.</p>
<p>지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.</p>
<ol>
<li>첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a<sub>1</sub>, ..., a<sub>k</sub>이었던 것이 a<sub>2</sub>, ..., a<sub>k</sub>와 같이 된다.</li>
<li>왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a<sub>1</sub>, ..., a<sub>k</sub>가 a<sub>2</sub>, ..., a<sub>k</sub>, a<sub>1</sub>이 된다.</li>
<li>오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a<sub>1</sub>, ..., a<sub>k</sub>가 a<sub>k</sub>, a<sub>1</sub>, ..., a<sub>k-1</sub>이 된다.</li>
</ol>
<p>큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="input">
<div class="headline">
<h2>입력</h2>
</div>
<div class="problem-text" id="problem_input">
<p>첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="output">
<div class="headline">
<h2>출력</h2>
</div>
<div class="problem-text" id="problem_output">
<p>첫째 줄에 문제의 정답을 출력한다.</p>
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
<pre class="sampledata" id="sample-input-1">10 3
1 2 3
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
<pre class="sampledata" id="sample-output-1">0
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
<pre class="sampledata" id="sample-input-2">10 3
2 9 5
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
<pre class="sampledata" id="sample-output-2">8
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
<pre class="sampledata" id="sample-input-3">32 6
27 16 30 11 6 23
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
<pre class="sampledata" id="sample-output-3">59
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
<pre class="sampledata" id="sample-input-4">10 10
1 6 3 2 7 9 8 4 10 5
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
<pre class="sampledata" id="sample-output-4">14
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