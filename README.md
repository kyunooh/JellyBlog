[![Build Status](https://travis-ci.org/kyunooh/JellyBlog.svg?branch=master)](https://travis-ci.org/kyunooh/JellyBlog)

<h2>도저히 워드프레스를 못쓰겠어서 그냥 제가 블로그를 만들었습니다.</h2>

<p>워드프레스로 블로그를 운영하고 있었는데, 어느 순간부터 워드프레스가 굉장히 무거워졌습니다.</p>

<p>지속적으로 최적화를 하려 했지만,&nbsp;더 이상 가상서버에서 돌릴 수 없겠다라고 판단,&nbsp;결국 그냥 처음부터 다시 만들어 버렸습니다. &nbsp;</p>

<p><strong>젤리 블로그 프로젝트의 목표는 결국 저를 위한 것이며,</strong>&nbsp;<strong><span style="color:rgb(255, 0, 0)">필수 기능과 제가 필요한 기능</span>들만 조금씩 추가하면서&nbsp;발전하는 블로그를 목표</strong>로 하고 있습니다.&nbsp;</p>

<h3>사용된 소스는 모두 공개합니다.</h3>

<p>소스는 모두&nbsp;오픈소스로 공개하지만, 아무래도 저 혼자 하는 프로젝트여서,&nbsp;</p>

<p>혹 다른분들이 사용하실 때에는 각자에 맞게 커스터마이징이 필요하며,</p>

<p><strong>사실 재사용성을 염두에 두고 만든 프로젝트는 아닙니다.</strong>&nbsp;</p>

<p>참고용 정도로만 사용하시길 권합니다 ㅎㅎ (소스코드도 더러운(?) 부분이 좀 많습니다.)</p>

<p>블로그에 사용된 소스 라이브러리(프레임워크)는 아래와 같으며</p>

<p><a href="https://www.djangoproject.com/">django</a>와 그외 여러가지 모듈(<a href="http://www.pymysql.org/">pymysql</a>,&nbsp;<a href="https://github.com/django-ckeditor/django-ckeditor">ckeditor</a>,&nbsp;<a href="http://django-compressor.readthedocs.org/en/latest/">compressor</a>&nbsp;등등)<br />
<a href="http://getbootstrap.com/">Bootstrap3</a></p>

<p>&nbsp;</p>

<p>실제 구동되고 있는 블로그 환경은 아래와 같습니다.</p>

<p>Ubuntu(<a href="http://aws.amazon.com/">AWS</a>&nbsp;프리티어)<br />
<a href="http://www.python.org/">python</a>&nbsp;3.4.4<br />
<a href="https://mariadb.org/">MariaDB</a>&nbsp;10.0</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<h4>갑자기 웬 파이썬?</h4>

<p>사실 제겐 자바가 가장 익숙한 언어지만, JVM이&nbsp;굉장히 메모리를 잡아먹고,</p>

<p>블로그에 사용하기엔 오버스펙이라고 생각되었습니다.&nbsp;</p>

<p>또 php를 사용하기엔 웹서버 설정등등이 너무 귀찮게 느껴졌습니다.</p>

<p>그래서 전부터 관심은 있었지만 실제로 배워본적은 없든&nbsp;파이썬을 살펴보고,</p>

<p>django라는 프레임워크를 조사해봤는데 굉장히 쉽고 빠르면서, 유용하게 느껴져 파이썬을 선택하게 되었습니다.</p>

<p>또한 django는&nbsp;백엔드와 프론트엔드가 분리된 느낌이 없는데, servlet + jsp와는 다른 느낌입니다.</p>

<p>모든게&nbsp;하나가 되어 유연하게 작업하는 느낌이 신선하고&nbsp;재밌습니다.</p>

<p>(추가로 파이썬이란 언어는&nbsp;굉장히 실용적이어서, 언어를 처음 배우고 블로그를 완성하기까지 3주정도 소요된것 같습니다.)</p>

<h3>앞으로 추가해야할 기능들</h3>
<p><strong>bold 처리한 것은 v0.5까지 목표</strong></p>
<p><strong>웹표준 짱짱 준수 (W3C Validator 및 조은님 검증기 통과)</strong></p>
<p><strong>최종 수정 시간 에러 수정</strong></p>
<p><strong>메인 san serif적용</strong></p>
<p><strong>포스트 썸네일 메타태그 적용</strong></p>
<p>about me update</p>

<p>업데이트  기록</p>
<h5>v0.4<h5>
<p>블로그 내부 검색 기능</p><br />
<p>생활 블로그와 기술 블로그 분리</p></br>

<h5>v.0.3</h5>
<p>글목록 정렬  버그 수정</p>
<p>about me 페이지 완성</p>

<h5>v.0.22</h5>
<p>댓글 기능<br />
모바일 버전 최적화<br />
Home 페이지(index) 수정&nbsp;<br />
<strong>검색 관련 최적화(구글 웹마스터용 사이트맵 제작 및 네이버 신디케이션 연동 등등)</strong><br />
<br />

<h5>v.0.21</h5>

<p><small><tt>임시 저장 기능 추가</tt></small></p>

<p>&nbsp;</p>

<h5>v0.11</h5>

<p><small><tt>Favicon 적용&nbsp;</tt></small><br />
<small><tt>소스 리팩토링 등등</tt></small><br />
<small><tt>페이스북 및 트위터 아이콘 추가</tt></small></p>

<p>&nbsp;</p>

<h4>그외&nbsp;정보</h4>

<p>제작자 : 젤리(최현묵)</p>

<p>이메일 : chm073@gmail.com</p>

<p>프로젝트 GitHub url : &nbsp;https://github.com/kyunooh/JellyBlog</p>
