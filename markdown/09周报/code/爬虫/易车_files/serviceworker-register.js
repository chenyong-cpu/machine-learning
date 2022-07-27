
// 注册sw
var YC_SW = {
    /**
     * @description: 初始化
     */
    init(config) {
        if ('serviceWorker' in window.navigator) {
            // 参数合并
            this.config = Object.assign({
                // 作用域
                scope: '/',
                // 项目名称,素材接口在使用
                projectName: '',
                // 获取开关函数
                checkSwitch(isOpen){
                    // 内部项目
                    if(this.projectName){
                        fetch(`//static1.bitautoimg.com/yc-sw/src/switch.txt?_=${Math.random()}`)
                            .then((response) => { return response.text(); })
                            .then(res => {
                                isOpen(res && res.indexOf(this.projectName) != -1)
                            })
                            .catch(() => {
                                isOpen()
                            })
                    } else {
                        isOpen(true)
                    }
                    
                }
            }, config);
            // 检查是否可以注册
            this.config.checkSwitch((res) => {
                this.checkCacheSize();
                this.runRegister(res)
            });
        }
    },

    /**
     * @description: 注册SW
     */
    runRegister(isRegister) {
        console.log('是否启用了service worker?', isRegister)
        if ('serviceWorker' in window.navigator) {
            // 注册 
            if(isRegister) {
                navigator.serviceWorker.getRegistration().then(res => {
                    if(!res || location.origin + this.config.scope !=  res.scope) {
                        navigator.serviceWorker.register(`/serviceworker.js?v=${Math.random()}`, { scope: this.config.scope })
                    }
                })
            }
            // 开关关闭了
            else {
                // 注销时，清除缓存
                this.clearCache();
                // 注销全部sw实例 
                navigator.serviceWorker.getRegistrations().then((registrations) => {
                    if (registrations) {
                        for (let registration of registrations) {
                            registration && registration.unregister();
                        }
                    }
                })
            }
        }
    },

    /**
     * 检查页面缓存大小
     * 如果超过了限制大小，则清除缓存
     */
     checkCacheSize () {
        if (navigator.storage && navigator.storage.estimate) {
            navigator.storage.estimate().then(estimate => {

                const ut = 1024 * 1024;
                var total = estimate.quota
                var usage = estimate.usage
                
                // 超过了限制大小 或者 缓存超过了3G
                if(usage >= total || usage / ut >= 3000) {
                    this.clearCache()
                }
            });
        }
    },

    /**
     * 清理缓存
     */
    clearCache() {
        // 注销时，清除缓存
        if(typeof caches != 'undefined'){
            caches.keys().then(keys => {
                if(keys){
                    keys.forEach(itemKey=> {
                        caches.delete(itemKey)
                    })
                }
            })
        }
    }
}

window.YC_SW = YC_SW;
