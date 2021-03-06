# 研究生周报（第八周）

## 学习目标

1. 深度前馈网络
2. 深度学习中的正则化
3. 深度模型中的优化
4. 卷积网络

## 学习时间

> 6.26～7.02

## 学习产出

1. [Python代码](./code/)
2. github记录

### 学习率衰减

1. 梯度下降法更新参数公式：$\theta_{t+1}=\theta_t-\eta\cdot\nabla J(\theta)$，其中$\eta$是学习率，$\theta_t$是第t轮的参数，$J(\theta_t)$是损失函数，$\nabla J(\theta_t)$是梯度；$\eta$是常数，是一个需要提前设定好的超参数
2. Adam更新参数，Adam是一种优化器
   1. Adam更新公式：$\\ m_t=\beta_1m_{t-1}+(1-\beta_1)g_t \\ v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2 \\ \hat{m_t}=\frac{m_t}{1-\beta_1^t} \\ \hat{v_t}=\frac{v_t}{1-\beta_2^t} \\ \theta_{t+1}=\theta_t-\frac{\eta}{\sqrt{\hat{v_t}+\epsilon}}\hat{m_t}$
   2. 前两行是对梯度和梯度的平方求滑动平均
   3. 中间两行是对初期滑动平均偏差进行修正；当t越来越大时，$1-\beta_1^t$和$1-\beta_t^2$越来越接近与1
   4. 最后一行为参数更新公式
3. 在训练神经网络时，使用学习率控制参数的更新速度．学习率较小时，会大大降低参数的更新速度；学习率较大时，会使搜索过程中发生震荡，导致参数在极优值附近徘徊。
   1. 指数衰减

      ```python
      # 定于一个优化器
      optimizer_ExpLR = torch.optim.SGD(net.parameters(), lr=0.1)
      # 绑定一个衰减学习率控制器
      ExpLR = torch.optim.lr_scheduler.ExponentialLR(optimizer_ExpLR, gamma=0.98)
      ```

   2. 固定步长衰减

      ```python
      # 学习率每隔一定步长能减少为原来的gamma分之一，使用固定步长衰减依旧先定义优化器，再给优化器绑定StepLR对象
      optimizer_StepLR = torch.optim.SGD(net.parameters(), lr=0.1)
      StepLR = torch.optim.lr_scheduler.StepLR(optimizer_StepLR, step_size=step_size, gamma=0.65)
      ```

   3. 多步长衰减

      ```python
      # 动态区间长度控制
      optimizer_MultiStepLR = torch.optim.SGD(net.parameters(), lr=0.1)
      torch.optim.lr_scheduler.MultiStepLR(optimizer_MultiStepLR,milestones=[200, 300, 320, 340, 200], gamma=0.8)
      ```

   4. 余弦退火衰减

      ```python
      # 严格来说，余弦退火策略不应该算是学习率衰减策略，因为他使得学习率按照周期变化
      optimizer_CosineLR = torch.optim.SGD(net.parameters(), lr=0.1)
      CosineLR = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer_CosineLR, T_max=150, eta_min=0)
      ```

### Softmax

1. Softmax的含义就在于不再唯一的确定某一个最大值，而是为每一个输出分类的结果都赋予一个概率值，表示属于每个类别的可能性。
2. $Softmax(z_i)=\frac{e^{z_i}}{\sum_{c=1}^Ce^{z_c}}$，其中$z_i$为第i个节点的输出值，C为输出节点的个数，即分类的类别个数。

### 深度前馈网络

1. 深度前馈网络（deep feedforward network），也叫作前馈神经网络（feedforward neutal network）或者多层感知机（multilayer perception,MLP）
2. 深度前馈网络的目标是近似某个函数$f^*$，例如，对于分类器，$y=f^*(x)$将输入x映射到一个类别y；前馈网络定义了一个映射$y=f(x;\theta)$，并且学习参数$\theta$的值，使它能够得到最佳的函数近似
3. 为了扩展线性模型来表示x的非线性函数，我们可以不把线性模型用于x本身，而是用在一个变换的$\phi(x)$上
   1. 使用一个通用的$\phi$
   2. 手动地设计$\phi$
   3. 深度学习的策略是去学习$\phi$
