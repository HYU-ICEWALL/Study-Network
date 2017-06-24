## Before Start

실전에 들어가기에 앞서 알아야 할 python 내용. 초심자를 위한 부분.

#### 변수

- 메모리에 저장되어 있는 데이터를 의미함.

```python
>>> port = 21 # port 라는 변수에 정수 저장.
>>> banner = "FreeFloat FTP Server" # 문자열 저장.
# str(port) : 문자열로 변환(cast)하는 과정.
>>> print "[+] Checking for" + banner + "on port " + str(port)
# 출력 결과
[+] Checking for FreeFloat FTP Server on port 21
```

- python에서는 정수, 실수, 불리언(boolean), 문자열 및 리스트와 딕셔너리와 같이 복잡한 데이터를 표현 할 수 있다.

```python
>>> banner = "FreeFloat FTP Server" # A string
>>> type(banner) # 타입 출력 방법
<type 'str'> # 출력결과
>>> port = 21 # An Integer
>>> portlist = [21,22,23,24] # A list
>>> userlist = {21:"127.0.0.1",22:"192.168.0.x",} # A dictionary
>>> portOpen = True # A boolean
```



#### 문자열

- python에서는 문자열 모듈로 강력한 메소드들을 지원한다.
- 문자열 모듈 확인하기 : [python3.x](https://docs.python.org/3/library/string.html) & [python2.x](https://docs.python.org/2/library/string.html)

```python
>>> banner = "FreeFloat FTP Server"
>>> print banner.upper() # FREEFLOAT FTP SERVER
>>> print banner.lower() # freefloat ftp server
>>> print banner.replace('FreeFloat', 'Ability')
# Ability FTP Server / old에 있는 부분을 new로 바꿔준다
>>> print banner.find('FTP') 
# 10 / 찾고 있는 문자열의 위치를 알려준다.
```



#### 리스트

- python에서의 리스트는 객체를 배열로 저장하기에 매우 좋은 수단이다.
- 추가, 삽입, 제거, 인덱스화, 카운트, 정렬 같은 작업을 위한 메소드가 있다.

```python
>>> portList = []
>>> portList.append(21)
>>> portList.append(80)
>>> portList.append(25)
>>> print portList # [21, 80, 25]
>>> print portList.sort() # [21, 25, 80]
>>> pos = portList.index(80)
>>> print "[+] There are " + str(pos) + " ports to scan before 80."
# [+] There are 2 ports to scan before 80.
>>> print portList.remove(21) # [25, 80]
>>> cnt = len(portList)
>>> print "[+] Scanning " + str(cnt) + " Total Ports."
# [+] Scanning 2 Total Ports.
```



#### 딕셔너리

- python 객체를 저장할 수 있는 해시 테이블을 제공한다.
-  키(key)와 값(value)으로 구성되어 있다.
- .keys() : 모든 키 값을 반환 한다.
- .items() : 모든 아이템의 목록을 반환하게 만들 수 있다. 키와 값을 묶은 tuple 객체를 list 안에 넣어서 출력한다.

#### 네트워크 + 선택문

#### 예외 처리

#### 함수

#### 반복문

#### 파일 I/O

