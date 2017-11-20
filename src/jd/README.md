# 文件信息
t_login.csv 登录信息表（训练）
t_trade.csv 交易风险标志表（训练）
t_login_test.csv 登录信息表（评测）
t_trade_test.csv 待预测交易表（评测）

# 数据字典

t_login t_login_test

---
log_id 主键
timelong 登录所用时间
device 设备标志
log_from 登录来源
ip 登录IP
city 登录ip归属地
result 登录结果
timestamp 登录时间戳
type 登录类型
id 用户账号
is_scan 是否扫码登录
is_sec 是否使用安全控件
time 登录时间

t_trade t_trade_test

---
rowkey 主键
time 交易时间
id 用户账号
is_risk 风险标志（t_trade表）





rowkey 主键
time 交易时间
is_risk 风险标志
log_id 主键
timelong 登录所用时间
device 设备标志
log_from 登录来源
ip 登录IP
city 登录ip归属地
result 登录结果
timestamp 登录时间戳
type 登录类型
id 用户账号
is_scan 是否扫码登录
is_sec 是否使用安全控件
time 登录时间