4. 学习XOR
   1. $\Chi=\{[0,0]^T,[0,1]^T,[1,0]^T,[1,1]^T\}$
   2. MSE损失函数$J(\theta)=\frac{1}{4}\sum_{x\subset\Chi}(f^*(x)-f(x;\theta))^2$
      1. $f^*(x)$为目标函数
      2. $f(x;w,b)=x^Tw+b$
5. 基于梯度的学习
   1. 大多数现代的神经网络使用最大似然来训练，这以为这代价函数就是负的对数似然：$J(\theta)=-E_{x,y~\hat{p_{data}}}\logp_{model}(y|x)$,它减轻了每个模型设计代价函数的负担
6. 反向传播
   1. 反向传播经常被误解为仅适用于多层神经网络，但是原则上它可以计算任何的导数。
   2. 微积分中的链式法则：$\frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx}$

### 深度学习中的正则化

1. 参数范数正则化
   1. 许多正则化方法通过对目标函数$J$添加一个参数范数惩罚$\Omega(\theta)$，限制模型的学习那里，我们将正则化后的目标函数记为$\hat{J}$：$\\\hat{J}(\theta;X,y)+\alpha\Omega(\theta)\\$其中$\alpha\in[0,\infty)$是权衡范数惩罚项和标准目标函数$J(X;\theta)相对贡献的超参数
2. 参数范数惩罚
   1. L1正则化可以产生稀疏权值矩阵，即产生一个稀疏模型，可以用于特征选择
   2. L2正则化可以防止模型过拟合；一定程度上，L1也可以防止过拟合

### 深度模型中的优化

1. 经验风险最小化
   1. 由于没有真实样本，只能通过使用训练样本获得的经验分布$\hat{p}(x,y)$代替真实分布$p(x,y)$：$E_{x,y~\hat{p}_{data}}[L(f(x;\theta),y)]=\frac{1}{m}\sum_{i=1}^mL(f(x^{(i)};\theta),y^{(i)})$
   2. 经验最小化分布容易导致过拟合，因为高容量的模型会简单的记住训练集
2. 代理损失函数和提前终止
3. 批量算法与小批量算法
   1. 机器学习中的优化算法在计算参数的每一次更新时通常仅使用整个代价函数中一部分项来估计代价函数的期望值
   2. 需要选择合适的小批量，极大的批量会计算更准确的梯度估计，但是回报却是小于线性的；极小的批量则难以充分利用多核架构
   3. 小批量需要为随机抽取的
4. 神经网络优化中的挑战
   1. 病态
      1. 病态问题一般被认为存在与神经网络训练过程中，病态体现在随机梯度下降会“卡”在某些情况，此时即使很小的更新步长也会增加代价函数
   2. 局部极小值
      1. 任何一个极小值都是全局最小点
      2. 一种能够排除极小值是主要问题的检测方法是画出梯度范数随时间的变化
      3. 通过牛顿法解决
   3. 高原、鞍点和其他平坦区域
      1. 在低维空间中，局部极小值很普遍，在更高维空间中，鞍点很普遍
      2. 通过无鞍牛顿法解决
   4. 悬崖和梯度爆炸
      1. 多层神经网络通常存在像悬崖一样的斜率较大区域，梯度更新时可能会跳过这类结构
      2. 通过梯度截断避免其后果
   5. 长期依赖
      1. 当计算图变得极深时，由于变深的结构使模型丧失了学习到先前信息的能力，让优化变得极其困难
   6. 非精确梯度
   7. 局部和全局结构间的弱对应
      1. 大多数优化研究的难点集中与训练是否找到了全局最小点、局部最小点或是鞍点，但是在实践中神经网络不会到达任何一种临界点
   8. 优化的理论限制
      1. 一些理论结果表面，我们为神经网络设计的任何优化算法都有性能限制
