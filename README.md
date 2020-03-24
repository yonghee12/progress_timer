# Progress Timer
* A Python module which prints elapsed time and estimated time left with accordance to percentage
* 파이썬 반복문에서 인덱스를 기반으로 백분율에 맞추어 진행률을 표시해주는 모듈

# Install
`pip install progress_timer`

# Usage
```
from progress_timer import Timer

length = len(a_iterator)
timer = Timer(length)
for idx, item in enumerate(a_itertator):
    timer.time_check(idx)
```

# Result
![result](https://user-images.githubusercontent.com/24601847/77436904-607ff580-6e27-11ea-8ec3-af31dd60392d.png)
