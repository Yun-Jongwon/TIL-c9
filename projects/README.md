# 1.

테이블 구성하기

```sqlite
CREATE TABLE movies(
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' DATE,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
.mode csv 
.import boxoffice.csv movies
.headers on
.mode column
```

전체데이터출력

```sqlite
SELECT * FROM movies;
```

# 2.

데이터 추가

```sqlite
INSERT INTO movies(
    
    '영화코드' ,
    '영화이름' ,
    '관람등급' ,
    '감독' ,
    '개봉연도' ,
    '누적관객수' ,
    '상영시간',
    '제작국가' ,
    '장르' ) VALUES(20182530,'극한직업','15세이상관람가','이병헌','20190123',3138467,111,'한국','코미디')
```

2. 데이터 수집과정에서 실수로 과거의 데이터가 포함되었습니다. 영화코드가 20040521인 데
  이터를 출력하세요. 그리고, 해당 데이터를 삭제하세요.

3. 영화코드 20185124인 데이터를 출력하세요. 공란으로 되어 있는 컬럼에 값을 '없음'으로 수
  정하세요. 그리고 해당 데이터의 감독이 변경되었는지 확인하세요.

  ```sqlite
  --2
  SELECT * FROM movies WHERE 영화코드=20042530;
  DELETE FROM movies WHERE 영화코드=20042530;
  --3
  SELECT * FROM movies WHERE 영화코드=20185124;
  UPDATE movies SET 감독='없음' WHERE 영화코드=20185124;
  SELECT * FROM movies WHERE 영화코드=20185124;
  ```


# 3.

1. 상영시간이 150분 이상인 영화이름만 출력하세요.

2. 장르가 애니메이션인 영화코드와 영화이름를 출력하세요.

3. 제작국가가 덴마크이고 장르가 애니메이션인 영화이름을 출력하세요.

4. 누적관객수가 백만이 넘고, 관람등급이 청소년관람불가인 영화이름과 누적관객수를 출력하세
  요.

5. 개봉연도가 2000년 1월 1일 ~ 2009년 12월 31일 사이인 영화를 출력하세요.

6. 장르를 중복 없이 출력하세요.

   ```sqlite
   --1
   SELECT 영화이름 FROM movies WHERE 상영시간 >= 150;
   --2
   SELECT 영화코드, 영화이름 FROM movies WHERE 장르='애니메이션';
   --3
   SELECT 영화이름 FROM movies WHERE 제작국가='덴마크';
   --4
   SELECT 영화이름,누적관객수 FROM movies WHERE 누적관객수>=1000000 and 관람등급='청소년관람불가';
   --5
   SELECT 영화이름 FROM movies WHERE 개봉연도 LIKE '200%';
   --6
   SELECT DISTINCT 장르 FROM movies; 
   ```


# 4.

1. 모든 영화의 총 누적관객수를 출력하세요.
2. 가장 많은 누적관객수인 영화이름과 누적관객수를 출력하세요.
3. 가장 상영시간이 짧은 영화의 장르와 상영시간을 출력하세요.
4. 제작국가가 한국인 영화의 평균 누적관객수를 출력하세요.
5. 관람등급이 청소년관람불가인 영화의 개수를 출력하세요.
6. 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수를 출력하세요.

```sqlite
--1
SELECT SUM(누적관객수) FROM movies;
--2
SELECT 영화이름,MAX(누적관객수) FROM movies;
--3
SELECT 장르,MIN(상영시간) FROM movies;
--4
SELECT AVG(누적관객수) FROM movies WHERE 제작국가='한국';
--5
SELECT COUNT(*) FROM movies WHERE 관람등급='청소년관람불가';
--6
SELECT COUNT(*) FROM movies WHERE 상영시간>=100 and 장르='애니메이션';
```

# 5.

1. 누적관객수 상위 5개 영화의 모든 데이터를 출력하세요.

2. 장르가 애니메이션인 영화를 제작국가(오름차순), 누적관객수(내림차순)순으로 정렬하여 10개
  만 출력하세요.

3. 상영시간이 긴 영화를 만든 감독의 이름을 10개만 출력하세요.

   ```sqlite
   --1
   SELECT * FROM movies ORDER BY 누적관객수 DESC LIMIT 5;
   --2
   SELECT* From movies ORDER BY 제작국가 ASC, 누적관객수 DESC LIMIT 10;
   --3
   SELECT DISTINCT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10 ;
   ```
