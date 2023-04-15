# MovieOneline 

> MovieOneline은 영화에 대한 별점과 한줄평을 가지고 비평이 이루어지는 사이트이다.

## 개요

해당 프로젝트는 **멀티캠퍼스 - 융복합PJT 데이터 분석 8회차 과정의 인터페이스 개발 프로젝트**이다.  
2023.04.11 ~ 2023.04.13 총 60시간이 주어졌으며,  
제한 시간 안에 웹 서버를 만드는 것을 목표로 한다.  

주어진 시간이 많지 않다고 생각하여,  
기본적으로는 기존 수업시간에 배웠던 게시판의 형태를 띄되,  
다른 기능을 하나 추가하여 그 두 가지가 접목된 형태의 웹 서버를 개발하고자 한다. 

**그래서 tmdb라는 영화 정보 사이트의 Open API를 이용하여,   
MovieOneline이라는 '영화 한줄평 리뷰 커뮤니티'를 구상하였다.**

---

## 목차

1. 프로젝트 결과
2. Modeling
3. Function
4. 개발 Timeline
5. 개발 후기

---

## 프로젝트 결과 

1. Index 페이지 (Home 화면)

<img width="1680" alt="02_index_authenticated" src="https://user-images.githubusercontent.com/129480514/232194309-7bda4e38-6a52-4d0d-a6f2-0efb49e17c25.png">


- 네비게이션 바 
    - 로그인이 안된 상태에서는 (Home, Login, Signup) 으로 이동할 수 있는 링크가,
    - 로그인이 된 상태에서는 (Home, My Profile, Log Out) 의 링크를 navbar에 포함시켜 주었다. 
- 검색창 
    - tmdb사이트의 Open API를 이용해 사용자가 검색창에 영화 제목을 입력하면, 해당 영화 제목을 포함하는 모든 영화가 리스트 업 된 검색 결과 화면이 나타난다. 
- 최신 영화 
    - 가장 최근에 db에 추가된 영화들의 포스터가 index 화면에 나타나게 했고, 포스터를 누르면 해당 영화의 detail 페이지로 이동하는 태그를 포함해주었다. 

2. My Profile 페이지 

<img width="1680" alt="03_profile" src="https://user-images.githubusercontent.com/129480514/232194750-f17585e4-381c-4932-a04c-67ad4abe6cdf.png">

- 팔로우
    - 유저들간 서로 팔로우가 가능하도록 구현해주었다.
    - 자기 자신은 팔로우가 불가능하며, 로그인이 된 상태에서만 가능하다. 
    - A가 B를 팔로우해도, B가 A를 팔로우 하지는 않는다. `(symmetrical=False)`
- 내가 본 영화
    - 해당 유저가 별점과 한줄평을 등록한 영화들의 포스터가 나타난다. 
    - 포스터를 클릭하면 해당 영화의 detail 페이지로 이동.
- 내가 쓴 한줄평 모음 
    - 내가 지금까지 한줄평을 등록했던 리스트가 나타난다.
    - 영화 제목에는 detail 페이지로 이동하는 링크가 걸려있다. 
- 내가 좋아요 한 한줄평
    - 내가 좋아요 버튼을 누른 다른 사람의 한줄평이 나타나도록 했다. 
    - 유저 이름을 클릭하면 해당 유저의 프로필 페이지로 이동한다. 

3. 영화 Detail 페이지

<img width="1359" alt="04_detail_02" src="https://user-images.githubusercontent.com/129480514/232196340-318b9216-5617-43f5-91b4-24c348552ff2.png">

- 영화 정보 
    - 상단부터 영화 제목, 포스터 이미지, 개봉일자, 러닝타임의 정보가 나타나게끔 했다. 
- 한줄평 작성란 
    - 만약 유저가 해당 영화에 대해 한줄평을 작성하지 않았다면,  
    '한줄평을 등록해주세요' 라는 문구와 함께, 한줄평 작성란과 별점 입력 칸이 나타난다. 
    - 한줄평을 작성한 유저라면, 작성칸이 나타나지 않는다. *(중복 작성 불가)*
