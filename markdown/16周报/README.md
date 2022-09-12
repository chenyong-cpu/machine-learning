# 研究生周报（第十九周）

## 学习目标

## 学习时间

> 9.11 ~ 9.17

## 学习产出

### LAS

1. **Phoneme**，是发音的基本单位，模型将声音转化成为Phoneme，然后通过发音的基本单位，在确定单词的拼写。
2. **Grapheme**，是最小的字符单元，意识就是说我们将声音通过模型转换为一个个字母。
3. **Word**，模型直接将声音转化成为单词，该方法看上去挺好，但是面对词汇量大的语言不适用，比如说土耳其语，可与创造出更加复杂的词汇。
4. **Morpheme**，大致意识就是词根词缀，单位介于Grapheme和Word之间。
5. **Bytes！**，二进制。

**Listen, Attend, and Spell(LAS)**，可以看出沦为分为三个部分**Listen（encoder编码器）、Attend（注意力机制）、Spell（decoder解码器）**

#### Listen

![avator](./image/1.png)

**Listen**，这一部分我们需要做的就是专注于我们所听的，去除噪声。

我们通过Encoder编码器可以选择RNN、CNN（通常是1D-CNN）、CNN+RNN、Self-Attention。

![avator](./image/2.png) | ![avator](./image/3.png) | ![avator](./image/4.png)
---|---|---

由于声音的采集通常都是很大数据量的比如采样率为16KHz需要在一秒钟采集16000个采样点，所以通常需要对神经进行降采样，减少样本参数。

![avator](./image/5.png) | ![avator](./image/6.png)
---|---

#### Attention

注意力机制，顾名思义就是要我们注意到我们该注意的，通过端到端的训练为我们总可以使得模型知道该拿哪些重要的。

![avator](./image/7.png) | ![avator](./image/8.png) | ![avator](./image/9.png)
---|---|---

#### Spell

**Spell**为解码器端，将会输出每一个词的概率，如果选择概率最大的词，那么这种方法就为贪婪搜索，通常是选择多个概率最大的词，进行下一波搜索，即为**集束搜索**。

![avator](./image/10.png) | ![avator](./image/11.png)
---|---

#### Training

在训练是不将Spell输出的结果作为下一个输入，而是直接把正确的结果作为输入。

![avator](./image/12.png) | ![avator](./image/13.png)
---|---

### Connectionist Temporal Classification(CTC)

![avator](./image/14.png) | ![avator](./image/15.png)
--|--

1. 输入T个声学信号，输出T个符号（包括$\phi$）。
2. 输出包含$\phi$的序列，合并重复的$\phi$，去除$\phi$。

#### Training

如何制造每一个输入对应的正确的输出？

1. alignment：向预训练中添加$\phi$，这会产生许多alignmet的序列 => CTC全部拿去使用

### RNN Transducer(RNN-T)

![RNN->RNN-T](./image/16.png) | ![RNN-T](./image/17.png) | ![RNN-T](./image/18.png)
---|---|---

### Neural Transducer

![Neural Transducer](./image/19.png) | ![Neural Transducer window](./image/20.png)
---|---

### Monootonic Chunkwise Attention(MoChA)

![判断移动窗口](./image/21.png) | ![avator](./image/22.png)
---|---

<!-- ### HMM

![state](./image/23.png) | ![state](./image/24.png)
---|---

1. Transition Probability：从一个state到另一个state的几率，及下一个vector是由哪一个state产生的
2. Emission Probability：给定一个state，这个state产生的声音序列样子怎么样。

**Tied-state**：有一些state，他们会共用一个model distribution，这件事叫做Tied-state。 -->

## 总结
