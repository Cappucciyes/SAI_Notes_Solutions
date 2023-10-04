# Pandas
`Series`와 `DataFrame`으로 이뤄짐. NumPy의 스프레드시트 응용버전이라 생각하면 편함. NumPy의 함수, 기능 가능함!

- 이점
	- 넘파이 사용. ==> 수학적 작업에 효율적임
	- 엑셀에서 가능한 스프레드시트 기능들 가능
	- 파이썬으로 데이터를 통해 직접 무언가를 하는 프로그렘 작성 가능 (엑셀에서는 불가)

## 함수
- `read_csv(filename, delimiter=None, header=)`: 데이터프래임 반환. csv파일을 기반으로 데이터프래임을 불러옴
	- `filename` : 여기에 전달된 파일 위치 (또는 URL)로부터 파일 읽
	- `delimiter`: `filename.txt`에서 각 데이터를 구분하는 기호는 " "(delimiter)임을 알려주고, 이를 토대로 `DataFrame` 만듬. 만일 csv 처럼`filename.txt`에 각 데이터가 기호 ","로 구분되어있으면  `read_csv(filename.txt)` 만 적어도 됨.
	- `header`: 만일 첫 행이 데이터 이름이 아니라면 (헤더가 없다면) 이 함수는 기본적으로 첫번째 행을 헤더로 보기에 `DataFrame`이 이상하게 나온다. 즉 헤더가 없으면 `header=None`으로 헤더 인수에 `None`을 넣어 헤더가 알아서 채워진 `DataFrame`이 만들어지도록 한다. (기본적으로 숫자를 체워넣는데, 첫 열은 0, 두번째 열은 1,... 방식으로 채움) 
	- `names`: 만일 헤더 이름을 넣고 싶으면 헤더 이름이 담긴 list를 names에 넣으면 된다.ex: `names=['name', 'is','here']`
## 클래스
- `Series`: 1차원 배열, `numpy.ndarray` 서브클래스 ==> `numpy.ndarray` 의 기능 다 활용가능 (인덱싱 등등)
	- 선언 방법: `pandas.core.series.Series(iterable)` 함수 호출 
	- 특징 및 기능
		- 1차원 `numpy.ndarray` 처럼 다룰 수 있다.
		- `numpy.ndarray`와 달리, 각 원소의 인덱스에 이름을 붙일 수 있고, 그 인덱스 이름으로 인덱싱 가능하다.
- `DataFrame`: `Series`로 이루워진 2차원 배열. 엑셀과 비슷함
	- 선언 방법: `pandas.DataFrame()`
		- 이때, `pandas.DataFrame(data=dict(col1=list1, col2=list2))` 처럼 선언하면, 열의 이름이 각각 `col1`, `col2`이고,  각 열이 `list1`,`list2` 의 원소들로 채워진 `DataFrame`이 만들어짐
		- 다른 `DataFrame`을 기반으로 새로운 `DataFrame` 만들 수 있음.
			- `pd.DataFrame(df, columns=[1,2,3])` : 원래 있었던 `df`라는 데이터프레임에서 열의 인덱스가 1,2,3인 것만 모아서 새로운 `DataFrame` 선언
			- `pd.DataFrame(df, columns=[*df.columns,"new"])`: 원래 있었던 `df`라는 데이터프레임에서 모든 열 + "new"라는 새로운 열을 포함한 새로운 `DataFrame` 선언
	- 특징 및 기능
		- `df`라는  `DataFrame`이 있다고 하자. 
		- `df[0]`, `df[1]` 이렇게 숫자로 인덱하면 각각 첫번째 행(`Series`), 두번째 행을 보여준다. => 인덱싱이 가능하다. `df[1:3]`
		- `Series`처럼 각 열과 행의 인덱스를 자신이 원하는 걸로 정하고, 그걸 토대로 인덱싱 가능
	- 메소드
		- `head(n)`: 첫번째 `n`행 보여줌
		- `tail(n)`: 마지막 `n`행 보여줌
		- `to_csv(DataFrame, index=True, header=True, na_rep='')`: `DataFrame`을 csv 파일로 컴퓨터에 저장
			- `DataFrame`: csv로 저장할 `DataFrame`
			- `index`: csv를 저장할 때 인덱스도 같이 저장할지 말지 결정함. 기본값은 True(저장 됨)
			- `header`: csv를 저장할 때 헤더도 같이 저장할지 말지 결정함. 기본값은 True(저장 됨)
			- `na_rep`: 빈 칸(그 자리에 데이터가 없음)을 저장할 때, 그 자리에 넣고 싶은 것을 말해줌 (예를 들면 빈칸을 '-'로 표시하고 싶을 때). 기본값은 ''(빈 문자열).
		- `loc[index]`:`index`(`index`는 `str`)에 있는 `Series`모두 반환, 만일 index가 list인 경우 `Series`들로 만들어진 `DataFrame` 반환. index 주소가 아니라 인덱스 이름이 맞는 것들 불러옴
	- 속성
		- `columns`: 각 열의 이름. 데이터프레임 `df` 가 있다면 `df.columns = ["a", "b", "c"]` 이런식으로 지정 가능
		- `values`: NumPy(예를 들면 `ndarray`)에서 출력하듯이 데이터프레임 출력
