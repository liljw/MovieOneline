# MovieOneline 

MovieOneline은 '영화 한줄평 커뮤니티'로,   
영화에 대한 별점과 한줄평을 가지고 비평과 추천이 이루어지는 사이트이다.

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

- 23.04.11 13:00 pm, MovieOneline 프로젝트 시작.
- 23.04.11 14:30 pm, MovieOneline 모델링 및 README.md 초안 작성 완료.
- 23.04.11 17:00 pm, Movie 모델링 및 관련 model 수정.
- 23.04.11 21:10 pm, Critic/reply update 기능 삭제, movie에 index 기능 추가.

- 23.04.12 10:40 am, like_reply, like_movie 기능 삭제.
- 23.04.12 11:00 am, create_oneline과 동시에 rated_movie에 data 추가 기능 구현.
- 23.04.12 11:30 am, navbar 추가, 서버 활성화 및 버그 수정 시작.
- 23.04.12 12:00 pm, movie API 연동 시작, pip install tmdbsimple, requests.
- 23.04.12 13:30 pm, 검색 기능 추가.
- 23.04.12 14:50 pm, movie 모델링 수정. 
- 23.04.12 23:10 pm, 모든 기능 구현 완료. (백엔드)








