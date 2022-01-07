<!-- TOC -->

- [问题拆解和数据](#问题拆解和数据)
    - [构建文本分类标签体系有哪些坑？](#构建文本分类标签体系有哪些坑？)
    - [初期监督数据不够怎么办？](#初期监督数据不够怎么办？)
    - [如何高效的积累标注数据](#如何高效的积累标注数据)
    - [如何发现新的类别？扩充类别空间？](#如何发现新的类别？扩充类别空间？)
- [算法抽象和选型](#算法抽象和选型)
    - [文本分类任务有哪些难点？](#文本分类任务有哪些难点？)
    - [如何定义一个文本分类问题的难度？](#如何定义一个文本分类问题的难度？)
    - [文本分类算法选型有何推荐？](#文本分类算法选型有何推荐？)
    - [如何确定验证集和评价方法](#如何确定验证集和评价方法)
- [细节策略和实现](#问题拆解和数据)
    - [如何处理溢出词表词？](#如何处理溢出词表词？)
    - [文本分类技术演进的明线和暗线？](#文本分类技术演进的明线和暗线？)
    - [策略和算法如何结合？](#策略和算法如何结合？)
    - [有哪些可以刷分的技巧？](#有哪些可以刷分的技巧？)
    - [模型inference资源限制条件下，如何挑战算法选型的天花板](#模型inference资源限制条件下，如何挑战算法选型的天花板)

<!-- /TOC -->

# 问题拆解和数据
## 构建文本分类标签体系有哪些坑？
* 稀疏程度合理：长尾，合并尾部类别；softmax；按业务频率分类
* 类间可分，类内聚集

## 初期监督数据不够怎么办？
* 规则，词典等进行标记
* fewshot learning: 匹配/相似度学习问题
* 迁移学习

## 如何高效的积累标注数据
* 类别空间会扩充以及长尾标注样本数量不足是两个最常见的问题
* 不确定的样本：置信度不高的样本，人工识别并指导学习
* 不一样的样本：adversarial validation
* uber paper to handle concept drift detection: https://arxiv.org/pdf/2004.03045v2.pdf

## 如何发现新的类别？扩充类别空间？
* 推荐ACL2019的那个论文 Deep Unknown Intent Detection with Margin Loss
* 本质上都是找出，与已知类别不相似（分布差异较大）的样本，其实用前面的adversrial validation也可以解决，实测margin softmax效果更好一点。

# 算法抽象和选型
## 文本分类任务有哪些难点？
* input: short -> long or very long 输入层面：短文本->长文本和超长文本
* tagging: complex and emotion 标签层面：复杂语义识别，如阴阳怪气
* development: the change of meaning 时间演化：川普VS 川普，开车VS开车
* context: word meaning change with context 上下文：美食论坛苹果小米黑莓 VS手机论坛苹果小米黑莓

## 如何定义一个文本分类问题的难度？
* topic classification
* emotion classification: positive vs negative
* intention classification
* granular emotion classification: happy, sad, upset, disappointed etc.
* hidden meaning classification

## 文本分类任务有哪些难点？
* Fasttext（垃圾邮件/主题分类） 特别简单的任务，要求速度
* TextCNN（主题分类/领域识别） 比较简单的任务，类别可能比较多，要求速度
* LSTM（情感分类/意图识别） 稍微复杂的任务
* Bert（细粒度情感/阴阳怪气/小样本识别）难任务

## 如何确定验证集和评价方法？
* 确定各类别错分的代价: customize loss function
* imbalance: add more tail samples to validation
* add many edge cases; adverserial validation

# 细节策略和实现
## 如何处理溢出词表词？
* Out of Vocabulary (OOV)
* 各种还原词根，大小写等；or subword
* bert

## 文本分类模型演进的明线和暗线？
* 明线：统计-机器学习-深度学习-更深的深度学习
* 暗线1：简单表达-语义表达-上下文语义表达
* 暗线2：特征输入粒度 从词到subword
* 暗线3：预训练权重从输入层扩展到网络结构内部


## 策略和算法怎么结合？
* sequential: rules(identify good vs bad) -> classification (identify high-freq tail categories) -> matching (very tail) FAST
* parallel: rules, classification, matching at the same time and then choose the most confident one, similar to ad bidding RELIABLE


## 有哪些可以刷分的奇技淫巧？
* RNN based model 包括lstm gru等，使用双向结构
* embedding 后使用dropout
* 显然问题fasttext，简单问题CNN，复杂问题RNN，终极问题bert
* ensemble
* 尽可能找到还原语义的pretrained embedding，实际情况是oov千奇百怪，拼写检查，基本上是100倍的努力，一点点收益，或者拆词，拆字能一定程度上缓解

## 模型inference资源限制条件下，如何挑战算法选型的天花板
* Bert vs TextCNN: accuracy vs speed
* Model Dislation 模型蒸馏 









