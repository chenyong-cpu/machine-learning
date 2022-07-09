# 研究生周报（第九周）

## 学习目标

1. 自编码器
2. 循环神经网络
3. 实践方法论
4. 应用例子
5. 残差网络

## 学习时间

> 7.03 ~ 7.09

## 学习产出

1. [Python代码](./code/)
2. github记录

### 自编码器

1. 均方误差（MSE）
   1. SSE（和方差、误差平方和），计算公式为：
          $SSE=\sum_{i=1}^mw_i(y_i-\hat{y_i})^2$
   2. MSE（均方差、方差），计算公式为：
          $MSE=\frac{SSE}{n}=\frac{1}{n}\sum_{i=1}^mw_i(y_i-\hat{y_i})^2$
   3. RMSE（均方根、标准差）
          $RMSE=\sqrt{MSE}=\sqrt{\frac{SSE}{n}}=\sqrt{\frac{1}{n}\sum_{i=1}^mw_i(y_i-\hat{y_i})^2}$
2. MAE（Masked Autoencoders Are Scalable Vision Learners）
   1. MAE的做法是：以一定比例随机mask掉图片中的一些图像块，然后重建这些部分的像素值，主要特点有两个：
      1. 非对称的编、解码设计
      2. 使用较高的掩码率
   2. 为什么mask在NLP很流行，而在CV却比较冷门
      1. 架构差异：CV和NLP的网络架构不一致，前者在过去一直被CNN通知，他基于方正的局部窗口来操作；不过ViT（Vision Transformer）已经在CV界大肆虐杀了
      2. 信息密度不同：语言是高度语义和信息密集的，而图像在空间上是高度冗余的
      3. 解码的目标不一致
         1. NLP解码输出的是被mask掉的词语，本身包含了丰富的语义信息，而CV要重建的是被mask掉的图像块，是第语义的
      ![avator](./resource/v2-429666bc256a21c8077fe02a5ab8e85d_720w.jpg)
   3. 策略
      1. 沿袭ViT的做法，将图像分成一块块不重叠的patch，然后使用服从均匀分布的采样策略对这些patches随机采样一部分，同时mask掉余下的另一部分。被mask掉的patches占所有patches的大部分（实验效果发现最好的比例是75%），他们不会输入到Encoder
         1. patch是服从均匀分布来采样的，这样能够避免潜在的“中心归纳偏好”
         2. 采样高掩码比例能够防止模型轻易地根据邻近的课件patches推断
         3. 这种策略还造就了稀疏的编码器输入，能够以更低的代价训练较大规模的Encoder
   4. Pipeline
      1. 将图像划分成 patches：(B,C,H,W)->(B,N,PxPxC)；
      2. 对各个 patch 进行 embedding(实质是通过全连接层)，生成 tokens，并加入位置信息(position embeddings)：(B,N,PxPxC)->(B,N,dim)；
      3. 根据预设的掩码比例(paper 中提倡的是 75%)，使用服从均匀分布的随机采样策略采样一部分 tokens 送给 Encoder，另一部分“扔掉”(mask 掉)；
      4. 将 Encoder 编码后的 tokens 与 加入位置信息后的 masked tokens 按照原先在 patch 形态时对应的次序拼在一起，然后喂给 Decoder 玩(如果 Encoder 编码后的 token 的维度与 Decoder 要求的输入维度不一致，则需要先经过 linear projection 将维度映射到符合 Decoder 的要求)；
      5. Decoder 解码后取出 masked tokens 对应的部分送入到全连接层，对 masked patches 的像素值进行预测，最后将预测结果与 masked patches 进行比较，计算 MSE loss
3. 自编码器
   1. 编码器：将输入压缩为潜在空间表示，可以用编码函数h=f(x)表示
   2. 解码器：这部分旨在重构来自隐藏空间表示的输入，可以用解码器r=g(h)表示
   3. 因此自编码器的整体可以用函数g(f(x))=r来表示，其中我们想要得到的r与原始输入相近