5. 基本算法
   1. 随机梯度下降（一般机器学习中应用最多的优化算法）
      1. SGD算法的一个关键参数是学习率，在实践中，有随着时间的推移逐渐降低学习率，因此我们将第$k$步迭代的学习率记为$\epsilon_k$
   2. 动量
      1. 动量的目的是为了解决两个问题：Hessian矩阵的变态条件和随机梯度的反差
   3. Nesterove动量
      1. 在凸批量梯度的情况下，Nesterov动量将额外误差收敛率从$O(1/k)$改进到$O(1/k)^2$
6. 参数初始化策略
7. 自适应学习率算法
   1. Delta-bar-delta算法是一个早期的在训练过程时适应模型参数各自学习率的启发式方法（全批量优化中）
   2. 增量（小批量）算法
   3. AdaGrad
   4. RMSProp
   5. Adam
8. 二阶近似方法
   1. 牛顿法
      1. 牛顿法是基于二阶泰勒级数展开在某点$\theta_0$附近来近似$J(\theta)$的优化方法，其忽略了高阶导数：$J(\theta)\approx J(\theta_0)+(\theta-\theta_0)^T\nabla\theta J(\theta_0)+\frac{1}{2}(\theta-\theta_0)^TH(\theta-\theta_0)$
      2. 其中$H$是$J$相对于$\theta$的$Hessian$矩阵在$\theta_0$处的估计，得到牛顿参数更新规则：$\theta^*=\theta_0-H^{-1}\nabla_\theta J(\theta_0)$
      3. 对于非二次的表面，只要$Hessian$矩阵保持正定，牛顿法能够迭代地应用
      4. 目标函数的表面通常为非凸（有很多特征），如鞍点，使用牛顿法存在问题
   2. 共轭梯度
      1. 通过迭代下降的共轭方向以有效避免Hessian矩阵求逆计算的方法
   3. BFGS
      1. BFGS具有牛顿法的一些有点，但没有牛顿法的计算负担
9. 优化策略和元算法
   1. 批标准化
      1. 它不是一个优化算法，而是一个自适应的重参数化的方法，试图解决训练非常深的模型的困难
      2. 设$H$是需要标准化的某层的小批量激活函数，排布为设计矩阵，每个样本的激活出现在矩阵的每一行。为了标准化$H$，我们将其替换为$\\H'=\frac{H-\mu}{\sigma}\\$其中$\mu$是包含每个单元的均值的向量，$\sigma$是包含每个单元标准差的向量
      3. 在训练阶段：$\mu=\frac{1}{m}\sum_iH_i$和$\sigma=\sqrt{delta+\frac{1}{m}\sum_i(H-\mu)_i^2}$，其中$\delta$是一个很小的真值，避免出现为0的问题
   2. 坐标下降
      1. 将一个优化问题分解成几个部分
   3. Polyak平均
   4. 监督预训练
      1. 贪心算法将问题分解成许多部分，然后独立地在每个部分求解最优值。虽然不是一个最近的完整解，但是往往是可以接受的
   5. 设计有助于优化的模型
   6. 延扩法和课程训练
      1. 延拓法(continuation method)是一族通过挑选初始点使优化更容易的方法,以确保局部优化花费大部分时间在表现良好的空间

### 卷积网络

1. 卷积运算：卷积是对两个实边函数的一种数学运算
   1. 卷积运算表示：$s(t)=(x*w)(t)$，其中w必须是一个有效的概率密度函数，另外，在参数为负值时，$w$的取值必须为0
   2. 卷积运算的第一个参数（$x$)叫做输入，第二个参数（$w$)叫做核函数，输出有时被称为特征映射
   3. 卷积是可交换的：$S(i,j)=(I*K)(i,j)=\sum_m\sum_nI(m,n)K(i-m,j-n)=\sum_m\sum_nI(i-m,j-n)K(m,n)$
   4. 互相关函数，和卷积运算几乎一样但是并没有对核进行翻转：$S(i,j)=(I*K)(i,j)=\sum_m\sum_nI(i+m,j+n)K(m,n)$