- 한줄평 목록
    - 유저 이름과 별점, 한줄평이 목록에 나열된다. 
    - 유저 이름에는 해당 유저의 프로필로 이동하는 링크를 걸어주었다. 
    - 한줄평에 *'좋아요'*를 누를 수 있는 버튼과, 그 안에 좋아요 개수가 보이게끔 구현해주었다. 
    - 이미 해당 한줄평에 좋아요를 누른 유저라면, *'좋아요 취소'* 버튼이 보인다.
    - 한줄평의 경우는 자기 자신이 좋아요를 누를 수 있게 해주었다.
- 한줄평 수정 및 삭제
    - 내가 작성한 한줄평 밑에는 수정 및 삭제 버튼이 나타난다. 
    - 수정은 기존에 작성한 한줄평의 내용이 포함되어있는 새로운 form이 반환된다. 
- 댓글 
    - 한줄평의 밑에는 댓글 등록할 수 있는 버튼과 작성란이 있다. *(중복 작성 가능)*
    - 작성란 아래에는 댓글 목록이 있는데, 그 중 본인의 댓글은 '댓글 삭제' 버튼이 보이게끔 구현하였다. 
    - 댓글이 없는 한줄평의 경우, 댓글 목록 대신 *'아직 댓글이 없어요 :('*라는 문구가 나타난다. 

4. 검색 결과 페이지

<img width="1240" alt="05_search" src="https://user-images.githubusercontent.com/129480514/232197360-9b046f06-2106-4c10-a0f3-dd0df85d9c64.png">

- 초기 홈 화면의 검색창에 'Harry Potter'라고 검색하면,  
tmdb 사이트 내에 'Harry Potter'라는 단어를 포함한 모든 영화의 제목이 나열된다. 
- 영화 제목을 클릭하면, 클릭과 동시에 서버 db에 해당 영화의 정보가 저장되고, detail 페이지가 반환된다. 

5. 회원가입 / 로그인 페이지

<img width="1680" alt="06_signup" src="https://user-images.githubusercontent.com/129480514/232197599-8b7a582c-3f14-4678-b931-cf578fa7d3ac.png">

<img width="1680" alt="06_login" src="https://user-images.githubusercontent.com/129480514/232197616-55272e06-5976-482f-9890-97508773c214.png">

- 회원가입과 로그인 페이지로, 사용자가 입력한 정보가 유효하지 않다면, 결과 값이 반환되지 않는다. 
- 다른 페이지와 마찬가지로 부트스트랩을 적용해주었다. 


---

## Modeling

- Accounts
    - User
        - follow (M:N)
        - like_oneline (M:N)
        - rated_movie (M:N)

- Movie
    - Movie
        - title
        - poster
        - released_date
        - running_time

- Critic
    - Oneline
        - movie (1:N)

    - Reply
        - Oneline (1:N)

---

## Function

- User
    - signup
    - signin
    - signout
    - profile
        - userinfo (name)
            - follower (count)
                - follower list (link to profile)
            - following (count)
                - following list (link to profile)
        - movies
            - movies list (sorted by rating)
        - onelines
            - onelines list (sorted by like_oneline)
        - like_oneline 
            - like_oneline list (sorted by like_oneline)
        - replies (user only)
            - replies list (sorted by updated_at)
    - follow

- Movie
    - detail
        - movieinfo
            - movie attributes
        - critic
            - critic form
            - critic list (user : rating, oneline)
                - like_oneline
                - reply form
                - reply list
                    - like_reply
    - index
        - search input
    - search
        - search result list
        
- Critic
    - oneline
        - create_oneline
            - add rated_movie
        - update_oneline
        - delete_oneline
    - reply
        - create_reply
        - delete_reply
    - like
        - like_oneline

- Navbar
    - Home
    - if authenticated
        - My Profile
        - Log out
    - else
        - Log in
        - Sign up

                



---

## Timeline

1. 1일차
    - 23.04.11 13:00 pm: MovieOneline 프로젝트 시작.
    - 23.04.11 14:30 pm: MovieOneline 모델링 및 README.md 초안 작성 완료.
    - 23.04.11 17:00 pm: Movie 모델링 및 관련 model 수정.
    - 23.04.11 21:10 pm: Critic/reply update 기능 삭제, movie에 index 기능 추가.