4. 自编码器的用途：数据可视化的数据降噪和降维
5. 自编码器的类型
   1. 普通的自编码器：三层网络（输入、隐藏、输出），其中输入和输出是一样的
   2. 多层自编码器
   3. 卷积自编码器：使用卷积代替完全连接层
   4. 正则化自编码器
      1. 系数自编码器：用于学习诸如分类等任务的特征
      2. 降噪自编码器：改变损失函数的重构误差项

### 序列建模：循环和递归网络

**循环神经网络**或RNN是一类用于处理序列数据的神经网络。就像卷积神经网络专门用于处理网格化数据**X**的神经网络，循环神经网络是专门用于处理序列$x^{(1)},\cdots,x^{(t)}$的神经网络。

1. 展开计算图
   1. 动态系统的经典形式：$s^{(t)}=f(s^{(t-1)};\theta)$
   2. 展开的示例为：$s^{(3)}=f(s^{(2)};\theta)=f(f(s^{(1)};\theta);\theta)$
   3. 循环图简洁，展开图能够明确描述其中的计算流程。
2. 循环神经网络
![avator](./resource/2022-07-05_21-29.png)
   1. 设计模式
      1. 每个时间步都有输出，并且隐藏单元之间有循环连接的循环网络
      2. 每个时间步都产生一个输出，只有当前时刻的输出到下个时刻的隐藏单元之间有循环连接的循环网络
      3. 隐藏单元之间存在循环连接，但读取整个序列后产生单个输出的循环网络
   2. 导师驱动过程和输出循环网络
      1. 尽在一个时间步的输出和下一个时间步的隐藏单元之间存在循环连接的网络不能模拟通用图灵机，因为这个网络缺少隐藏到隐藏的循环。
      2. 由输出反馈到模型而产生循环连接的模型可用导师驱动过程进行训练，导师驱动模型的最初动机是为了在缺乏隐藏到隐藏连接的模型中避免通过时间反向传播
   3. RNN前向传播
      $a^{<t>}=b+Wh^{<t-1>}+Ux^{<t>}$
      $h^{<t>}=\tanh{(a^{<t>})}$
      $o^{<t>}=c+Vh^{<t>}$
      $\hat{y^{<t>}}=softmax(o^{<t>})$
   4. RNN反向传播（穿越时间的反向传播BPTT）
      $\frac{\partial{L}}{\partial{o^{<t>}}}=\sum_{t=1}^{\tau}\frac{\partial{L^{<t>}}}{\partial{o^{<t>}}}=\sum_{t=1}^{\tau}\hat{y^{<t>}}-t^{<t>}$
      $\frac{\partial{L}}{\partial{c}}=\sum_{t=1}^{\tau}\frac{\partial{L^{<t>}}}{\partial{o^{<t>}}}\times\frac{\partial{o^{<t>}}}{\partial{c}}=\sum_{t=1}^{\tau}\hat{y^{<t>}}-t^{<t>}$
      $\frac{\partial{L}}{\partial{V}}=\sum_{t=1}^{\tau}\frac{\partial{L^{<t>}}}{\partial{o^{<t>}}}\times\frac{\partial{o^{<t>}}}{\partial{V}}=\sum_{t=1}^{\tau}(\hat{y^{<t>}}-t^{<t>})(h^{<t>})^T$
      $\frac{\partial{L}}{\partial{h^{t}}}=\frac{\partial{L^{<t>}}}{\partial{o^{<t>}}}\times \frac{\partial{o^{<t>}}}{\partial{h^{<t>}}}+\frac{\partial{L^{<t+1>}}}{\partial{h^{<t+1>}}}\times \frac{\partial{h^{<t+1>}}}{\partial{h^{<t>}}}=V^T(\hat{y^{<t>}}-y^{<t>})+W^T\frac{\partial{L}}{\partial{h^{<t+1>}}}diag(1-(h^{<t+1>})^2)$
      $\frac{\partial{L}}{\partial{h^{<\tau>}}}=V^T(\hat{y}^{<\tau>}-y^{<\tau>})$
      $\frac{\partial{L}}{\partial{b}}=\sum_{t=1}^{\tau}\frac{\partial{L^{<t>}}}{\partial{h^{<t>}}}\times \frac{\partial{h^{<t>}}}{\partial{b}}=\sum_{t=1}^{\tau}diag(1-(h^{<t>})^2)\times \frac{\partial{L}}{\partial{h^{<t>}}}$
      $\frac{\partial{L}}{\partial{W}}=\sum_{t=1}^{\tau}\frac{\partial{L^{<t>}}}{\partial{h^{<t>}}}\times \frac{\partial{h^{<t>}}}{\partial{W}}=\sum_{t=1}^{\tau}diag(1-(h^{<t>})^2)\times \frac{\partial{L}}{\partial{h^{<t>}}}\times (h^{<t-1>})^T$
      $\frac{\partial{L}}{\partial{U}}=\sum_{t=1}^{\tau}\frac{\partial{L^{<t>}}}{\partial{h^{<t>}}}\times \frac{\partial{h^{<t>}}}{\partial{U}}=\sum_{t=1}^{\tau}diag(1-(h^{<t>})^2)\times \frac{\partial{L}}{\partial{h^{<t>}}}\times (h^{<t>})^T$
   5. 作为有向图模型的循环网络
      1. 原则上循环网络几乎可以使用认可损失
      2. 最大化对数似然：$\log{p(y^{(t)}|x^{(1)},\cdots,x^{(t)})}$
   6. 基于上下文的RNN序列建模
