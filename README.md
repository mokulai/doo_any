# doo_any

原始项目地址：https://github.com/tonglei100/doo

# 新增功能

因自身使用需要增加了参数配置为**any**时，无论传递任何值都可以返回既定的RESPONSE

# example

```

--- # any mock
Name: AnyMock
Desc: any参数的demo
Path: /api/any
Method: GET
Auth: None

REQUEST:
  Body:
    id: [int, Y, 随机id, '']

RESPONSE:
  Headers:
    Content-Type: application/json
  Body:
    Body: [json, Y, 报文Body, json格式]

DATA1:
  REQUEST:
    orderNo: any
  RESPONSE:
    error_code: "0"
    error_msg: 查询成功
```

# 使用方式

同原始项目