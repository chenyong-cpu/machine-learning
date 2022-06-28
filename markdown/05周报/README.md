# 研究生周报（第八周）

## 学习产出

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