3. 双向RNN
   1. 对于要输出的$y^{(t)}$可能依赖与整个输入序列，例如语音识别中，由于协同发音，当前声音的正确介绍可能取决于为了的几个音素
   ![avator](./resource/Screenshot_20220705_231245.png)
4. 深度循环网络
   1. 实验证据与我们需要足够的深度以执行所需映射的想法一致
5. 递归神经网络
   1. 递归神经网络代表循环网络的了一个扩展，它被构造为深的树状结构而不是RNN的链状结构。对于具有相同长度$\tau$的序列，深度可以急剧地从$\tau$减小为$O(\log{\tau})$，这可能有助于解决长期依赖。
6. 渗透单元和其它多时间尺度的策略
   1. 时间维度的跳跃连接：增加遥远过去的变量到目前变量的直接连接
   2. 渗透单元和一系列不同时间尺度
7. 长短期记忆和其它门控RNN
   1. 长短期记忆的网络（LSTM）
   2. 门控循环单元的网络
8. 优化长期依赖
   1. 截断梯度：有助于处理爆炸的梯度
   2. 引导信息流的正则化
9. LSTM
   1. DNN和CNN的前一个输入和后一个输入是没有关系的，但是处理序列信息时，某些前面的输入和后面的输入是有关系的，要处理这些序列就需要使用循环神经网络。
   2. 原始RNN的隐藏层只有一个状态，即h,它对于短期的输入非常敏感，那么我们在增加一个门（gate）机制用于控制特征的流通的损失，即c,让它来保持长期的状态，这就是长短时记忆网络（Long short Term Memory,LSTM）
   ![avator](./resource/Screenshot_20220709_145834.png)
      1. LSTM的输入有三个：当前时刻网络的输出值$x_t$、上一时刻LSTM的输出值$h_{t-1}$、以及上一时刻的记忆单元向量$c_{t-1}$
      2. LSTM的输出有两个：当前时刻LSTM的输出值$h_t$、当前时刻的隐藏状态向量$h_t$、和当前时刻的记忆单元状态向量$c_t$

### 实践方法论

1. 性能度量
   1. 使用什么误差度量是必要的第一步
      1. 精度（precision）是模型报告的检测是正确的比率
      2. 召回率（recall）是真实事件被检测到的比率
      3. PR曲线，y轴表示精度，x轴表示召回率，F分数：$F=\frac{2pr}{p+r}$
