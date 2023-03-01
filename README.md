# 🤸‍♂️ Kiokio - 초중고 인바디 기록 관리 및 조회 솔루션

## 📅 프로젝트 진행 기간

2022.12.2(금) ~ 2022.12.22(목) (21일간 진행)

## 💡 Kiokio - 배경

2022년 정부는 초중고생 체력 증진을 위해 학교체육 활성화를 추진했습니다. 이에 일부 초중고에서는 학교에 체력단련실(헬스장)을 설치하기 시작했고, Kiokio팀은 체력단련실 키오스크에 필요한 인바디 관리 솔루션 개발을 의뢰받았습니다.

메인 기능인 인바디 조회, 관리뿐 아니라 체육 수업에 필요한 출석 체크 기능 포함 관리자 페이지를 만들어 교사가 학생의 인바디 기록을 용이하게 관리할 수 있도록 하였습니다.

## 📌 주요 기능

### 키오스크

#### 출결 확인

```
- 학년반번호를 입력하고 출석을 할 수 있습니다.
- 40분이내 중복출석을 금지합니다.
```

#### 인바디

```
- 학년반번호와 비밀번호 입력 후 인바디 기록을 조회할 수 있습니다.
- 인바디 정보를 조회, 등록, 수정할 수 있습니다.
- 정규식표현을 이용해 입력값이 양식에 맞지 않는 경우 경고창을 띄웁니다.
- 비밀번호를 변경할 수 있습니다.
```

### 운동시설

```
- 체육시설물의 사진과 설명을 조회할 수 있습니다.
```

### 관리자페이지

#### 학생 관리

```
- 학생 정보 조회, 등록, 수정, 삭제를 할 수 있습니다.
- 학년반 혹은 이름으로 학생을 조회할 수 있습니다.
- 키오스크 출결 확인과 인바디 기록 조회에서 쓰이는 학생의 개별 비빌번호를 설정할 수 있습니다.
- 엑셀파일로 학생 정보 리스트를 내려받을 수 있습니다.
```

#### 출결 관리

```
- 학생 출결 정보 조회를 할 수 있습니다.
- 엑셀파일로 학생 출결 정보 리스트를 내려받을 수 있습니다.
- 출결 정보는 수정, 삭제가 불가합니다.
```

#### 인바디 관리

```
- 기간으로 혹은 특정 날짜로 인바디 정보를 조회할 수 있습니다.
- 학년 반 혹은 이름으로 인바디 정보를 조회할 수 있습니다.
- 인바디 정보 등록, 수정, 조회를 할 수 있습니다.
- 엑셀파일로 인바디 정보 리스트를 내려받을 수 있습니다.
- 검사일시, 키, 나이, 체중, BMI, 체지방률은 필수 입력값입니다.
```

#### 정보 등록

```
- 학교 이름과 로고를 등록할 수 있습니다.
- 체육시설물의 사진과 이름, 설명을 등록할 수 있습니다.
```

## 💻 주요 기술

**Backend - Django 3.2.13**

**Frontend - Vue.js 2.7.14**

## 📁 프로젝트 파일 구조

### Back

```
backend
 ┣ accounts
 ┃ ┣ migrations
 ┃ ┃ ┗ __init__.py
 ┃ ┣ __init__.py
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ serializers.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┗ views.py
 ┣ kiosk
 ┃ ┣ __init__.py
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┗ wsgi.py
 ┣ students
 ┃ ┣ migrations
 ┃ ┃ ┗ __init__.py
 ┃ ┣ __init__.py
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ serializers.py
 ┃ ┣ tests.py
 ┃ ┣ urls.py
 ┃ ┗ views.py
 ┣ manage.py
 ┣ requirements.txt

```

### Front

- 계속 리팩토링 중입니다. 변경될 수 있습니다.

