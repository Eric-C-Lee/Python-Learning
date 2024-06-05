import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
plt.rcParams['font.sans-serif'] = ['SimSun']  # 修复字体问题

data = pd.read_excel('Data(Washed).xls')
data['季度'] = pd.to_datetime(data['季度']).dt.to_period('Q')
data['季度'] = data['季度'].apply(lambda x: x.start_time)
X = data[['季度']]
y = data['居民人均可支配收入中位数']
model = RandomForestRegressor()
model.fit(X, y)

future_quarters = pd.date_range(start='2023-12', end='2025-03', freq='Q')
future_quarters = future_quarters.to_series().dt.to_period('Q')
future_quarters = future_quarters.apply(lambda x: x.start_time)
future_quarters = future_quarters.to_numpy().reshape(-1, 1)
future_predictions = model.predict(future_quarters)

plt.plot(data['季度'], data['居民人均可支配收入中位数'], label='历史数据')
plt.plot(future_quarters, future_predictions, label='预测数据')
plt.xlabel('季度')
plt.ylabel('数值')
plt.title('居民人均可支配收入中位数')
plt.legend()
plt.xticks(rotation=45)
plt.show()
