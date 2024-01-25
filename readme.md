#### 2023 KAIST MadCamp Week4
###### 이화여자대학교 컴퓨터공학과 황재령, KAIST 전산학부 송한이
# Pro . dev
## *PitchBlend*
### Premier League의 실시간 데이터 집계와 AI를 이용한 분석, 조회, 커뮤니티 기능을 모두 합친 all in one 앱
## 프로젝트 소개
- 크롤링을 통해 4개년 시즌의 모든 팀의 stat, 전술, 날씨에 따른 승률, 홈/원정 승률 등 모든 데이터를 가져와 데이터 전처리를 하고 학습시켜 모델링을 완성하고 이를 통해 홈 화면에서 앞으로의 경기에 승부 예측 기능을 구현<br>
- 이 외에도 예측 라인업 등을 제공한다. (AI 학습)
- 이 외에도 컴퓨터 비전을 이용하여 Big Matches들의 양 팀 선수 인식, 경로 인식, 점유율 반영<br>
- 뉴스 api를 사용하여 premiar league의 trending news와 hot topic news를 분리하여 바인딩. 로그인한 사용자의 지지 팀 정보를 얻어와 필터링하여 검색을 하여 그 팀의 뉴스를 따로 볼 수 있게 하였다.
- 유튜브 api를 이용하여 지지하는 팀의 최근 감독 인터뷰를 불러와 팀 소식에 띄웠다.
- 방대한 양의 데이터들을 모두 실시간으로 연동하여 경기 진행 중 live score, Goal 개수, red/yellow 카드, 승률, 승부, 점유율, 유효슈팅, 오프사이드 횟수 등 모든 정보를 실시간으로 변동될 수 있도록 구현
- community 탭에서는 직관 티켓 예매, 새벽 경기 알람, MOM 투표 등의 기능을 구현




### 회원가입/로그인

<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/168c9359-2767-4651-9c34-eb571eac1947" alt="login" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/bf4e10d2-9902-4bc4-abbf-3b73bc5152b6" alt="logindetail" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/76c627e7-05ed-43f3-9d07-8ecd150da88c" alt="register" width="200"/>
</div>

첫 화면은 하나하나 누끼를 따서 만들었다 ㅎㅎ .. <br>
- 회원가입 시 자신이 응원하는 팀을 하나 선택할 수 있다.
- 이때 이미지에 id를 부여하여 access token으로 함께 전달해 로그인 시 모든 정보에 사용하였다.

### premier league 모든 정보
***
<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/1c0510b0-23a3-4eec-8463-e5b3dc575909" alt="home" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/75644c3d-ad73-497f-8aff-999a54d03ed0" alt="home2" width="200"/>
</div>

#### 1) Previous Matches
지난 경기들의 모든 정보를 볼 수 있음

home 화면에는 위와 같이 경기 팀들과 날짜, 시간, 경기 score 결과를 볼 수 있다.
- 실시간 데이터와 직접 연결했기 때문에 한 경기가 더 치뤄지거나, PL에서 score에 변동을 주면 우리 앱에서도 변동사항이 반영된다.

<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/d00ae304-00ea-49ff-8a16-dcbf1baf563f" alt="booking" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/6d2d5de7-d442-434c-8ad5-19adac443a92" alt="mobile_ticket" width="200"/>
</div>
- 저 Previous Matches에 떠있는 어떤 경기를 선택해 들어가게 되면 hightlights 영상을 유튜브에서 불러오게 된다. 유튜브 api를 사용하면 광고가 계속해서 반복 재생되어서 html 안에서 구글 정보와 유튜브 검색 주소를 쭉 나열해 필터링을 한 후 링크 순서와 함께 각 경기에 함수를 통해 바인딩하였다.
- xG, Shooting 개수, Shots on Target, Corners, Offside, Total Passes, 패스 성공률, 총 점유율, Fouls, 옐로카드와 레드 카드 갯수까지 실제 데이터와 연결하여 집계하였다.


#### 2) Match Schedule
<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/de4df3f9-1ef8-4b94-ba04-402c3c474fb3" alt="detail" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/23c134a8-48eb-460d-a1e8-ced5f093dc6f" alt="detail1" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/2bf2a7cf-b037-4b15-a9a6-27dec4890410" alt="detail2" width="200"/>
</div>
앞으로 다가올 세 경기에 대한 정보
- 실제 데이터에 연결해 오늘 날짜를 기준으로 앞으로의 PL 세 경기를 불러와 바인딩하였다.

