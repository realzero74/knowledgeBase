# knowledgeBase
> IT 기반 지식을 정리 하기 위한 개인 프로젝트
> 기본 데이터는 기반 지식을 정리 하는 목적.
> 활용 관점으로는 기술사등의 공부를 위한 효율적인 기술 및 이론 정리가 목적.

## 목표 프로젝트 구성 아키텍처
> 3개의 front-end 와 3개의 back-end로 개발 한다.
> 검색 지원을 위한 ELK스택의 도입을 고려한다.

## front-end 기능
> mind-map<br>
> topic<br>
> time-line

## back-end 기능
>back-end는 별거 없다. 단순 저장과 조회를 위한 데이터일뿐 <br>
>단지 단순 저작와 조회를 위한 데이터의 여러 버전을 만들어 보고 싶은 바램일뿐<br>

>일단 구상 가능한 대상은 다음과 같다.
> - 웹어플리케이션 서버
>   - node js
>   - python rest framework
>   - java springboot
> - 저장공간
>   - cvs 파일 기반 - 네트워크 없이 스탠드 얼론으로 동작 가능하게 하기 위해서 고려 해 봤다.
>   - H2 or Sqlite - 역시 경량 DB이면서 스탠드 얼론으로 동작 하능하게 할 수 있다는 점에서 고려.
>   - mariadb - 그냥 저장장치의 끝판
>   - NoSql - mongodb - ELK 스택을 위한 저장 공간으로 고려 해 보고 있다. 향후에 ELK 스택을 공부 하고 나서 더 자세히 고려 해 볼듯.
><br>
><br>

>개발 조합으로는 일단 만만한 순서로
> - java springboot + csv file
> - java springboot + H2


