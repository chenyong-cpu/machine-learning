reader = ds.load_block(dsId)
# 5、指定每次读取数据行数
onceReadLines = 1000000
# 6.循环预测
rt = 0
train = 0
model = 0
df2 = pd.DataFrame()
full = pd.DataFrame()
x_train, x_test, y_train, y_test = 0,0,0,0
while True:
    print("this is round：", rt)
    try:
        # 1）读数据
        full = pd.DataFrame()
        print(onceReadLines)
        fulll = reader.get_chunk(onceReadLines)
        full = fulll.copy(deep=True)
        #建立ageDf，存放年龄分段
        ageDf= pd.DataFrame()
        ageDf[ 'age' ] = full[ 'age' ]
        '''
        年龄分段：
        '[0,18]','[19,25]','[26,35]','[36,45]','[46,60]' ,'[60,)'
        '''
        #if 条件为真的时候返回if前面内容，否则返回0
        ageDf[ 'age1' ]  = ageDf[ 'age' ].map( lambda s : 1 if 0 <= s <= 18 else 0 )
        ageDf[ 'age2' ]  = ageDf[ 'age' ].map( lambda s : 1 if 19 <= s <= 25 else 0 )
        ageDf[ 'age3' ]  = ageDf[ 'age' ].map( lambda s : 1 if 26 <= s <= 35 else 0 )
        ageDf[ 'age4' ]  = ageDf[ 'age' ].map( lambda s : 1 if 36 <= s <= 45 else 0 )
        ageDf[ 'age5' ]  = ageDf[ 'age' ].map( lambda s : 1 if 46 <= s <= 60 else 0 )
        ageDf[ 'age6' ]  = ageDf[ 'age' ].map( lambda s : 1 if 61 <= s  else 0 )
        ageDf=ageDf.drop(['age'],axis=1)
        need_onehot_columns=['sex_new','famstru','edu_level','life_stage','occu','tele_fac']
        # 便捷方法，用df全部替换
        full_X = pd.get_dummies(
        full,
        # 要转码的列
        columns=need_onehot_columns,
        # 生成的列名的前缀
        prefix=need_onehot_columns,
        # 把空值也做编码
        dummy_na=True,
        # 把1 of k移除（dummy variable trap）
        drop_first=True
        )
        
        full_X = pd.concat([full_X,ageDf],axis=1)
        full_X.shape
        train= full_X.drop(['bill_no'],axis=1)
        train.shape
        from imblearn.under_sampling import RandomUnderSampler
        from sklearn.model_selection import train_test_split
        X = np.array(train.drop(['is_ym'],axis=1))
        y = np.array(train['is_ym'])
        x_train,x_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,shuffle =True)
        from xgboost import XGBClassifier
        model =exported_pipeline =XGBClassifier(learning_rate=0.3, max_depth=5, min_child_weight=1, n_estimators=100, n_jobs=1, subsample=0.9500000000000001, verbosity=0)
        model.fit(x_train,y_train)
        ypred1=model.predict(x_test)
        model.score(x_test, y_test)
        from sklearn.metrics import confusion_matrix, classification_report
         #分类报告
        cr = classification_report(y_test,ypred1)
        print(cr)
        ypred1 = ypred1.astype(int)
        sourceRow=len(full_X)-len(ypred1)
        bill_no = full_X.loc[sourceRow:,'bill_no']
        predDf = pd.DataFrame(
			{ 'bill_no': bill_no,
			 'pred': ypred1,
			})
		
        if (rt == 0):
            predDf.to_csv("yanming", index=False)
        elif(rt != 0):
            predDf.to_csv("yanming", index=False,mode='a')
            #result.to_csv('output.csv', index=False, header=False, mode='a')
        rt = rt + 1
    except StopIteration:
        print("Iteration is stopped. OVER")
        # 关闭
        reader.close()
        # 退出while
        break;
print("循环结束，请查看预测结果")