[detail]
- 저 중 하나를 클릭하게 되면 상세 화면으로 이동한다.
- Expected Results By AI ) 이 부분은 AI 승부예측이다. 웹 크롤링을 통해 수집한 4개년의 방대한 데이터들을 R 을 이용하여 전처리하고 train, test 데이터로 분류하여 학습시켰다. 이를 바탕으로 각 팀의 매치와 이 모델링을 연동하여 승부 예측을 진행한다. 이 때 최대로 나올 수 있는 골 갯수까지 반영된다.
- Recent 3 Matches는 그 팀들의 이전 승부를 띄우게 된다. 가장 최근 경기는 밑줄을 그어 하이라이팅 했다.
- 그리고 각 팀에서 가장 많은 골을 넣은 선수의 이미지와 골 수까지 불러올 수 있다.
- !! 포인트 !! : 예측 라인업
  -> 각 팀의 부상 업데이트, stat, 감독 스타일을 반영하여 라인업을 예측해준다. 포지션 구조를 짜느라 굉장히 힘들었다 ..



### News Update
***
#### 1) Trending news & Hot topic news
<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/fd356c17-c018-4f90-82c6-cd9b4cb1061c" alt="news_detail" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/83687031-c215-4230-8085-0d49f5b0aabd" alt="tab_news" width="200"/>
</div>

- 뉴스 api를 사용하여 premiar league의 trending news와 hot topic news를 분리하여 바인딩
- 로그인한 사용자의 지지 팀 정보를 얻어와 필터링하여 검색을 하여 그 팀의 뉴스를 따로 볼 수 있게 하였다
- 유튜브 api를 이용하여 지지하는 팀의 최근 감독 인터뷰를 불러와 팀 소식에 헤드라인과 함께 뜰 수 있도록 구현



### Analyzing Big Matches
***
<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/de698117-c11c-4550-8f0d-a87fa500157b" alt="tab3" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/70d44148-2aeb-49b1-96f1-17314fca029e" alt="video_playing" width="200"/>
</div>

![video_detail](https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/43401b0e-b00b-4be2-88b8-f84a03a86da8)

- 팀은 이벤트를 준비하면서 이전 경기 기록과 경기 중 코치에게 전달된 실시간 정보를 기반으로 경기력을 검사하기 위해 AI 지원 스포츠 분석에 그 어느 때보다 더 의존하고 있다. AI는 성공으로 이어지는 패턴을 식별하고 코치에게 팀의 득점 가능성을 극대화하기 위해 최적화할 객관적인 수치를 제공하는 지표를 계산하는 데 사용되고 있는 지표 중 하나는 볼 소유이다. 오픈 소스 추적 라이브러리인 Norfair를 활용하여 비디오 분석 기술을 테스트하고 AI가 경기 비디오를 보면서 자동으로 팀별 공 소유를 계산하는 방법을 보여주는 몇 가지 코드를 작성했다. 



### My Page & Community
***
#### 1) My Page
![myprofile](https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/59b22275-4f2d-491e-af8b-58d6e4588c4e)

1. 회원가입 시 선택했던 팀에 맞게 로고가 띄워지고, 그 팀의 이름이 뜨고 팀의 커뮤니티로 들어갈 수 있다. <br>
2. 선택한 팀의 홈 구장과 위치가 띄워지고 클릭하면 직관 티켓을 예약할 수 있다. 

#### 2) alarm
<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/21bf1ebf-9bca-4116-aa60-9b4a64eb9fcf" alt="alarm" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/7bc65e26-4a26-4b79-a077-127c9d271604" alt="alarm_detail" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/bb3b02aa-1195-42dc-98a8-cdcdb37c4856" alt="alarm_alarm" width="200"/>
</div>

- 해외 축구는 새벽 시간에 경기가 진행되는 경우가 많다.
- 저렇게 알림을 설정해놓으면 앱 자체에서 실제로 알림이 오며 예약을 확인할 수 있다.

#### 3) Community
![community](https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/493b4c5a-a5d1-4aa7-b09f-6af585abd555)

- 팬들이 직접 최근 세 경기 MOM 선수에 대한 평가를 진행한다.
- 찬성/ 반대 투표와 함께 코멘트도 작성할 수 있다.
- 이는 이 팀을 지지하는 사람들끼리 같은 공간을 공유하는 것이며, 다른 팀으로 로그인 된 사람들은 그 팀의 커뮤니티와 팀 선수에만 투표할 수 있도록 accounts user 정보와 데이터베이스 내에서 외래키를 사용해 구현하였다.
- 찬성,반대 투표를 하면 rating으로 반영이 된다. 이는 데이터베이스에 쌓인 정보를 토대로 백엔드 api를 구성하여 프론트에 바인딩 하였다.
- 다른 사람의 코멘트들은 stack 구조를 적용하여 최신 순이 가장 위로 뜨게 구현하였다.

#### 4) Booking
<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/c502284c-938d-4bc5-8c5f-1a1fd7772350" alt="booking" width="200"/>
    <img src="https://github.com/Hwang-Jaeryeong/madcamp_week4_BE/assets/113423770/56ae4239-2c39-46d5-ac04-dcd1971dabb4" alt="mobile_ticket" width="200"/>
</div>
- 아까 My Profile에서 뜬 팀의 홈 구장을 클릭하면 앞으로의 세 경기에 대한 정보와 직관 티켓의 가격이 불러와진다. 이를 클릭하면 이 정보로 구성된 QR 코드를 얻을 수 있다.