2. 2일차
    - 23.04.12 10:40 am: like_reply, like_movie 기능 삭제.
    - 23.04.12 11:00 am: create_oneline과 동시에 rated_movie에 data 추가 기능 구현.
    - 23.04.12 11:30 am: navbar 추가, 서버 활성화 및 버그 수정 시작.
    - 23.04.12 12:00 pm: movie API 연동 시작, pip install tmdbsimple, requests.
    - 23.04.12 13:30 pm: 검색 기능 추가.
    - 23.04.12 14:50 pm: movie 모델링 수정. 
    - 23.04.12 23:10 pm: 모든 기능 구현 완료. (백엔드)

3. 3일차
    - 23.04.13 09:00 am: html 이미지 파일 깨지는 현상 해결.
    - 23.04.13 10:00 am: bootstrap 적용 시작, pip install django-bootstrap-v5
    - 23.04.13 15:00 pm: 1차 front-end 작업 완료. 
    - 23.04.13 15:30 pm: tmdb_pk, oneline 중복 문제 발견 
    - **23.04.13 16:00 pm: 프로젝트 'MovieOneline' 발표.**

4. 추가 수정
    - 23.04.15 11:00 am: movie 모델링에 tmdb_pk column 추가, 기존 detail view 함수로 이동되는 url들 모두 tmdb_pk로 변경 완료. 
    - 23.04.15 11:30 am: oneline_edit.html 수정 완료. oneline 중복 문제 해결. 모든 view 함수에 decorators 추가 완료.
    - 23.04.15 11:30 am: index나 profile에서 정해진 수의 poster만 보여주고 싶은데, db에 있는 모든 데이터를 가져오는 문제 발견.
    - 23.04.15 17:30 pm: 위의 문제 slicing으로 해결, README.md 수정 완료.



---

## 개발 후기

- 잘한 점
    1. Open API를 써보는게 처음이어서 많이 헤맸지만, 결국 연동에 성공하고 원하는 정보를 가져올 수 있었다.
    2. 프론트엔드쪽은 거의 지식이 없는 상태에서 시도해봤지만, 템플릿을 쓰지 않고 직접 여러가지를 시도하였다. 
    3. 필수적으로 구현해야 했던 기능을 제외하고, 시간 내에 구현하기 힘들 것 같다고 생각이 들면 과감하게 삭제하였다. 
    4. 수업시간에 배웠던 내용들은 거의 다 적용할 수 있게끔 평소에 복습을 철저히 했던 것과, 나아가서 한 단계 더 발전하려고 한 것.

- 아쉬운 점
    1. 초기 모델링 할 때 내가 API를 사용해서 어떤 정보들을 가져올 수 있는지 모르는 상태로 모델링을 한 결과, 영화쪽은 나중에 상당부분 모델링을 수정해야했다. 
        - 다음부터는 API 사용법을 좀 더 익혀서 도전해보자.
    2. 검색 결과가 영어로만 반환되는 것. 
        - 검색 자체는 한국어로도 가능하지만, 반환되는 값이 영어만 가능한 줄은 몰랐다.  
        이 역시 기존에 모델링 단계에서 tmdb가 제공해주는 API에 대한 문서를 더 자세히 읽어봐야 했었다. 
    3. 검색 결과 반환 html에 조금 더 많은 정보가 포함되게끔 했으면 좋았을 것 같다. 
        - 이 경우는 시간이 더 있었으면 충분히 구현가능했을 것 같다. 
    4. tmdb의 id와 내 서버의 영화 id가 detail view함수 내에서 충돌했던 점. 
        - 이 에러를 발견하지 못했던 것은 너무 적은 양의 데이터만 가지고 서버를 돌려봤던 이유가 큰 것 같다. 
        - 앞으로는 어느 정도 충분한 양의 데이터를 만들어놓고 서버를 이것저것 테스트하는 시간을 꼭 가져야 할 것 같다. 







