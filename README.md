<div align="center">
  <h1>:dog:  aiovk_new</h1>
  <h3>A simple async library for vk with pydantic & httpx</h3>
</div><br>

## 🛠 Usage
```python
from aiovk_new import AioVK

vk_api = AioVK(access_token=...)

post, *_ = await vk_api.wall.get("vk")
print(post.text)
```

## 🎉 Features
- Full async
- Uses [httpx](https://github.com/encode/httpx)
- Uses models by [pydantic](https://github.com/samuelcolvin/pydantic)

## 🚀 Install
To install, run this code:
```
pip install aiovk_new
```
