# 1059 
Source URL: https://www.acmicpc.net/problem/1059 
# Description 
<div class="" id="problem-body">
<div class="col-md-12">
<section class="problem-section" id="description">
<div class="headline">
<h2>문제</h2>
</div>
<div class="problem-text" id="problem_description">
<p>정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.</p>
<ul>
<li>A와 B는 양의 정수이고, A &lt; B를 만족한다.</li>
<li>A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.</li>
</ul>
<p>집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="input">
<div class="headline">
<h2>입력</h2>
</div>
<div class="problem-text" id="problem_input">
<p>첫째 줄에 집합 S의 크기 L이 주어진다. 둘째 줄에는 집합에 포함된 정수가 주어진다. 셋째 줄에는 n이 주어진다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="output">
<div class="headline">
<h2>출력</h2>
</div>
<div class="problem-text" id="problem_output">
<p>첫째 줄에 n을 포함하는 좋은 구간의 개수를 출력한다.</p>
</div>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="limit">
<div class="headline">
<h2>제한</h2>
</div>
<div class="problem-text" id="problem_limit">
<ul>
<li>1 ≤ L ≤ 50</li>
<li>집합 S에는 중복되는 정수가 없다.</li>
<li>집합 S에 포함된 모든 정수는 1보다 크거나 같고, 1,000보다 작거나 같다.</li>
<li>1 ≤ n ≤ (집합 S에서 가장 큰 정수)</li>
</ul>
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
<pre class="sampledata" id="sample-input-1">4
1 7 14 10
2
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
<pre class="sampledata" id="sample-output-1">4
</pre>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="sample_explain_1">
<div class="problem-text" id="problem_sample_explain_1">
<p>[2,3], [2,4], [2,5], [2, 6]</p>
</div>
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
<pre class="sampledata" id="sample-input-2">5
4 8 13 24 30
10
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
<pre class="sampledata" id="sample-output-2">5
</pre>
</section>
</div>
<div class="col-md-12">
<section class="problem-section" id="sample_explain_2">
<div class="problem-text" id="problem_sample_explain_2">
<p>[9, 10], [9, 11], [9, 12], [10, 11], [10, 12]</p>
</div>
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
10 20 30 40 50
30
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
<pre class="sampledata" id="sample-output-3">0
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
<pre class="sampledata" id="sample-input-4">8
3 7 12 18 25 100 33 1000
59
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
<pre class="sampledata" id="sample-output-4">1065
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