2. 动机
   1. 稀疏交互：使核的大小远小于输入的大小来达到
   2. 参数共享：在一个模型的多个函数中使用相同的参数
   3. 等边表示：函数满足输入改变，输出也同样的方式改变这一性质
3. 池化
   1. 卷积网络中一个典型层包含三级：第一个计算多个卷积产生一组线性激活响应；第二级中每一个线性激活响应将会通过一个非线性的激活函数（探测级）；第三级中使用池化函数来进一步调整这一层的输出
   2. 池化函数使用某一位置的相邻输出的总体统计特征来代替网络在该位置的输出
4. 卷积与池化作为一种无限强的先验
   1. 卷积和池化只有当先验的假设合理并且正确才有用
5. 基本卷积函数的变体
   1. 神经网络的卷积通常指多个并行卷积组成的运算：因为具有单个核的卷积只能提取一种类型的特征，尽管它作用在多个空间位置上，我们希望网络的每一层能够在多个位置提取多种类型的特征。
6. 结构化输出
   1. 卷积神经网络可以用于输出高维的结构化对象
7. 高效的卷积算法
   1. 当一个d维的核可以表示成d个向量，则该核被称为可分离的；当核可分离时，朴素的卷积是低效的。
8. 随机或无监督的特征
   1. 不通过监督训练而得到卷积核
      1. 随机初始化
      2. 手动设计
      3. 逻辑回归或者SVM
   2. 随机过滤器经常在卷积网络中表现得出乎意料得好：由卷积和随后的池化组成的词，当随机赋予随机权中时，自然地变得具有频率选择性和平移不变性
9. 卷积网络的神经科学基础
   1. 卷积网络层被设计为描述V1的三个性质
      1. V1可以进行空间映射
      2. V1包含许多简单细胞：在某种程度上可以概括为在一个小的空间位置感受野内的图像的线性函数
      3. V1还包含许多复杂细胞：这类细胞相应简单细胞检测到的那些特征
   2. 方向相关向我们表面，大多数的V1细胞具有有Gabor函数所描述的权重
      1. Gabor变换属于加窗傅立叶变换，Gabor函数可以在频域不同尺度、不同方向上提取相关的特征。（实质上是对二维图像求卷积）
      2. 二维Gabor函数可以表示为：$g_{uv}(x,y)=\frac{k^2}{\sigma^2}\exp(-\frac{k^2(x^2+y^2)}{2\sigma^2})\cdot[\exp(ik\cdot\left(\begin{matrix}x\\y\end{matrix}\right))-exp(-\frac{\sigma^2}{2})]$$\\k=\left(\begin{matrix}k_x \\ k_y\end{matrix}\right)$=$\left(\begin{matrix}k_v\cos\varphi_u \\ k_v\sin\varphi_u\end{matrix}\right)$$\\k_v=2^{-\frac{v+2}{2}\pi}$$\\\varphi_u=u\frac{\pi}{K}\\$v的取值决定了Gabor滤波的波长，u的取值表示Gabor核函数的方向，K表示总的方向数，参数$\frac{\sigma}{k}$决定了高斯窗口的大小
      3. Gabor滤波的本质是提取图像的特征向量，通常应用的领域有质问识别，虹膜识别，人脸识别等

## 总结

1. 本周看了深度学习一书的第七章（正则化）——第九章（卷积网络），学习了一些聚类算法并进行比较
2. 下周继续看深度学习一书的第十章等章节，由于本书是理论知识，因此准备自己抽时间需要自己寻找代码练手
