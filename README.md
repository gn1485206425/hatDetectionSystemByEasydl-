# hatDetectionSystemByEasydl-
* 实验系统，pyqt下调用easydl（BaiduAi）上团队账户训练好的模型
* 项目结束后在进行整理
* 目前初步完善了ui和模型调用

## 流程和功能
1. 在easydl上训练模型
2. 在pyqt框架里面定义filename得到传入图片路径
3. 从平台得到token和host，在app.makenImgName中对实验图片进行调用请求并返回json信息
4. 设计出配套的判断预警系统，阈值暂时拟定0.6

**thanks for my friend [甘宁](https://github.com/gn1485206425)（who collects the dataset and trains the models by easydl）**
