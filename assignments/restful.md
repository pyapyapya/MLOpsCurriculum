### Restful API

RESTful API를 배우기 전, 먼저 protocol과 API에 대해 알아보자.

<b>프로토콜은 통신을 위해 상호 간 맺는 규약</b>으로, Web Server - Client 통신을 위해 사용되는 것이 HTTP Protocol이다.
HTTP protocol에서는 Request와 Response가 존재하며, response는 request 없이 발생할 수 없다.

HTTP Request는 어떻게 생겼을까?
간단한 코드를 예시로 들면 다음과 같이 나타낼 수 있다.
``` javascript
GET /search?q=test HTTP/2
Host: www.bing.com
User-Agent: curl/7.54.0
Accept: */*
```

이를 세부적으로 알아보자.
- Method: `GET` 에 해당하는 부분으로, resource에 대해 어떤 행동을 하려고 하는지 명시함
  -  `GET`, `POST` , `PUT` , `DELETE` 등이 있음
- HOST: `Host: www.bing.com` 에 해당하는 부분으로, 어느 서버에 가야할 지 표시
- Path: `/search` 에 해당하는 부분으로, Host와 Resource의 위치를 특정함
- Query: `?q=test` 에 해당하는 부분으로, 서버가 요청을 처리하기 위해 추가적으로 필요한 정보를 담음
  - url-encode 형식을 사용함
- protocoal: `HTTP/2` 에 해당하는 부분으로, 명확한 프로토콜을 명시함. 여러가지가 있지만, `HTTP/1.1` 이 보편적
- Headers: `User-Agent: curl/7.54.0` 과 같이  :로 구분된 Key-Value 값에 해당함
  - `User-Agent` 클라이언트의 브라우저, `Accept` 클라이언트가 해석할 수 있는 형식
- Body: `POST` , `PUT` 등 메소드의 요청 시 정보를 첨부하는 곳

---
RESTful API란?

HTTP Respons의 예시는 다음과 같다.
``` javascript
HTTP/1.1 200 OK
Content-Encoding: gzip
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Vary: Accept-Encoding


<!DOCTYPE html>
...
```
- Protocol, Headers, Body는 클라이언트와 동일한 형식
- Status code가 존재하는데, 이는 응답 상태를 알려주는 코드이며, 코드마다 정해진 의미가 있음

### API (Application Programming Interface)
![image](https://user-images.githubusercontent.com/42240862/184858648-a9d0e0d9-9b4c-4c8c-81fd-1fae2b4d4ab1.png)

복잡한 로직을 내부적으로 감추고 단순화해서 하나의 함수, 혹은 end-point 등으로 만든 것
이를 통해, 프로그래머는 내부 로직을 모르더라도 API의 요소(이름, URI ..), 입력, 출력, 형식만 알아도 사용할 수 있음
따라서 API를 통해 어떤 시스템에서 실제로 복잡한 일들을 수행하는 로직을 만들어 놓고, 그 로직에 클라이언트가 접근할 수 있는 API endpoint를 개발하는 것이다.

![image](https://user-images.githubusercontent.com/42240862/184858712-5cf81d2e-b4dc-4964-ab2c-db11b6bab376.png)

이때 가장 많이 사용되는 프로토콜은 HTTP Protocol
HTTP 형식으로 클라이언트에게 API에 요청을 보내고, API 서버는 그 결과를 response로 되돌려줌

---
### Assignment
<b>특정 유저의 돈을 다른 유저에게 전달하는 상황</b>
ex) 3번 사람이 4번 사람에게 1000원 전달

<b>URI</b><br>
POST/transfers

<b>Parameter</b>
|Name|Type|Description|
|:----:|:---:|:------------:|
|sender_id|str|송금자 아이디|
|transfer_money|int|보내는 돈|
|receiver_id|str|수신자 아이디|

<b>Response</b>
|Name|Type|Description|
|:----:|:---:|:------------:|
|sender_id|str|송금자 아이디|
|sender_balance|int|송금자 남은 잔고|
|transfer_money|int|보내는 돈|
|receiver_id|str|수신자 아이디|

<b>Error Message</b>
|error code|message|Description|
|:----:|:---:|:------------:|
|200|송금이 완료되었습니다.|정상 처리|
|400|1원 이상의 돈을 보내야 합니다.|돈을 0원 혹은, 그 이하로 보내려는 시도를 함|
|400|잔액이 부족합니다.|수신자의 잔고가 보내는 돈보다 적음|
|400|해당 유저가 존재하지 않습니다.| 수신자 id가 유효하지 않음
