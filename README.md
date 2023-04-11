# MovieOneline 

MovieOneline은 '영화 한줄평 커뮤니티'로,   
영화에 대한 별점과 한줄평을 가지고 비평과 추천이 이루어지는 사이트이다.

---

## Modeling

- Accounts
    - User
        - follow (M:N)
        - like_oneline (M:N)
        - like_reply (M:N)
- Movies

- Critics
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
    - like
        - like_oneline
        - like_reply
        - like_movie
    - follow

- Movies
    - detail
        - movieinfo
            - poster img
            - director
            - actors
            - rating
            - etc
        - critic
            - critic form
            - critic list (user : rating, oneline)
                - like_online
                - reply form
                - reply list
                    - like_reply
        
- Critics
    - oneline
        - create_oneline
        - edit_oneline
        - delete_oneline
    - reply
        - create_reply
        - edit_reply
        - delete_reply
                



---

## Timeline

- 23.04.11 13:00 pm, MovieOneline 프로젝트 시작.
- 23.04.11 14:30 pm, MovieOneline 모델링 및 README.md 초안 작성 완료.
- 

