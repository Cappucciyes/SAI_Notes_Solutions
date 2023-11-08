# Matplotlib
```python
import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,8]

plt.plot(x,y)
```

한글은 폰트 설정을 해야 사용가능하다.
- `matplotlib.rcParams['font.family']`=`원하는 한글 폰트`
- 사용가능한 폰트는 `matplotlib.font_manager.fontManager.ttflist`로 확인 가능
- 한글 폰트를 사용하면 표에 표시되는 마이너스(-) 기호가 깨진다. `matplotlib.rcParams['axes.unicode_minus']=False` 를 적어 한글 폰트를 사용하면서 마이너스(-) 기호가 깨지는 것을 방지하자.

# matplotlib.pyplot
matplotlib을 MATLAB처럼 쓸 수 있도록 해주는 함수들의 모음집

한글은 폰트 설정을 해야 사용가능하다.
- `matplotlib.rcParams['font.family']`=`원하는 한글 폰트`
- 사용가능한 폰트는 `matplotlib.font_manager.fontManager.ttflist`로 확인 가능
- 한글 폰트를 사용하면 표에 표시되는 마이너스(-) 기호가 깨진다. `matplotlib.rcParams['axes.unicode_minus']=False` 를 적어 한글 폰트를 사용하면서 마이너스(-) 기호가 깨지는 것을 방지하자.

## 그래프 그리기 (기본)
matplotlib.pyplot를 활용해 차트를 만드는 방식은 차트(Figure)에 원하는 그래프(Line2D)를 plot()함수를 이용해 넣는 방식이다.
### plot()
그래프를 차트에 그려줌. 그래프는 Line2D라는 클래스이다. (matplotlib.lines.Line2D) 
- `plot(x, y)`: x, y축 데이터를 받고 그래프 그려줌
	- x, y 는 리스트 또는 시리즈(판다스) 이며 길이는 같아야한다
- `plot(y)`: 데이터 모음 1가지만 입력할 수도 있는데, 이런 경우 데이터는 y축, 인덱스를 x축 값으로 인식

범례도 정의할 수 있다
- `plot(x, y, label="예시 데이테")`: 그려지는 데이터에 대한 범례를 차트에 추가 됨.
- 단 이 범례를 볼려면 `legend()`함수로 차트에 추가해야함.
```python
import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,8]
z = [3,6,9]

plt.plot(x,y , label="xy")
plt.plot(y, label="y")

plt.legend() # 모든 그래프의 범례 추가
``````

- `plot()`를 쓸 때, Line2D 속성(색깔, 투명도, 선 형태 등등)들도 임의로 정할 수 있다.
```python
# 투명도가 0.5이고 동그라미 표시의 마커를 가진 그래프 추가
plt.plot(x,y , alpha=0.5, marker="o") 
```
속성은 (https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_marker) 에서 확인이 가능하다.
- 속성을 줄여서 쓸 수 있는 것들도 있다.

간단한 그래프는 format string으로 속성들을 
### show()
지금까지 저장 된 그래프들을 한 차트에 보여줌
```python
import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,8]
z = [3,6,9]

plt.plot(x,y)
plt.plot(x,z)

plt.show()
```
이 경우, 1차트에 2개의 곡선이 그려진 모습을 볼 수 있다.

## 축/제목 설정
### title()

차트의 이름을 설정할 수 있다.
- `title("선 그래프")`: 차트의 이름을 "선 그래프로 설정"
- `title("선 그래프", fontdict={'family':"Liberation Mono", 'size': 20})`:
	- `fontdict={'family':"Ariel", 'size': 20}`를 전달해 개별 폰트 설정 가능
### xlabel() / ylabel()
- `xlabel("이름",loc="center")`: x축을 원하는 이름으로 설정
	- `matplotlib.text`에 정의 된 속성들을 전해 글씨 꼴 변경 가능
		- `xlabel("이름", color="red")` 차트에 빨간 글씨로 나타남
	- `loc`을 설정해 이름의 위치 조정 가능 ('left', 'center', 'right'). 기본값은 'center'
- `ylabel`: `xlabel`과 똑같음
	- 단, `loc` 설정 값은 'bottom', 'center', 'top'

### xticks / yticks
plot()에 전달된 데이터와 별개로 x,y축에 나타나는 값들을 따로 설정 가능
- `xticks([1,2,3,4])`: x축에 1 2 3 4 가 표시 됨.
	- 어디까지 표시만 바뀌는 것이지 x축으로 나타나는 데이터 값이 바뀌는 것이 아니다!
- `yticks`: `xticks`와 똑같음 대신 y축에 적용 됨

## 범례
- `plt.legend(loc="best")`: 지정 된 위치에 범례추가. 기본값은 'best'
	- `loc`에 matplotlib에서 미리 정의해 문자열들로 나타낼 수 있는 위치들이 있다. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html 에서 확인 가능
	- 'bests'는 위에 말한 위치들 중 그래프를 최대한 가리지 않는 위치를 matplotlib이 알아서 적절히 선정해준 위치이다.
	- `loc=(0.1,0.2)` 처럼 튜플을 전달해 자신이 차트 내 범례의 위치를 직접 지정할 수 있다. (x축 위치, y축 위치)이며, 각 위치는 0~1 사이 실수로 표현한다.

## 차트(Figure)
`matplotlib.pyplot.figure(figsize=(6.4, 4.8))` 함수를 통해 자신이 원하는 속성들을 가진 (사이즈, 해상도 등등) 차트를 만들 수 있다.
- figsize: 차트의 크기 정의. (가로, 세로) 길이. 기본값으로 (6.4, 4.8)로 설정 됨
```python
import matplotlib.pyplot as plt

x = [1,2,3]
y = [2,4,8]

# 크기가 (6,2)이고 배경 색이 g(초록색)인 차트 만들기
plt.figure(figsize=(6,2), facecolor ='g')
plt.plot(x,y)
plt.show()
```

- Figure 속성들은 (https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure)에서 확인이 가능하다.