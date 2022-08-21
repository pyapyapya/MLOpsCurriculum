### Getting Start
```
cd pip install -r requirements.txt
cd api/app/
uvicorn main:app --reload
```

### Assignment
- 아래 명세를 만족하는 API를 설계하고 DB를 구축하기

### 유의할 점
- Response 신경쓰기
- 다양한 상황에 대해 message나 code 명확히 보내기
- 다양한 edge case에 대해 500을 내지 않기
- clean code


## API 명세
### 0. Health Check

<br>URI GET /</b><br><br>

<b>Parameters</b>
|Name|Type|Value|Description|Required|
|:----:|:---:|:------:|:------------:|:------:|

<b>Response</b>
|Name|Type|Value|Description|Required|
|:----:|:---:|:------:|:------------:|:------:|
|status|str|"OK"|서버 동작 여부| |



<b>Error Message</b>
|Error code|Message|Description|Required|
|:----:|:------:|:------------:|:------:|

### 1. Get All Users
<b>URI GET /users</b><br><br>
<b>Parameters</b>
|Name|Type|Value|Description|Require|
|:----:|:---:|:------:|:------------:|:------:|

<b>Response</b>
|Name|Type|Value|Description|Require|
|:----:|:---:|:------:|:------------:|:------:|
| | List[TypedDIct{"id": int, "name":str, "age":int}]| | | |


<b>Error Message</b>
|Error code|Message|Description|Require|
|:----:|:------:|:------------:|:------:|

### 2. Get User
<b>URI GET /users/<<id:int>></b><br><br>

<b>Parameters</b>
|Name|Type|Value|Description|Require|
|:----:|:---:|:------:|:------------:|:------:|
|id|int|유저|아이디|YES|

<b>Response</b>
|Name|Type|Description|Require|
|:----:|:----------------------------:|:--------:|:------:|
| |TypedDIct{"id": int, "name":str, "age":int}| | |

<b>Error Message</b>
|Error code|Message|Description|
|:----:|:------:|:------------:|
|404|The user is not found.|해당 유저가 존재하지 않음|
|400|Invalid user id.|id가 유효하지 않음 (int가 아님 등..)|

### 3. Create User
<b>URI POST /users</b> <br><br>
<b>Parameters</b>
|Name|Type|Description|Require|
|:----:|:---:|:------------:|:------:|
|name|str|유저 이름|YES|
|age|int|유저 나이| |


<b>Response</b>
|Name|Type|Description|
|:----:|:---:|:------------:|
|id|int|생성된 유저 아이디|
|name|str|생성된 유저 이름|
|age|int|생성된 유저 나이|

<b>Error Message</b>
|Error code|Message|Description|
|:----:|:------:|:------------:|
|400|"name" paramter is empty.|유저 이름이 존재하지 않음|
|400|"age" must be an integer.|age가 정수가 아님|
|409|The user already exists.|해당 유저 이름이 이미 존재함|

### 4. Update User
<b>URI Put /users/<<id:int>></b> <br><br>
<b>Parameters</b>
|Name|Type|Description|
|:----:|:---:|:------------:|
|name|str|유저 이름|
|age|int|유저 나이|


<b>Response</b>
|Name|Type|Description|
|:----:|:---:|:------------:|
|id|int|수정된 유저 아이디|
|name|str|수정된 유저 이름|
|age|int|수정된 유저 나이|

<b>Error Message</b>
|Error code|Message|Description|
|:----:|:------:|:------------:|
|400|Invalid user id.|id가 유효하지 않음 (int가 아님 등..)|
|400|"age" must be an integer.|age가 정수가 아님|
|404|The user is not found.|해당 유저를 찾을 수 없음|
|409|The user already exists.|해당 유저 이름이 이미 존재함|

### 5. Delete User
<b>URI DELETE /users/<<id:int>></b><br><br>

<b>Parameters</b>
|Name|Type|Description|Required|
|:----:|:---:|:------------:|:------:|
|id|int|유저 아이디|YES|

<b>Response</b>
|Name|Type|Description|
|:----:|:---:|:------------:|
|id|int|삭제된 유저 아이디|
|name|str|삭제된 유저 이름|
|age|int|삭제된 유저 나이|

<b>Error Message</b>
|Error code|Message|Description|
|:----:|:------:|:------------:|
|400|Invalid user id.|id가 유효하지 않음 (int가 아님 등..)|
|404|The user is not found.|해당 유저를 찾을 수 없음|


## DB
<b>Table User</b><br>
|Name|Type|nullable|unique|primary|
|:----:|:---:|:------:|:------------:|:------:|
|id|int|NO|YES|YES|
|name|str|NO|YES|YES|
|age|int|YES|NO|NO|