```
axios
ㄴaxios.js
router
ㄴindex.js
store
ㄴindex.js
Views
ㄴAdmin
	ㄴ Login // 관리자 로그인 화면 v
	ㄴ Admin // 관리자 메인 화면 v
	ㄴ Student // 학생리스트 조회 화면 v
	ㄴ StudentCreate // 학생리스트 생성 화면 v
	ㄴ StudentUpdate // 학생리스트 수정 화면
  ㄴ StudentDelete // 학생리스트 삭제 화면
  ㄴ Attend // 학생 출결 조회 화면
  ㄴ InbodyHistory // 학생 인바디 기간 검색 화면
  ㄴ InbodyHistory // 학생 인바디 날짜 검색 화면
  ㄴ InbodyStu // 특정 학생 인바디 조회 화면 v
  ㄴ InbodyStuCreate // 특정 학생 인바디 생성 화면
  ㄴ InbodyStuUpdate // 특정 학생 인바디 수정 화면
  ㄴ InbodyStuDelete // 특정 학생 인바디 삭제 화면
  ㄴ InbodyDetail // 특정 인바디 조회 화면
  ㄴ InbodyDetailUpdate // 특정 인바디 수 화면

ㄴKiosk
	ㄴ Index // 키오스크 메인 화면 v
	ㄴ AttendCheck // 출석체크 화면 v
	ㄴ Inbody // 인바디 학번 입력 화면 v
	ㄴ InbodyHistory // 학생의 인바디 전체 기록 화면 v
  ㄴ InbodyDetail // 학생의 인바디 디테일 화면 v
	ㄴ InbodyCreate // 학생의 인바디 등록 화면 v
	ㄴ InbodyUpdate // 학생의 인바디 수정 화면 v
	ㄴ Gym // 운동기구 화면 v

Components
ㄴAdmin
  ㄴcommon
    ㄴButton // 버튼(파랑색, 빨강색, 초록색, 회색) v
    ㄴIconButton // 아이콘 버튼
    ㄴInput // 입력창
  ㄴstudent
    ㄴStudentHeader // 학생 테이블 헤더 v
    ㄴStudentList // 학생 테이블 리스트
    ㄴStudentItem // 학생 테이블 요소
  ㄴattend
    ㄴAttendHeader // 출결 테이블 헤더 v
    ㄴAttendList // 출결 테이블 리스트
    ㄴAttendItem // 출결 테이블 요소
  ㄴinbody
    ㄴInbodyHistoryHeader // 인바디 관리 헤더 v
    ㄴInbodyHistoryList // 인바디 관리 리스트
    ㄴInbodyHistoryItem // 인바디 관리 요소
    ㄴInbodyHistoryItemRecord // 인바디 관리 요소의 하나의 인바디 기록
    ㄴInbodyHeader // 인바디 하나의 기록 헤더
    ㄴInbodyList // 인바디 하나의 기록 리스트
    ㄴInbodyItem // 인바디 하나의 기록 요소
    ㄴInbodyDetailForm // 학생의 인바디 디테일 화면에서의 폼(컨텐츠)
ㄴKiosk
	ㄴcommon
		ㄴKioskHeader // 키오스크 헤더 v
		ㄴTheKeypad // 키패드 v
		ㄴTheModal  // 출석, 운동기구 모달 v
		ㄴTheNumGuide // 반번호 입력 가이드 v
		ㄴPasswordModal // 비밀번호 입력 모달 v
	ㄴInbody
		ㄴ InbodyHistoryItem // 인바디 기록 리스트 v
		ㄴ InbodyDetail // 인바디 상세 기록... DetailView로 옮기기 v
	ㄴGym
		ㄴGymItem // 운동기구 설명 v
```

## 📱 협업 툴

- Git
- Notion

## 🤼‍♂️ 팀원 역할 분배

![members](/README.assets/members.png)

## 📑 프로젝트 산출물

- Design
- API 명세서
- ERD

## Kiokio 서비스 화면

### 키오스크 페이지

  <div>
    <b>출석체크</b>

![attendance](/README.assets/attendance.gif)

  </div>

<div style="display:flex; justify-content:space-between;">

  <div>
    <b>인바디 조회</b>

![inbodyRead](/README.assets/inbodyRead.gif)

  </div>

  <div>
    <b>인바디 등록</b>

![inbodyRead](/README.assets/inbodyCreate.gif)

  </div>

  <div>
    <b>인바디 수정</b>

![inbodyRead](/README.assets/inbodyUpdate.gif)

  </div>
  </div>

  <div>
    <b>운동기구 조회</b>

![retrieveGym](/README.assets/retrieveGym.gif)

  </div>

### 관리자 페이지

<b>로그인 화면</b>

![admin](/README.assets/admin.png)

<b>메인 화면</b>

![adminIndex](/README.assets/adminIndex.png)

<b>학생 조회 및 수정</b>

![retrieveStudent](/README.assets/retrieveStudent.gif)

<b>학생 등록</b>

![createStudent](/README.assets/createStudent.gif)

<b>학생 삭제</b>

- 리팩토링 : 삭제시 confirm창이 나오도록 수정

![deleteStudent](/README.assets/deleteStudent.gif)

<b>출결 조회</b>

<b>인바디 조회</b>

![retrieveInbody](/README.assets/retrieveInbody.gif)

<b>인바디 수정</b>

![updateInbody](/README.assets/updateInbody.gif)

<b>인바디 등록 & 삭제</b>

- 리팩토링 : 삭제시 confirm창이 나오도록 수정

![CDinbody](/README.assets/CDinbody.gif)

<b>운동기구 정보 등록</b>

<b>학교 로고 등록</b>