2. 默认的基准模型
   1. 在确定度量和目标后，任何实际应用下一步是建立一个端到端的系统
3. 决定是否收集更多的数据
4. 选择超参数
   1. 手动调整超参数：最小化受限与运行时间和内存预算的泛化误差
   2. 自动超参数优化算法
   3. 网格搜索：当有三个或更少的超参数时
   4. 随机搜索
5. 调试策略
   1. 可视化计算中模型的行为
   2. 可视化最严重的错误
   3. 根据训练和测试误差检测软件
   4. 拟合极小的数据集
   5. 比较反向传播倒数和数值导数
   6. 监控激活函数值和梯度的直方图

### 应用

1. 大规模的深度学习
   1. 快速的CPU实现：使用许多台机器的CPU连接在一起
   2. GPU实现
   3. 大规模的分布式实现：单个计算资源是有限的，把训练的人物分摊到多个机器上
   4. 模型压缩：一个时间和内存开销较小的推断算法比一个时间和内存开销较小的训练算法更为重要
2. 计算机视觉
   1. 预处理：图像应该被标准化，从而使得它们的像素都在相同并且合理的范围内
   2. 对比度归一化
      1. 全局对比度归一化：通过从每一个图像中减去其平均值，然后缩放其使得其像素上的标准差等于某个常数s来防止图像具有变化的对比度。
         $X_{i,j,k}^{'}=s\frac{X_{i,j,k}-\bar{X}}{\max{\{\epsilon, \sqrt{\lambda+\frac{1}{3rc}\sum_{i=1}^r\sum_{j=1}^c\sum_{k=1}^3(X_{i,j,k}-\bar{X})^2}\}}}$
      2. 局部归一化：确保对比度在每个小窗口上被归一化
   3. 数据集增强
3. 语音识别
   1. 自动语音识别任务指的是构造一个函数$F_{ASR}^*$，使得它能够在给定序列X的情况下计算最有可能的语言序列y：$F_{ASR}^*(X)=\arg_y{\max{P^*(y|X=X)}}$
4. 自然语言处理
   1. n-gram（可用于搜索引擎或者输入法的猜想或者提示）
      1. 语言模型定义了自然语言中标记序列的概率分布，标记可以是词、字符、甚至是字节
      2. n-gram模型基于这一假设，第N个词的出现只与前面N-1个词相关，而与其它任何词都不相关，整句的概率就是各个词出现概率的成绩
      3. $P(x_1,\cdots,x_t)=P(x_1,\cdots,x_{n-1}\prod_{t=n})^{\tau}P(x_t|x_{t-n+1},\cdots,x_{t-1})$
   2. 神经语言模型
      1. 神经语言模型是一类用来克服维数灾难的语言模型，它使用词的分布式表示对自然语言序列建模。模型为每个词学习的分布式表示，允许模型处理具有类似共同特征的词来实现这种共享，比如dog和cat映射到许多具有许多属性的表示
      2. 有时候将这些词表示为词嵌入，在原始空间中每个词由一个one-hot向量表示，每对词彼此之间的欧式距离都是$\sqrt{2}$

### 矩阵微积分

1. 向量对标量求导：向量$y=[y_1 y_2 \cdots y_m]^T$关于标量$x$的导数可以写成：
   $\frac{\partial{y}}{\partial{x}}=
   \left[
      \begin{matrix}
      \frac{\partial{y_1}}{\partial{x}} \\
      \frac{\partial{y_2}}{\partial{x}} \\
      \vdots \\
      \frac{\partial{y_m}}{\partial{x}}
      \end{matrix}
   \right]$
2. 标量$y$对向量$x=[x_1 x_2 \cdots x_n]^T$的导数为：
   $\frac{\partial{y}}{\partial{x}}=
   \left[
      \begin{matrix}
      \frac{\partial{y}}{\partial{x_1}} & 
      \frac{\partial{y}}{\partial{x_2}} & 
      \cdots 
      \frac{\partial{y}}{\partial{x_n}} &
      \end{matrix}
   \right]$
3. 向量对向量求导：
   $\frac{\partial{y}}{\partial{x}}=
   \left[
      \begin{matrix}
      \frac{\partial{y_1}}{\partial{x_1}} & \frac{\partial{y_1}}{\partial{x_2}} & \cdots & \frac{\partial{y_1}}{\partial{x_n}} \\
      \frac{\partial{y_2}}{\partial{x_1}} & \frac{\partial{y_2}}{\partial{x_2}} & \cdots & \frac{\partial{y_2}}{\partial{x_n}} \\
      \vdots & \vdots & \ddots & \vdots \\
      \frac{\partial{y_m}}{\partial{x_1}} & \frac{\partial{y_m}}{\partial{x_2}} & \cdots & \frac{\partial{y_m}}{\partial{x_n}}
      \end{matrix}
   \right]$
4. 矩阵求导：矩阵函数$Y$对标量$x$的导数被称为切矩阵：
   $\frac{\partial{Y}}{\partial{x}}=
   \left[
      \begin{matrix}
      \frac{\partial{y_{11}}}{\partial{x}} & \frac{\partial{y_{12}}}{\partial{x}} & \cdots & \frac{\partial{y_{1n}}}{\partial{x}} \\
      \frac{\partial{y_{21}}}{\partial{x}} & \frac{\partial{y_{22}}}{\partial{x}} & \cdots & \frac{\partial{y_{2n}}}{\partial{x}} \\
      \vdots & \vdots & \ddots & \vdots \\
      \frac{\partial{y_{m1}}}{\partial{x}} & \frac{\partial{y_{m2}}}{\partial{x}} & \cdots & \frac{\partial{y_{mn}}}{\partial{x}}
      \end{matrix}
   \right]$
5. 矩阵对标量求导：
   $\frac{\partial{y}}{\partial{X}}=
   \left[
      \begin{matrix}
      \frac{\partial{y}}{\partial{x_{11}}} & \frac{\partial{y}}{\partial{x_{21}}} & \cdots & \frac{\partial{y}}{\partial{x_{p1}}} \\
      \frac{\partial{y}}{\partial{x+{12}}} & \frac{\partial{y}}{\partial{x_{22}}} & \cdots & \frac{\partial{y}}{\partial{x_{p2}}} \\
      \vdots & \vdots & \ddots & \vdots \\
      \frac{\partial{y}}{\partial{x_{1q}}} & \frac{\partial{y}}{\partial{x_{21}}} & \cdots & \frac{\partial{y}}{\partial{x_{pq}}}
      \end{matrix}
   \right]$

### 残差神经网络（ResNet）

1. 残差神经网络的主要贡献是发现了“退化现象”，并针对退化现象发明了“快捷连接”，极大的消除了深度过大的神经网络训练困难问题。
2. 对于一个堆积层结构当输入为x时学习到的特征记为H(x)，现在我们希望其可以学习到残差F(x)=H(x)-x；当残差为0时，此时堆积层仅仅做了恒等映射（至少网络性能不会下降），实际上残差不会为0,这也使得堆积层在输入特征基础上学习到了新的特征。
![avator](./resource/Screenshot_20220709_183730.png)
3. 残差网络是由一系列残差块组成的，一个残差块可以表示为：$x_{l+1}=x_l+F(x_l,W_l)$
   在卷积网络中，$x_l$和$x_{l+1}$的Feature Map的数量不一样时需要使用$1\times 1$卷积进行生维或者降维，这时残差块表示为：$x_{l+1}=h(x_l)+F(x_l,W_l)$

## 总结

1. 本周看了深度学习一书的第十章（序列建模：循环和递归网络）、十一章（实践方法论）、十二章（应用），还看了自编码器和了解了残差学习
2. 下周应该看深度学习第三部分深度学习研究的前几章并寻找代码练习
